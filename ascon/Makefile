all: main

main: main.o core.o permutations.o
	gcc -o main main.o core.o permutations.o --verbose

main.o: main.c core.o permutations.o
	gcc -c main.c

core.o: core.h core.c encrypt.c decrypt.c
	gcc -c core.c encrypt.c decrypt.c
permutations.o: permutations.c permutations.h endian.h
	gcc -c permutations.c

clean:
	rm -r -f *.o