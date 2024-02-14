#include "core.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "stdint.h"
#include "inttypes.h"

int main() {
  const unsigned char key = 186;
  const unsigned char nonce = 187;
  const unsigned char tag = 130;

  unsigned long long plaintextLen = 67;
  void* memory = malloc(plaintextLen);
  char packet_bytes[] = {
    0x09, 0x3a, 0xcf, 0x14, 0x48, 0xda, 0xcf, 0xba,
    0xc7, 0xb1, 0xfd, 0xe7, 0x3f, 0xb9, 0xa7, 0xc5,
    0x1b, 0xee, 0x94, 0xb1, 0x56, 0x14, 0xe0, 0xea,
    0x41, 0x4c, 0xc1, 0x28, 0xb6, 0x6a, 0x0b, 0x6e,
    0xd7, 0x86, 0xe5, 0xb5, 0x42, 0x14, 0x26, 0x76,
    0xf7, 0x6f, 0x2c, 0xf8, 0xb0, 0x14, 0x27, 0x7a,
    0xca, 0xe8, 0xd0, 0xe6, 0x0d, 0xe9, 0x70, 0xcd,
    0xb6, 0x7b, 0xc8, 0x30, 0x74, 0xc4, 0x53, 0xf6,
    0xbe, 0x35, 0x2b
  };
  memcpy(memory, packet_bytes, plaintextLen);

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
