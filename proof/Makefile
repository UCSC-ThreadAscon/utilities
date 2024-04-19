CC = clang 
CFLAGS = -Wall -Werror -Wextra -Wpedantic
HEADERS = ascon.h ascon_internal.h

all: ascon_permutations.o

ascon_permutations.o: $(HEADERS) ascon_permutations.c
	$(CC) $(CFLAGS) -c ascon_permutations.c -g

clean:
	rm -r -f $(wildcard *.o)