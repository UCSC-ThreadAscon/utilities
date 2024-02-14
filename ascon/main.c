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
  void* memory = malloc(plaintextLen);
  char* string = "The brown fox jumped over the lazy dog.";
  memcpy(memory, string, plaintextLen);

  printf("Plaintext before encryption: %s\n", (char *) memory);
  printf("Plaintext length %llu\n\n", plaintextLen);

  unsigned long long cipherLen;
  int ret = crypto_aead_encrypt(memory, &cipherLen,
                      memory, plaintextLen,
                      &tag, sizeof(const unsigned char),
                      NULL, &nonce,
                      &key);

  printf("Ciphertext created by encryption: %s\n", (char *) memory);
  printf("Ciphertext length: %llu\n", cipherLen);
  printf("Return status: %d\n\n", ret);

  void* decrypted;
  unsigned long long decryptedLen;
  ret = crypto_aead_decrypt(decrypted, &decryptedLen,
                      NULL, memory,
                      cipherLen, &tag,
                      sizeof(const unsigned char), &nonce,
                      &key);

  printf("Decrypted ciphertext: %s\n", (char *) decrypted);
  printf("Decrypted ciphertext length: %llu\n", decryptedLen);
  printf("Return status: %d\n\n", ret);

  free(memory);
  return 0;
}
