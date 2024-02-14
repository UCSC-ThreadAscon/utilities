all: core

core: core.o
	gcc -O -o core core.o decrypt.o encrypt.o permutations.o

core.o: decrypt.o encrypt.o
	gcc -O -c core.c

decrypt.o: permutations.o decrypt.c
	gcc -O -c decrypt.c
encrypt.o: permutations.o encrypt.c
	gcc -O -c encrypt.c
permutations.o: permutations.c permutations.h endian.h api.h
	gcc -O -c permutations.c

clean:
	rm -r -f *.o