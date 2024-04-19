CC = clang 
CFLAGS = -Wall -Werror -Wextra -Wpedantic

ascon_permutations.o: libascon/src/ascon_internal.h libascon/src/ascon_permutations.c
	$(CC) $(CFLAGS) -c libascon/src/ascon_permutations.c -g

clean:
	rm -r -f $(wildcard *.o)