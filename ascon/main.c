#include "core.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

int main() {
  const unsigned char tag = 186;
  const unsigned char nonce = 187;
  const unsigned char key = 130;

  void* plaintext = calloc(40, sizeof(char));
  char* string = "The brown fox jumped over the lazy dog.";
  memcpy(plaintext, string, sizeof(char) * 40);
  printf("Text to be encrypted: %s\n", (char *) plaintext);

  free(plaintext);
  return 0;
}
