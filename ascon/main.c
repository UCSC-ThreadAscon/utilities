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
  printf("Plaintext length: %llu\n\n", plaintextLen);

  unsigned long long cipherLen;
  int ret = crypto_aead_encrypt(memory, &cipherLen,
                                memory, plaintextLen,
                                &tag, sizeof(const unsigned char),
                                NULL, &nonce,
                                &key);

  printf("Ciphertext created by encryption: %s\n", (char *)memory);
  printf("Ciphertext length: %llu\n", cipherLen);
  printf("Return status: %d\n\n", ret);

  void *decrypted = malloc(4096);
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
  free(decrypted);
}

int main()
{
  example();
  const unsigned char tag = 186;
  const unsigned char nonce = 187;
  const unsigned char key = 130;

  unsigned long long length = 67 * sizeof(char);
  void* memory = malloc(length);

  char packet_bytes[] = {
    0x01, 0x17, 0x04, 0x91, 0x23, 0x08, 0x9f, 0x38,
    0x3a, 0xa5, 0xdd, 0xaa, 0x92, 0x09, 0x27, 0xc1,
    0xf9, 0xf4, 0x0c, 0xd9, 0xe7, 0x11, 0xe5, 0x8e,
    0x62, 0xdb, 0xe9, 0xa7, 0x21, 0x8b, 0x6b, 0x52,
    0x08, 0x3b, 0x74, 0x4b, 0xcb, 0x7b, 0xb4, 0x56,
    0x01, 0x1d, 0x85, 0x37, 0x5d, 0x24, 0x6a, 0x78,
    0x40, 0xf3, 0x8f, 0x66
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
