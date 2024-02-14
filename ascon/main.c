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
  int ret = crypto_aead_encrypt(ciphertext, &cipherLen,
                      plaintext, plaintextLen,
                      &tag, sizeof(const unsigned char),
                      NULL, &nonce,
                      &key);

  printf("Ciphertext created by encryption: %s\n", (char *) ciphertext);
  printf("Ciphertext length: %llu\n", cipherLen);
  printf("Return status: %d\n\n", ret);

  void* decrypted;
  unsigned long long decryptedLen;
  ret = crypto_aead_decrypt(decrypted, &decryptedLen,
                      NULL, ciphertext,
                      cipherLen, &tag,
                      sizeof(const unsigned char), &nonce,
                      &key);

  printf("Decrypted ciphertext: %s\n", (char *) decrypted);
  printf("Decrypted ciphertext length: %llu\n", decryptedLen);
  printf("Return status: %d\n\n", ret);

  free(plaintext);
  return 0;
}
