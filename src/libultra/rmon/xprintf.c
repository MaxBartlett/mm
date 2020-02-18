#include <ultra64.h>
#include <global.h>

#define ATOI(i, a)                                                                                     \
    for (i = 0; *a >= '0' && *a <= '9'; a++)                                                           \
        if (i < 999)                                                                                   \
            i = *a + i * 10 - '0';
#define _PROUT(fmt, _size)                                                                        \
    if (_size > 0) {                                                                                   \
        arg = (void*)pfn(arg, fmt, _size);                                                                  \
        if (arg != 0)                                                                                  \
            x.nchar += _size;                                                                        \
        else                                                                                           \
            return x.nchar;                                                                          \
    }
#define _PAD(m, src, extracond)                                                                       \
    if (extracond && m > 0) {                                                                          \
        int i;                                                                                         \
        int j;                                                                                         \
        for (j = m; j > 0; j -= i) {                                                                   \
            if ((u32) j > 32)                                                                          \
                i = 32;                                                                                \
            else                                                                                       \
                i = j;                                                                                 \
            _PROUT(src, i);                                                                       \
        }                                                                                              \
    }

#define FLAGS_SPACE 1
#define FLAGS_PLUS 2
#define FLAGS_MINUS 4
#define FLAGS_HASH 8
#define FLAGS_ZERO 16

// TODO .data section should be included after boot .data is split
//char spaces[] = "                                ";
//char zeroes[] = "00000000000000000000000000000000";

int _Printf(printf_func pfn, void* arg, char* fmt, va_list ap) {
    _Pft x;
    x.nchar = 0;
    while (1) {
        unsigned char* s;
        unsigned char c;
        unsigned char* t;

        static const char fchar[] = " +-#0";
        static const u32 fbit[] = { FLAGS_SPACE, FLAGS_PLUS, FLAGS_MINUS, FLAGS_HASH, FLAGS_ZERO, 0 };

        unsigned char ac[0x20];

        s = fmt;
        while ((c = *s) != 0 && c != '%') {
            s++;
        }
        _PROUT(fmt, s - fmt);
        if (c == 0) {
            return x.nchar;
        }
        fmt = (char *) ++s;
        x.flags = 0;
        // TODO the cast isn't necessary because strchr should take it in as const, but it currently doesn't
        for (; (t = strchr((char*)fchar, *s)) != NULL; s++) {
            x.flags |= fbit[t - fchar];
        }
        if (*s == '*') {
            x.width = va_arg(ap, s32);
            if (x.width < 0) {
                x.width = -x.width;
                x.flags |= FLAGS_MINUS;
            }
            s++;
        } else {
            ATOI(x.width, s);
        }
        if (*s != '.') {
            x.prec = -1;
        } else {
            s++;
            if (*s == '*') {
                x.prec = va_arg(ap, s32);
                s++;
            } else {
                ATOI(x.prec, s);
            }
        }
        if (strchr("hlL", *s) != NULL) {
            x.qual = *s++;
        } else {
            x.qual = 0;
        }

        if (x.qual == 'l' && *s == 'l') {
            x.qual = 'L';
            s++;
        }
        _Putfld(&x, &ap, *s, ac);
        x.width -= x.n0 + x.nz0 + x.n1 + x.nz1
                      + x.n2 + x.nz2;
        _PAD(x.width, spaces, !(x.flags & FLAGS_MINUS));
        _PROUT((char *) ac, x.n0);
        _PAD(x.nz0, zeroes, 1);
        _PROUT(x.s, x.n1);
        _PAD(x.nz1, zeroes, 1);
        _PROUT((char *) (&x.s[x.n1]), x.n2)
        _PAD(x.nz2, zeroes, 1);
        _PAD(x.width, spaces, x.flags & FLAGS_MINUS);
        fmt = (char *) s + 1;
    }
}

void _Putfld(_Pft* px, va_list* pap, unsigned char code, unsigned char* ac) {
    px->n0 = px->nz0 = px->n1 = px->nz1 = px->n2 =
        px->nz2 = 0;

    switch (code) {

        case 'c':
            ac[px->n0++] = va_arg(*pap, u32);
            break;

        case 'd':
        case 'i':
            if (px->qual == 'l') {
                px->v.ll = va_arg(*pap, s32);
            } else if (px->qual == 'L') {
                px->v.ll = va_arg(*pap, s64);
            } else {
                px->v.ll = va_arg(*pap, s32);
            }

            if (px->qual == 'h') {
                px->v.ll = (s16) px->v.ll;
            }

            if (px->v.ll < 0) {
                ac[px->n0++] = '-';
            } else if (px->flags & FLAGS_PLUS) {
                ac[px->n0++] = '+';
            } else if (px->flags & FLAGS_SPACE) {
                ac[px->n0++] = ' ';
            }

            px->s = (char *) &ac[px->n0];

            _Litob(px, code);
            break;

        case 'x':
        case 'X':
        case 'u':
        case 'o':
            if (px->qual == 'l') {
                px->v.ll = va_arg(*pap, s32);
            } else if (px->qual == 'L') {
                px->v.ll = va_arg(*pap, s64);
            } else {
                px->v.ll = va_arg(*pap, s32);
            }

            if (px->qual == 'h') {
                px->v.ll = (u16) px->v.ll;
            } else if (px->qual == 0) {
                px->v.ll = (u32) px->v.ll;
            }

            if (px->flags & FLAGS_HASH) {
                ac[px->n0++] = '0';
                if (code == 'x' || code == 'X') {

                    ac[px->n0++] = code;
                }
            }
            px->s = (char *) &ac[px->n0];
            _Litob(px, code);
            break;

        case 'e':
        case 'f':
        case 'g':
        case 'E':
        case 'G':
            px->v.ld = px->qual == 'L' ? va_arg(*pap, f64) : va_arg(*pap, f64);

            if (*(u16*)&px->v.ll & 0x8000) {
                ac[px->n0++] = '-';
            } else {
                if (px->flags & FLAGS_PLUS) {
                    ac[px->n0++] = '+';
                } else if (px->flags & FLAGS_SPACE) {
                    ac[px->n0++] = ' ';
                }
            }

            px->s = (char *) &ac[px->n0];
            _Ldtob(px, code);
            break;

        case 'n':
            if (px->qual == 'h') {
                *(va_arg(*pap, u16 *)) = px->nchar;
            } else if (px->qual == 'l') {
                *va_arg(*pap, u32 *) = px->nchar;
            } else if (px->qual == 'L') {
                *va_arg(*pap, u64 *) = px->nchar;
            } else {
                *va_arg(*pap, u32 *) = px->nchar;
            }
            break;

        case 'p':
            px->v.ll = (long) va_arg(*pap, void *);
            px->s = (char *) &ac[px->n0];
            _Litob(px, 'x');
            break;

        case 's':
            px->s = va_arg(*pap, char *);
            px->n1 = strlen(px->s);
            if (px->prec >= 0 && px->n1 > px->prec) {
                px->n1 = px->prec;
            }
            break;

        case '%':
            ac[px->n0++] = '%';
            break;

        default:
            ac[px->n0++] = code;
            break;
    }
}