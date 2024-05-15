 # UTF-8 Validation 
 
This Python module provides functionality to validate whether a given list of integers represents a valid UTF-8 encoding. Here's a detailed breakdown of how the module works:

## Functions
`validUTF8(data)`

This function determines if a given list of integers represents a valid UTF-8 encoding.
**Arguments:**

    data (list of int): A list of integers where each integer represents a byte (values ranging from 0 to 255).

**Returns:**

    bool: Returns True if the data is a valid UTF-8 encoding, False otherwise.

**How it works:**

1. Initializes next_span to track the number of continuation bytes expected. 
2. Iterates through each byte in the input data.
3. For each byte:
   - If next_span is 0, it means the byte should be a starting byte. It calls get_span to determine how many continuation bytes are expected.
   - If next_span is not 0, it means the byte should be a continuation byte. It calls check_continuity to verify if the byte is a valid continuation byte.
4. If any byte fails the checks, the function returns False.
5. After processing all bytes, the function returns True if all expected continuation bytes were found (next_span is 0), otherwise, it returns False.

`get_span(byte)`

This helper function determines the number of bytes in a UTF-8 encoded character based on the first byte.

**Arguments:**

    byte (int): The first byte of a UTF-8 character.

**Returns:**

    int: The number of remaining bytes in the UTF-8 character (0, 1, 2, or 3), or -1 if the byte is not a valid starting byte.

**How it works:**

Checks the value of the byte:
  * If the byte is less than 128, it returns 0 (indicating a single-byte character).
  * If the byte is between 128 and 191, it returns -1 (indicating an invalid starting byte).
  * If the byte is between 192 and 223, it returns 1 (indicating a two-byte character).
  * If the byte is between 224 and 239, it returns 2 (indicating a three-byte character).
  * If the byte is between 240 and 247, it returns 3 (indicating a four-byte character).
  * If the byte is greater than 247, it returns -1 (indicating an invalid starting byte).

`check_continuity(byte)`

This helper function checks if a byte is a valid continuation byte in UTF-8 encoding.
**Arguments:**

    byte (int): The byte to check.

**Returns:**

    bool: Returns True if the byte is a valid continuation byte (in the range 128 to 191), False otherwise.

**How it works:**

Checks if the byte value is between 128 and 191 inclusive. If it is, the byte is a valid continuation byte and the function returns True. Otherwise, the function returns False.