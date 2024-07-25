#!/usr/bin/python3
""" 0.valditate utf-8"""


def validUTF8(data):
    """utf-8 validation"""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for the most significant bits of each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the 8 least significant bits of the number
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine how many bytes the UTF-8 character consists of
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1-byte characters or characters with
            # more than 4 bytes are invalid
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For the remaining bytes, the pattern should be `10xxxxxx`
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes left to process
        num_bytes -= 1

    # If we finish processing all the bytes,
    # the data is valid UTF-8 if no more bytes are expected
    return num_bytes == 0
