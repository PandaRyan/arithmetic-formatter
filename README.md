## Overview:

An arithmetic formatter designed to format strings of arithmetic problems into a vertical form, allowing primary students to easily solve the problem. It is also able to display the answers upon request. 

## Instructions:

1. Call upon the subroutine: 
```bash
arithmetic_formatter()
```
2. Enter the following parameters into the subroutine with the stated format:
```bash
arithmetic_arranger([string_of_arithmetic_problems],displayAnswer?)
```
Example:
```bash
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

## Limits and Restrictions:

- Limit of problems in a string: 5
- Only applicable for addition and subtraction
- Each number cannot be more than 4 digits
