#!/usr/bin/python3
# Write a method that determines if a given data set represents a valid UTF-8 encoding.
# Prototype: def validUTF8(data)
# Return: True if data is a valid UTF-8 encoding, else return False
# A character in UTF-8 can be 1 to 4 bytes long
# The data set can contain multiple characters
# The data will be represented by a list of integers
# Each integer represents 1 byte of data, therefore you only need to
# handle the 8 least significant bits of each integer

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count how many 1s are at the start of the byte
            while mask & num:
                num_bytes += 1
                mask >>= 1

            # 1 byte characters
            if num_bytes == 0:
                continue

            # If the number of bytes is more than 4 or less than 2, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If this byte doesn't start with '10', it's invalid
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    # All characters should be fully processed, so num_bytes should be 0
    return num_bytes == 0
