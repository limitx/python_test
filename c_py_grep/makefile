CFLAGS=-O3 -std=c++0x -pg -D_DEBUG -g -c -Wall
CXXFLAGS += -std=gnu++11


grep.out:main.o Utils.o
	g++ -std=c++11 -o grep.out main.o Utils.o
main.o:main.cpp Utils.h
	g++ -std=c++11 -c main.cpp

Utils.o:Utils.cpp Utils.h
	g++ -std=c++11 -c -fPIC Utils.cpp

libUtils.so:
	g++ -shared -Wl,-soname,libUtils.so -o libUtils.so  Utils.o

clean:
	rm -f main.o Utils.o grep.out
