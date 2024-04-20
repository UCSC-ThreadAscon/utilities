/**
 * --- TO-DO ---
 * 1. A function to get the key
 * 2. A function to get the nonce
 * 3. A function to get the associated data
 * 4. Get the tag.
 * 5. Get the packet bytes.
 * 4. Then given (1)-(3), decrypt!
 *
 * ---- NOTE ----
 * You must use the ACTUAL BYTES or the key, NOT its string representation.
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdbool.h>

#include "ascon.h"
#include "common.h"

void* createAssocData(void* dstAddrBytes, void* srcAddrBytes,
                      size_t dstAddrSize, size_t srcAddrSize)
{
  void* assocData = calloc(1, CRYPTO_ABYTES);

  uint16_t *offset = (uint16_t *) assocData;

  memcpy(offset, dstAddrBytes, dstAddrSize);
  offset += dstAddrSize;

  memcpy(offset, srcAddrBytes, srcAddrSize);
  offset += srcAddrSize;

  return assocData;
}

void* createNonce(uint8_t *seqNum, uint8_t *keyId, uint32_t *frameCounter) {
  void *nonce = calloc(1, ASCON_AEAD_NONCE_LEN);
  uint8_t *offset = (uint8_t *) nonce;

  memcpy(offset, seqNum, sizeof(uint8_t));
  offset += sizeof(uint8_t);

  // This is called the KEY INDEX in Wireshark.
  memcpy(offset, keyId, sizeof(uint8_t));
  offset += sizeof(uint8_t);

  memcpy(offset, frameCounter, sizeof(uint32_t));
  return nonce;
}

int main(void) {
  /**
   * The current cipher suite is LibAscon-128, for MAC layer encryption.
  */
  uint8_t key[] = {0x53, 0x08, 0x9a, 0x00, 0x90, 0x04, 0x52, 0xca,
                   0xad, 0xc9, 0x65, 0xdd, 0x85, 0xa8, 0x81, 0x1c};

  uint8_t destination[] = { 0xff, 0xff };
  uint8_t source[] = { 0x10, 0x68 };
  void *assocData = createAssocData(destination, source,
                                    sizeof(destination), sizeof(source));

  uint32_t frameCounter[] = { 0xb3, 0x00, 0x00, 0x00 };
  uint8_t keyId[] = { 0xff };
  uint8_t seqNum[] = { 0x1e };
  void *nonce = createNonce(seqNum, keyId, frameCounter);

  uint8_t tag[] = { 0xfd, 0x65, 0x95, 0xc2 };

  uint8_t payload[] = {
    0x13, 0xc3, 0x65, 0x43, 0xbe, 0xcf, 0x27, 0xa3,
    0xa0, 0x2b, 0xb3, 0x6e, 0xa6, 0x5b, 0x0d, 0x3a,
    0x8b, 0xd5, 0x26, 0x40, 0xd2, 0xc4, 0x3d, 0xce,
    0xd5, 0x1c, 0xb5, 0xbd, 0xcc, 0x9e, 0x6a, 0x6d,
    0xf9, 0xb5, 0x28, 0xfc, 0x73, 0x08, 0x23, 0xdc,
    0xe4, 0xf8, 0xab, 0xa4, 0x7a
  };

  bool status = ascon_aead128_decrypt(payload, key, nonce, assocData, payload,
                                      tag, CRYPTO_ABYTES, sizeof(payload),
                                      sizeof(tag));
  if (status == ASCON_TAG_OK) {
    printf("ASCON decryption success!");
  }
  else {
    printf("ASCON decryption failure.");
  }

  free(assocData);
  free(nonce);
  return 0;
}
