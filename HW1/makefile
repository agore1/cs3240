#Austin Gore ayg9fh
#Makefile for CS3240 HW1

CC=g++
#Flags are compile but don't link, warn all
CFLAGS=-c -Wall -std=c++11
LFLAGS=-Wall -std=c++11

computeK: computeK.o Point.o
	$(CC) $(LFLAGS) computeK.o Point.o -o computeK.out

computeK.o: computeK.cpp
	$(CC) $(CFLAGS) computeK.cpp

scratch:scratch.o Point.o
	$(CC) $(LFLAGS) scratchwork.o Point.o -o scratch.out

scratch.o: scratchwork.cpp
	$(CC) $(CFLAGS) scratchwork.cpp 

Point.o: Point.cpp Point.h
	$(CC) $(CFLAGS) Point.cpp

clean:
	\rm *.o computeK.out scratch.out