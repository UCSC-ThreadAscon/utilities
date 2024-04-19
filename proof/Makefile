CC = clang 
CFLAGS = -Wall -Werror -Wextra -Wpedantic

ascon_permutations.o: ascon.h ascon_internal.h ascon_permutations.c
	$(CC) $(CFLAGS) -c ascon_permutations.c -g

clean:
	rm -r -f $(wildcard *.o)