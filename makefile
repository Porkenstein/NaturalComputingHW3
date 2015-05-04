gray-scott: Source.o

	g++ Source.o -g -std=c++11 -Wall -O3 -lm -o gray-scott


Source.o: Source.cpp

	g++ -g -std=c++11 -Wall -O3 -c Source.cpp


clean:

	rm -rf *o gray-scott
