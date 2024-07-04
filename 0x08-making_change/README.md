# Making Change Module

This Python module provides a function to determine the fewest number of coins needed to meet a given amount total.

## Functions

### `make_change(coins, total)`

Determines the fewest number of coins needed to meet a given amount total.

#### Parameters

- `coins` (list of int): A list of the values of the coins in your possession.
- `total` (int): The total amount to be met using the fewest number of coins.

#### Returns

- `int`: The fewest number of coins needed to meet the total.
  - Returns 0 if the total is 0 or less.
  - Returns -1 if the total cannot be met by any number of coins you have.

#### Description

The function first sorts the list of coins in descending order. It then uses a dynamic programming approach to determine the minimum number of coins needed to meet the given total. If the total cannot be met by any combination of the given coins, it returns -1.

#### Example

```python
from making_change import make_change

print(make_change([1, 2, 25], 37))  # Output: 7
print(make_change([1256, 54, 48, 16, 102], 1453))  # Output: -1
```
