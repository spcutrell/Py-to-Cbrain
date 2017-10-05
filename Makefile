CC=gcc
CFLAGS=-Wall -Wextra
SOURCE=cbrain.c
TARGET=cbrain

.PHONY: all clean debug 

all:
	$(CC) -o $(TARGET) $(CFLAGS) $(SOURCE) 

debug:
	$(CC) -o $(TARGET) $(CFLAGS) -g $(SOURCE) 

clean:
	rm $(TARGET)
