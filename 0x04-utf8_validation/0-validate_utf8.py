#!/usr/bin/python3
"""
Module for validating UTF-8 encoding.
"""

def validUTF8(data):
    num_bytes = 0

    for num in data:
        byte = num & 0xFF  # Only consider the least significant 8 bits

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check that the byte is of the form 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
