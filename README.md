# palindromic-numbers

Generates the smallest base (greater than or equal to 2) in which each positive decimal integers in the given range are palindromes, and saves the results in a csv file.

### Setup and Usage

_Assuming Python version is 2.7_
```
pip install mock==2.0.0
chmod +x generate_smallest_palindrome_bases.py
./generate_smallest_palindrome_bases.py 1 1000
```

_To run tests:_
```
python -m unittest test_utils
```