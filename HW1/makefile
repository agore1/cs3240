#Austin Gore ayg9fh
#Makefile for CS3240 HW1

CC=g++
#Flags are compile but don't link, warn all
CFLAGS=-c -Wall
LFLAGS=-Wall

scratch:scratch.o Point.o
	$(CC) $(LFLAGS) scratchwork.o Point.o -o scratch.out

scratch.o: scratchwork.cpp
	$(CC) $(CFLAGS) scratchwork.cpp 

Point.o: Point.cpp Point.h
	$(CC) $(CFLAGS) Point.cpp

clean:
	\rm *.o 