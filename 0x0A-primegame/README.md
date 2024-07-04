# Prime Game
 
This Python module implements a game involving prime numbers and two players, Maria and Ben. The module provides functions to determine if a number is prime, generate prime numbers starting from an offset, and determine the winner of the game based on given input.
 
## Functions

`is_prime(n)`: Determines if a number is prime.

`prime_nums_generator(offset)`: Generates prime numbers starting from a given offset.

`game(x, nums)`: Simulates the game between Maria and Ben based on the given numbers.

`isWinner(x, nums)`: Determines the winner of the game based on the scores of Maria and Ben.

## Usage

To use the functions, import them into your Python script and call them with the appropriate arguments. The isWinner function provides the overall result of the game.

### Example Usage

```python
from prime_numbers_game import isWinner

print(isWinner(3, [5, 2, 3]))  # Output: "Maria
print(isWinner(2, [1, 4]))     # Output: "Ben"
print(isWinner(2, [4, 5]))     # Output: None
```
