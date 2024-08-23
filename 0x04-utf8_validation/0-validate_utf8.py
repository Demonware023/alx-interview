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

    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Get the 8 least significant bits of the integer
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 1):
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 2):
                num_bytes = 3
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0
