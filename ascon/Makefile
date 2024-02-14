all: main

main: main.o core.o permutations.o encrypt.o decrypt.o
	gcc -o main main.o core.o permutations.o encrypt.o decrypt.o --verbose

main.o: main.c
	gcc -c main.c

core.o: core.h core.c
	gcc -c core.c

encrypt.o: core.h encrypt.c
	gcc -c encrypt.c

decrypt.o: core.h decrypt.c
	gcc -c decrypt.c
permutations.o: permutations.c permutations.h endian.h
	gcc -c permutations.c

clean:
	rm -r -f *.o