#include "core.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "stdint.h"
#include "inttypes.h"

int main() {
  const unsigned char tag = 186;
  const unsigned char nonce = 187;
  const unsigned char key = 130;

  unsigned long long plaintextLen = 40 * sizeof(char);
  void* plaintext = malloc(plaintextLen);
  char* string = "The brown fox jumped over the lazy dog.";
  memcpy(plaintext, string, plaintextLen);

  printf("Plaintext before encryption: %s\n", (char *) plaintext);
  printf("Plaintext length %llu\n\n", plaintextLen);

  void* ciphertext;
  unsigned long long cipherLen;
  crypto_aead_encrypt(ciphertext, &cipherLen,
                      plaintext, plaintextLen,
                      &tag, sizeof(const unsigned char),
                      NULL, &nonce,
                      &key);

  printf("Ciphertext created by encryption %s\n", (char *) ciphertext);
  printf("Ciphertext length %llu\n\n", cipherLen);

  free(plaintext);
  return 0;
}
