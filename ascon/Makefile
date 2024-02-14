all: main

main: main.o core.o permutations.o
	gcc -o main main.o core.o permutations.o

main.o: main.c core.o permutations.o
	gcc -c main.c

core.o: core.h
	gcc -c core.c
permutations.o: permutations.c permutations.h endian.h
	gcc -c permutations.c

clean:
	rm -r -f *.o