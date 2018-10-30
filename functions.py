known_funcs = {
    0x80080060:("func_80080060","UNK_RET","void"),
    0x80080150:("func_80080150","void","UNK_PTR, UNK_PTR"),
    0x80080180:("func_80080180","void","UNK_TYPE*, UNK_TYPE, UNK_TYPE"),
    0x8008019C:("func_8008019C","UNK_RET","void"),
    0x800801EC:("func_800801EC","UNK_RET","void"),
    0x80080250:("func_80080250","UNK_RET","void"),
    0x80080300:("func_80080300","UNK_RET","UNK_TYPE"),
    0x8008038C:("func_8008038C","UNK_RET","void"),
    0x80080514:("func_80080514","void","UNK_TYPE"),
    0x800805E0:("func_800805E0","UNK_RET","UNK_TYPE"),
    0x80080C04:("func_80080C04","UNK_RET","UNK_PTR, UNK_FUN_ARG, UNK_PTR, UNK_TYPE, UNK_TYPE, UNK_PTR, UNK_TYPE"),
    0x80080D0C:("func_80080D0C","UNK_RET","void"),
    0x80080E00:("func_80080E00","UNK_RET","void"),
    0x80081754:("func_80081754","UNK_RET","UNK_PTR, struct s80085320*, UNK_TYPE, UNK_TYPE"),
    0x80081820:("func_80081820","void","void"),
    0x80081828:("func_80081828","void","void"),
    0x80081830:("func_80081830","void","void"),
    0x8008189C:("func_8008189C","void","void"),
    0x800818D0:("func_800818D0","void","void"),
    0x800818F4:("func_800818F4","void","void"),
    0x800819F0:("func_800819F0","UNK_RET","UNK_PTR, void(*)(UNK_TYPE, UNK_TYPE), UNK_TYPE, UNK_TYPE"),
    0x80081AD4:("func_80081AD4","UNK_RET","UNK_PTR"),
    0x80081BCC:("func_80081BCC","UNK_RET","UNK_PTR, UNK_TYPE(*)(UNK_TYPE, UNK_TYPE), UNK_TYPE"),
    0x80081CA4:("func_80081CA4","UNK_RET","UNK_PTR"),
    0x8008439C:("func_8008439C","UNK_RET","UNK_TYPE, UNK_TYPE"),
    0x800847CC:("func_800847CC","UNK_RET","UNK_PTR, ..."), # printf?
    0x8008481C:("func_8008481C","UNK_RET","UNK_TYPE, UNK_TYPE, UNK_PTR, UNK_PTR"),
    0x80085320:("func_80085320","void","struct s80085320*, UNK_PTR, UNK_PTR, UNK_TYPE, UNK_TYPE, UNK_PTR"),
    0x800853F8:("func_800853F8","UNK_RET","struct s80085320*"),
    0x80085468:("func_80085468","UNK_TYPE","struct s80085320*"),
    0x800854E0:("func_800854E0","UNK_TYPE","UNK_ARGS"),
    0x80085538:("func_80085538","UNK_RET","struct s80085320*"),
    0x80087830:("func_80087830","UNK_TYPE","UNK_TYPE, UNK_TYPE, UNK_TYPE"),
    0x80087854:("func_80087854","UNK_TYPE","u8*, UNK_TYPE, UNK_PTR"),
    0x800878A4:("func_800878A4","UNK_TYPE","u8*, UNK_TYPE, UNK_TYPE, UNK_TYPE"),
    0x80087A6C:("func_80087A6C","UNK_RET","UNK_TYPE"),
    0x80087B00:("__osSetCause","void","u32 value"),
    0x80087B10:("osSendMesg","s32","OSMesgQueue* mq, OSMesg msg, s32 flags"),
    0x80087E00:("func_80087E00","void","u32"),
    0x80087E10:("osStopThread","void","OSThread* t"),
    0x80087ED0:("osRecvMesg","s32","OSMesgQueue* mq, OSMesg* msg, s32 flags"),
    0x80088010:("osSetIntMask","OSIntMask","OSIntMask im"),
    0x800880B0:("osGetIntMask","OSIntMask","void"),
    0x80088350:("__sinf","float","float x"), # multiple names? __sinf/fsin/sinf
    0x80088510:("sins","short","unsigned short x"),
    0x80088580:("_VirtualToPhysicalTask","OSTask*","OSTask* intp"), # Note: not exported
    0x8008868C:("osSpTaskLoad","void","OSTask* intp"),
    0x800887F4:("osSpTaskStartGo","void","OSTask* tp"),
    0x80088840:("__ull_rshift","long long","unsigned long long left, long long right"),
    0x8008886C:("__ull_rem","unsigned long long","unsigned long long left, unsigned long long right"),
    0x800888A8:("__ull_div","unsigned long long","unsigned long long left, unsigned long long right"),
    0x800888E4:("__ll_lshift","long long","long long left, long long right"),
    0x80088910:("__ll_rem","long long","long long left, unsigned long long right"),
    0x8008894C:("__ll_div","long long","long long left, long long right"),
    0x800889A8:("__ll_mul","long long","long long left, long long right"),
    0x800889D8:("__ull_divremi","void","unsigned long long* quotient, unsigned long long* remainder, unsigned long long dividend, unsigned short divisor"),
    0x80088A38:("__ll_mod","long long","long long left, long long right"),
    0x80088AD4:("__ll_rshift","long long","long long left, long long right"),
    0x80088B00:("__osExceptionPreamble","UNK_RET","UNK_ARGS"),
    0x80088B10:("__osException","UNK_RET","UNK_ARGS"),
    0x8008905C:("send_mesg","UNK_RET","UNK_ARGS"),
    0x80089110:("handle_CpU","UNK_RET","UNK_ARGS"),
    0x80089144:("__osEnqueueAndYield","UNK_RET","OSThread**"),
    0x80089244:("__osEnqueueThread","UNK_RET","UNK_PTR, OSThread*"),
    0x8008928C:("__osPopThread","OSThread*","OSThread**"),
    0x800892A4:("__osDispatchThread","UNK_RET","void"), # TODO is this really void?
    0x80089420:("__osCleanupThread","UNK_RET","UNK_ARGS"),
    0x80089430:("__osDequeueThread","UNK_RET","OSThread**, OSThread*"),
    0x80089470:("osDestroyThread","void","OSThread* t"),
    0x80089630:("_blkclr","UNK_RET","u8*, u32"), # multiple names? bzero/_bzero/blkclr/_blkclr
    0x80089AA0:("__osSiCreateAccessQueue","void","void"),
    0x80089AF0:("__osSiGetAccess","void","void"),
    0x80089B34:("__osSiRelAccess","void","void"),
    0x80089B60:("osContInit","s32","OSMesgQueue* mq, u8* bitpattern, OSContStatus* data"),
    0x80089CBC:("__osContGetInitData","void","u8* pattern, OSContStatus* data"),
    0x80089D68:("__osPackRequestData","void","u8 cmd"),
    0x80089E40:("osCreateThread","void","OSThread* t, OSId id, void (*entry)(void*), void* arg, void* sp, OSPri p"),
    0x80089F90:("osContStartReadData","s32","OSMesgQueue* mq"),
    0x8008A014:("osContGetReadData","void","OSContPad* data"),
    0x8008A540:("osVirtualToPhysical","u32","void* virtualAddress"),
    0x8008A5C0:("__osGetSR","u32","void"),
    0x8008A5D0:("__osSetSR","void","u32 value"),
    0x8008A5E0:("osWritebackDCache","void","void *vaddr, s32 nbytes"),
    0x8008A660:("func_8008A660","void","void"),
    0x8008A6FC:("func_8008A6FC","void","void"),
    0x8008A9A8:("func_8008A9A8","void","void"),
    0x8008AA50:("guPerspectiveF","void","float* mf[4], u16* perspNorm, float fovy, float aspect, float near, float far, float scale"),
    0x8008AC80:("guPerspective","void","Mtx* m, u16* perspNorm, float fovy, float aspect, float near, float far, float scale"),
    0x8008ACE0:("__osSpRawStartDma","s32","s32 direction, u32 devAddr, void* dramAddr, u32 size"),
    0x8008AD70:("__osSiRawStartDma","s32","s32 direction, void* dramAddr"),
    0x8008AE70:("func_8008AE70","UNK_RET","UNK_TYPE"),
    0x8008AEE0:("func_8008AEE0","UNK_TYPE","UNK_TYPE, UNK_PTR"),
    0x8008AF30:("osGetThreadId","OSId","OSThread* t"),
    0x8008AF50:("osSpTaskYield","void","void"),
    0x8008B650:("func_8008B650","UNK_RET","UNK_PTR"),
    0x8008B6B0:("__osGetConfig","u32 ","void "),
    0x8008B6C0:("__osSetConfig","void ","u32 value"),
    0x8008BE70:("osStopTimer","int","OSTimer* t"),
    0x8008BF60:("__osProbeTLB","u32","void*"),
    0x8008C020:("osCreatePiManager","void","OSPri pri, OSMesgQueue* cmdQ, OSMesg* cmdBuf, s32 cmdMsgCnt"),
    0x8008C190:("__osPiCreateAccessQueue","void","void"),
    0x8008C1E0:("__osPiGetAccess","void","void"),
    0x8008C224:("__osPiRelAccess","void","void"),
    0x8008D2C0:("osGetCount","u32","void"),
    0x8008D350:("func_8008D350","UNK_TYPE","void"),
    0x8008D640:("osSetEventMesg","void","OSEvent e, OSMesgQueue* mq, OSMesg m"),
    0x8008D700:("sqrtf","UNK_RET","UNK_ARGS"),
    0x8008D730:("osContStartQuery","s32","OSMesgQueue* mq"),
    0x8008D7AC:("osContGetQuery","void","OSContStatus* data"),
    0x8008E050:("_Printf","int","void* (*pfn)(void*), void* arg, const unsigned char* fmt, va_list ap"),
    0x8008E698:("func_8008E698","UNK_RET","UNK_ARGS"), # this does not have a name? (maybe not exported idk) (_Putfld?)
    0x8008EDE0:("osUnmapTLBAll","void","void"),
    0x8008EE30:("osPiStartDma","s32","OSIoMesg* mb, s32 priority, s32 direction, u32 devAddr, void* dramAddr, u32 size, OSMesgQueue* mq"),
    0x8008F1A0:("strchr","unsigned char*","const unsigned char* s, int c"),
    0x8008F1E0:("strlen","size_t","const unsigned char* s"), # unsigned int == size_t
    0x8008F208:("memcpy","void*","void* s1, const void* s2, size_t n"), # unsigned int == size_t
    0x8008F240:("osCreateMesgQueue","void","OSMesgQueue* mq, OSMesg* msg, s32 msgCount"),
    0x8008F270:("osInvalICache","void","void *vaddr, s32 nbytes"),
    0x8008F2F0:("osInvalDCache","void","void *vaddr, s32 nbytes"),
    0x8008F3A0:("__osTimerServicesInit","void","void"),
    0x8008F42C:("__osTimerInterrupt","void","void"),
    0x8008F5A4:("__osSetTimerIntr","void","OSTime tim"),
    0x8008F644:("__osInsertTimer","OSTime","OSTimer* t"),
    0x8008FA00:("__osSpDeviceBusy","int","void"),
    0x8008FA30:("__osSiDeviceBusy","int","void"),
    0x8008FAB0:("osJamMesg","s32","OSMesgQueue* mq, OSMesg msg, s32 flags"),
    0x8008FC00:("osSetThreadPri","void","OSThread* t, OSPri p"),
    0x8008FCE0:("osGetThreadPri","OSPri","OSThread* t"),
    0x8008FE60:("func_8008FE60","UNK_RET","UNK_PTR"),
    0x800902A0:("osSpTaskYielded","void","void"),
    0x80090300:("memcmp","UNK_RET","UNK_ARGS"), # multiple names? memcmp/bcmp/_bcmp
    0x80090420:("osGetTime","OSTime","void"),
    0x80090680:("__osSetGlobalIntMask","UNK_RET","UNK_ARGS"),
    0x80091280:("__osSetCompare","void","u32 value"),
    0x80091290:("__osGetCompare","u32","void"),
    0x800912A0:("osDpGetStatus","u32","void"),
    0x800912B0:("osDpSetStatus","void","u32 data"),
    0x800912C0:("_bcopy","void","const void* src, void* dst, size_t n"), # multiple names? bcopy/_bcopy
    0x800915D0:("__osResetGlobalIntMask","UNK_RET","UNK_ARGS"),
    0x800918A0:("guOrthoF","void","float* mf[4], float l, float r, float b, float t, float n, float f, float scale"),
    0x800919F4:("guOrtho","void","Mtx* m, float l, float r, float b, float t, float n, float f, float scale"),
    0x80091A60:("__osDisableInt","u32","void"),
    0x80091AD0:("__osRestoreInt","void","u32"),
    0x80091AF0:("__osViInit","void","void"),
    0x80091C10:("__osViSwapContext","void","void"),
    0x80091F10:("osPiGetCmdQueue","OSMesgQueue*","void"),
    0x80091f40:("__cosf","float","float x"), # multiple names? __cosf/fcos/cosf
    0x80092100:("func_80092100","UNK_RET","UNK_TYPE"),
    0x80092260:("coss","short","unsigned short x"),
    0x80092290:("osSetTime","void","OSTime ticks"),
    0x80092920:("func_80092920","struct s80092920*","void"),
    0x80092C80:("osContSetCh","s32","u8 ch"),
    0x80092CE0:("__osSetFpcCsr","void","u32 value"),
    0x80092CF0:("__osGetFpcCsr","u32","void"),
    0x80093BA0:("osAiGetLength","u32","void"),
    0x80093C00:("osMapTLBRdb","void","void"),
    0x80093C60:("osYieldThread","void","void"),
    0x80093D90:("__osGetCause","u32","void"),
    0x80094150:("osSetTimer","int","OSTimer* t, OSTime value, OSTime interval, OSMesgQueue* mq, OSMesg msg"),
    0x800942E0:("_Ldtob","void","_Pft* px, unsigned char code"),
    0x80094770:("func_80094770","UNK_RET","UNK_ARGS"), # this does not have a name? (maybe not exported idk) (_Ldunscale?)
    0x80094828:("func_80094828","UNK_RET","UNK_ARGS"), # this does not have a name? (maybe not exported idk) (_Genld?)
    0x80094DF0:("ldiv","ldiv_t","long numer, long denom"),
    0x80094E74:("lldiv","lldiv_t","long long numer, long long denom"),
    0x80094F80:("_Litob","void","_Pft* px, unsigned char code"),
    0x80095220:("__osSiRawWriteIo","s32","u32 devAddr, u32* data"),
    0x80095270:("__osSpGetStatus","u32","void"),
    0x80095280:("__osSpSetStatus","void","u32 data"),
    0x800952A0:("osCreateViManager","void","OSPri pri"),
    0x800955F0:("__osGetCurrFaultedThread","OSThread*","void"),
    0x800955B0:("__osViGetCurrentContext","__OSViContext*","void"),
    0x800955C0:("osWritebackDCacheAll","void","void"),
    0x80095740:("guMtxF2L","void","float* mf[4], Mtx* m"),
    0x800957B0:("osStartThread","void","OSThread* t"),
    0x80095900:("func_80095900","void","f32"),
    0x80095950:("func_80095950","UNK_RET","f32"),
    0x80095A60:("__d_to_ll","long long","double d"),
    0x80095A7C:("__f_to_ll","long long","float f"),
    0x80095A98:("__d_to_ull","unsigned long long","double d"),
    0x80095B38:("__f_to_ull","unsigned long long","float f"),
    0x80095BD4:("__ll_to_d","double","long long l"),
    0x80095BEC:("__ll_to_f","float","long long l"),
    0x80095C04:("__ull_to_d","double","unsigned long long l"),
    0x80095C38:("__ull_to_f","float","unsigned long long l"),
    0x80096510:("__osSpSetPc","s32","u32 data"),
    0x80096820:("func_80096820","UNK_RET","UNK_TYPE"),
    0x800968B0:("func_800968B0","u32","const u8*, const u8*"),
    0x80097540:("osViModeNtscHpf1","UNK_RET","UNK_ARGS"),
    0x80097eb0:("osViModeNtscHpn1","UNK_RET","UNK_ARGS"),
    0x80097fc0:("osViModeNtscLan1","UNK_RET","UNK_ARGS"),
    0x80098010:("osViModeMpalLan1","UNK_RET","UNK_ARGS"),
    0x800991a0:("__osRcpImTable","UNK_RET","UNK_ARGS"),
    0x80099450:("__libm_qnan_f","UNK_RET","UNK_ARGS"),
    0x800A5AC0:("func_800A5AC0","UNK_RET","void*, UNK_TYPE"), # guessing this is void* bc it's a thread entry point
    0x800A5B6C:("func_800A5B6C","UNK_RET","struct s800A5AC0*, UNK_TYPE"),
    0x800A5B98:("func_800A5B98","UNK_RET","struct s800A5AC0*, UNK_TYPE"),
    0x800A5C28:("func_800A5C28","UNK_RET","struct s800A5AC0*"),
    0x800A5C60:("func_800A5C60","UNK_RET","struct s800A5AC0*, UNK_TYPE"),
    0x800A5CB8:("func_800A5CB8","UNK_RET","struct s800A5AC0*, UNK_TYPE"),
    0x800B3BA4:("func_800B3BA4","UNK_RET","UNK_PTR, UNK_TYPE, UNK_PTR, UNK_TYPE"),
    0x800B3FC0:("func_800B3FC0","UNK_TYPE","UNK_TYPE"),
    0x800B675C:("func_800B675C","UNK_RET","struct s800A5AC0*, UNK_TYPE"),
    0x800B84D0:("func_800B84D0","UNK_TYPE","struct s800A5AC0*, UNK_TYPE"),
    0x800B863C:("func_800B863C","UNK_RET","struct s800A5AC0*, UNK_TYPE"),
    0x800B867C:("func_800B867C","UNK_TYPE","struct s800A5AC0*"),
    0x800BDFC0:("func_800BDFC0","UNK_RET","UNK_TYPE, UNK_TYPE, UNK_TYPE, struct s800A5AC0*"),
    0x800C6024:("func_800C6024","UNK_TYPE","UNK_TYPE"),
    0x800C6248:("func_800C6248","UNK_TYPE","UNK_TYPE, UNK_TYPE"),
    0x800CAAD0:("func_800CAAD0","UNK_RET","UNK_TYPE, UNK_TYPE, UNK_TYPE"),
    0x800CAC0C:("func_800CAC0C","UNK_RET","UNK_TYPE, UNK_TYPE, UNK_TYPE"),
    0x800CACA0:("func_800CACA0","UNK_RET","UNK_TYPE, UNK_TYPE, UNK_TYPE"),
    0x800CAD2C:("func_800CAD2C","UNK_TYPE","UNK_TYPE, UNK_TYPE, UNK_TYPE"),
    0x800CAE88:("func_800CAE88","UNK_RET","UNK_TYPE"),
    0x800CAF24:("func_800CAF24","UNK_RET","UNK_TYPE"),
    0x800CAF38:("func_800CAF38","UNK_RET","UNK_TYPE"),
    0x800E03A0:("func_800E03A0","s800E03A0*","s32"),
    0x800E03CC:("func_800E03CC","void","u8*"),
    0x800E11EC:("func_800E11EC","UNK_RET","UNK_TYPE, UNK_PTR"),
    0x800E1374:("func_800E1374","UNK_RET","UNK_TYPE, UNK_PTR, struct s800A5AC0*, UNK_PTR"),
    0x800E2928:("func_800E2928","UNK_RET","UNK_TYPE, UNK_TYPE, UNK_PTR"),
    0x800E7DF8:("func_800E7DF8","UNK_RET","struct s800A5AC0*, UNK_PTR"),
    0x800FFADC:("func_800FFADC","UNK_RET","struct s800A5AC0*, UNK_PTR"),
    0x80138C88:("func_80138C88","UNK_RET","UNK_PTR, UNK_PTR, UNK_PTR"),
    0x80139188:("func_80139188","UNK_TYPE","UNK_PTR, UNK_PTR"),
    0x80139894:("func_80139894","UNK_RET","UNK_PTR, UNK_TYPE, UNK_TYPE, UNK_TYPE, UNK_TYPE, UNK_TYPE, UNK_TYPE, f32, f32, f32"),
    0x80174BF0:("func_80174BF0","UNK_RET","UNK_TYPE"),
    0x80183070:("func_80183070","void","void"),
    0x8018349C:("func_8018349C","UNK_RET","UNK_TYPE, UNK_TYPE"),

    # ovl_En_Test
    #0x80862B70:("func_80862B70","void","void* a0"),
    #0x80862CBC:("func_80862CBC","UNK_RET","UNK_ARGS"),
    #0x80862EDC:("func_80862EDC","UNK_RET","UNK_ARGS"),
    #0x80863048:("func_80863048","UNK_RET","UNK_ARGS"),
    #0x80863188:("func_80863188","UNK_RET","UNK_ARGS"),
    #0x80863310:("func_80863310","UNK_RET","UNK_ARGS"),
    #0x8086333C:("func_8086333C","UNK_RET","UNK_ARGS"),
    #0x808634B8:("func_808634B8","UNK_RET","UNK_ARGS"),
    #0x808636A8:("func_808636A8","UNK_RET","UNK_ARGS"),
    }
