/**
 * --- TO-DO ---
 * 1. A function to get the key
 * 2. A function to get the nonce
 * 3. A function to get the associated data
 * 4. Get the tag.
 * 5. Get the packet bytes.
 * 4. Then given (1)-(3), decrypt!
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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

int main(void) {
  uint8_t destination[] = { 0xff, 0xff };
  uint8_t source[] = { 0x10, 0x68 };
  void *assocData = createAssocData(destination, source,
                                    sizeof(destination), sizeof(source));
  free(assocData);
  return 0;
}
