CC      = gcc
OBJCOPY = objcopy
CFLAGS  = -O3 -march=native -pipe -fno-plt -flto -fwhole-program \
          -fdata-sections -ffunction-sections -g3 -ggdb
LDFLAGS = -r -nostdlib -Wl,--gc-sections
SRC      = devtools.c
DEPS     = $(wildcard dependencies/*.c)
OBJ_NAME = gentro_devtools.o
DBG_NAME = gentro_devtools.debug
.PHONY: all clean install
all: $(OBJ_NAME)
$(OBJ_NAME): $(SRC) $(DEPS)
	@$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@
	@$(OBJCOPY) --only-keep-debug $@ $(DBG_NAME)
	@$(OBJCOPY) --strip-debug $@
	@$(OBJCOPY) --add-gnu-debuglink=$(DBG_NAME) $@
install: $(OBJ_NAME)
	@install -d /usr/include/gentro
	@install -m 644 devtools.h /usr/include/gentro/
	@install -m 644 $(OBJ_NAME) /usr/lib/
	@install -m 644 $(DBG_NAME) /usr/lib/
clean:
	@rm -f *.o *.debug