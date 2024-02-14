#include "core.h"
#include "api.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "stdint.h"
#include "inttypes.h"

void example()
{
  const unsigned char tag = 186;
  const unsigned char nonce = 187;
  const unsigned char key = 130;

  unsigned long long plaintextLen = 40 * sizeof(char);
  void *memory = malloc(plaintextLen);
  char *string = "The brown fox jumped over the lazy dog.";
  memcpy(memory, string, plaintextLen);

  printf("Plaintext before encryption: %s\n", (char *)memory);
  printf("Plaintext length %llu\n\n", plaintextLen);

  unsigned long long cipherLen;
  int ret = crypto_aead_encrypt(memory, &cipherLen,
                                memory, plaintextLen,
                                &tag, sizeof(const unsigned char),
                                NULL, &nonce,
                                &key);

  printf("Ciphertext created by encryption: %s\n", (char *)memory);
  printf("Ciphertext length: %llu\n", cipherLen);
  printf("Return status: %d\n\n", ret);

  void *decrypted;
  unsigned long long decryptedLen;
  ret = crypto_aead_decrypt(decrypted, &decryptedLen,
                            NULL, memory,
                            cipherLen, &tag,
                            sizeof(const unsigned char), &nonce,
                            &key);

  printf("Decrypted ciphertext: %s\n", (char *)decrypted);
  printf("Decrypted ciphertext length: %llu\n", decryptedLen);
  printf("Return status: %d\n\n", ret);

  free(memory);
}

int main()
{
  const unsigned char tag = 186;
  const unsigned char nonce = 187;
  const unsigned char key = 130;

  unsigned long long length = 67 * sizeof(char);
  void* memory = malloc(length);

  char packet_bytes[] = {
    0x58, 0xa1, 0x8d, 0x89, 0x2f, 0x8d, 0xa3, 0x7f,
    0x78, 0xd4, 0x7e, 0xa3, 0xe0, 0x9d, 0xe9, 0xf7,
    0x52, 0x76, 0x7e, 0x19, 0xf2, 0x60, 0xc4, 0xbd,
    0x9d, 0xac, 0x9c, 0x49, 0x3c, 0xe6, 0x24, 0x5b,
    0x69, 0x75, 0x9b, 0xfa, 0x7a, 0x9e, 0xba, 0xd9,
    0x10, 0x96, 0x9f, 0x38, 0x2e, 0xfb, 0x1b, 0x8e,
    0x73, 0x73, 0x83, 0x11, 0xd1, 0x37, 0xcc, 0xe4,
    0x0a, 0x0e, 0x98, 0x9f, 0xa8, 0x0a, 0x80, 0xb8,
    0x83, 0x4b, 0x14
  };
  memcpy(memory, &packet_bytes, length);

  printf("Ciphertext: %s\n", (char *) packet_bytes);
  printf("Ciphertext length: %llu\n\n", length);

  void *decrypted = malloc(4096);
  unsigned long long decryptedLen;
  int ret = crypto_aead_decrypt(decrypted, &decryptedLen,
                                NULL, memory,
                                length, &tag,
                                sizeof(const unsigned char), &nonce,
                                &key);

  printf("Decrypted ciphertext: %s\n", (char *)decrypted);
  printf("Decrypted ciphertext length: %llu\n", decryptedLen);
  printf("Return status: %d\n\n", ret);

  return 0;
}
