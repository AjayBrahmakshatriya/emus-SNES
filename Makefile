export


BASE_DIR:=$(shell pwd)
SRC_DIR=$(BASE_DIR)/src
INCLUDE_PATH=$(BASE_DIR)/include
BUILD_PATH:=$(BASE_DIR)/build
HEADERS:=$(wildcard $(BASE_DIR)/include/*.h)
TARGET=$(BUILD_PATH)/emu-nes.out


CC=clang
CFLAGS=-m64
LINK_FLAGS=-lSDL2

MAKE_FLAGS=--no-print-directory

all: directories program

.PHONY: directories

directories: $(BUILD_PATH)

$(BUILD_PATH):
	@mkdir $(BUILD_PATH)

program:
	@make $(MAKE_FLAGS) -C src

clean:
	@rm -rf $(BUILD_PATH)
