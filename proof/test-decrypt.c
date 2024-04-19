/**
 * --- TO-DO ---
 * 1. A function to get the key
 * 2. A function to get the nonce
 * 3. A function to get the associated data
 * 4. Get the packet bytes.
 * 4. Then given (1)-(3), decrypt!
*/
#include <stdio.h>

#include "ascon.h"
#include "common.h"

void* createAssocData(void* dstAddrBytes, void* srcAddrBytes,
                      size_t dstAddrSize, size_t srcAddrSize)
{
  void* assocData = calloc(1, CRYPTO_ABYTES);

  uint16_t offset = (uint16_t) assocData;

  memcpy(offset, dstAddrBytes, dstAddrSize);
  offset += dstAddrSize;

  memcpy(offset, srcAddrBytes, srcAddrSize);
  offset += srcAddrSize;

  return assocData;
}

int main() {
  return 0;
}
