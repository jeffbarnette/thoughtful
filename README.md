# Thoughtful Package Sorting Function

## Overview

This project provides a function, `sort`, which categorizes packages into one of three stacks based on their dimensions and mass:
- **STANDARD**: Packages that are neither bulky nor heavy.
- **SPECIAL**: Packages that are either bulky or heavy, but not both.
- **REJECTED**: Packages that are both bulky and heavy.

The accompanying test suite provides comprehensive validation of the function's behavior, including edge cases and input validation.

---

## Requirements

- Python 3.10 or higher


## How it works

The package sorting system evaluates packages based on two main criteria: bulkiness and weight. A package is considered bulky if either its volume equals or exceeds 1,000,000 cubic centimeters (equivalent to 1 cubic meter) or if any single dimension is 150 centimeters or larger. It's classified as heavy if it weighs 20 kilograms or more. Using these criteria, the system sorts packages into three categories: REJECTED (for packages that are both bulky and heavy), SPECIAL (for packages that are either bulky or heavy, but not both), and STANDARD (for packages that are neither bulky nor heavy). This ensures efficient handling and appropriate routing of packages based on their physical characteristics.

## Instructions

### **Function Usage**

The function `sort(width, height, length, mass)` is defined in `sort.py`. 

#### Parameters:
- `width` (float): Width of the package in cm (must be positive).
- `height` (float): Height of the package in cm (must be positive).
- `length` (float): Length of the package in cm (must be positive).
- `mass` (float): Mass of the package in kg (must be positive).

#### Returns:
- A string indicating the category:
  - `"STANDARD"`: Package is neither bulky nor heavy.
  - `"SPECIAL"`: Package is either bulky or heavy, but not both.
  - `"REJECTED"`: Package is both bulky and heavy.

#### Raises:
- `ValueError`: If any input measurement is negative.

---

### **Test Suite**

The test cases are implemented in `test_sort.py` using the `unittest` framework. The suite includes:
- Basic functionality tests
- Edge case handling
- Boundary value testing
- Invalid input validation
- Decimal value handling

#### Test Categories:
- Standard package classification
- Bulky package detection (volume and dimension-based)
- Heavy package classification
- Rejected package validation
- Edge cases and boundary conditions
- Invalid input handling
- Decimal value processing

#### How to Run Tests:
1. Ensure both `sort.py` and `test_sort.py` are in the same directory.
2. Run the following command in the terminal:

```
python -m unittest test_sort.py
```

---

## Error Handling

The function includes input validation to ensure all measurements are positive values. Negative inputs will raise a ValueError with an appropriate error message.
