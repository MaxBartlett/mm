CC := gcc
CFLAGS := -Wall -Wextra -pedantic -std=c99 -g -O2
PROGRAMS := yaz0 makeromfs elf2rom mkldscript vtxdis

all: $(PROGRAMS)
	$(MAKE) -C ZAPD

clean:
	$(RM) $(PROGRAMS)
	$(MAKE) -C ZAPD clean
# Need to clean the above line later...

mkldscript_SOURCES := mkldscript.c util.c
elf2rom_SOURCES    := elf2rom.c elf32.c n64chksum.c util.c
yaz0_SOURCES       := yaz0tool.c yaz0.c util.c
makeromfs_SOURCES  := makeromfs.c n64chksum.c util.c
vtxdis_SOURCES	   := vtxdis.c

define COMPILE =
$(1): $($1_SOURCES)
	$(CC) $(CFLAGS) $$^ -o $$@
endef

$(foreach p,$(PROGRAMS),$(eval $(call COMPILE,$(p))))
