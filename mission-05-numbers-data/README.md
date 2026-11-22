# Mission 5 — Numbers and Data

## 1. Task / Objective

Convert between decimal, binary and hexadecimal numbers by hand, verify results with Python, build a number converter program, and explain how text is stored using encoding standards.

## 2. Work Completed

- Converted numbers manually between decimal, binary and hexadecimal with working shown.
- Verified all manual results using Python's built-in functions in the interactive shell.
- Built `number_converter.py` that takes a decimal input and outputs binary and hexadecimal.
- Tested the converter with three different numbers.
- Explained ASCII, UTF-8 and why encoding standards are needed.

## 3. Commands / Tools Used

| Command / Function | Purpose |
|-------------------|---------|
| `python3` | Open the Python interactive shell for verification |
| `bin()` | Python built-in that converts a decimal integer to its binary string representation (prefixed with `0b`) |
| `hex()` | Python built-in that converts a decimal integer to its hexadecimal string representation (prefixed with `0x`) |
| `int("1010", 2)` | Converts a binary string to a decimal integer (second argument specifies base 2) |
| `int("1F", 16)` | Converts a hexadecimal string to a decimal integer (second argument specifies base 16) |
| `input()` | Python built-in that reads user input from the keyboard |
| `python3 number_converter.py` | Run the converter program from Terminal |

## 4. My Understanding

### Task 5.1 — Convert Numbers by Hand

| Question | Working and Answer |
|----------|-------------------|
| Convert decimal 13 to binary | 13 ÷ 2 = 6 remainder **1** → 6 ÷ 2 = 3 remainder **0** → 3 ÷ 2 = 1 remainder **1** → 1 ÷ 2 = 0 remainder **1** → Read remainders bottom to top: **1101** |
| Convert decimal 25 to binary | 25 ÷ 2 = 12 r **1** → 12 ÷ 2 = 6 r **0** → 6 ÷ 2 = 3 r **0** → 3 ÷ 2 = 1 r **1** → 1 ÷ 2 = 0 r **1** → Read bottom to top: **11001** |
| Convert binary 1010 to decimal | (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1) = 8 + 0 + 2 + 0 = **10** |
| Convert binary 1101 to decimal | (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1) = 8 + 4 + 0 + 1 = **13** |
| Convert hexadecimal A to decimal | A = **10** (in hex, A represents 10) |
| Convert hexadecimal 1F to decimal | (1 × 16) + (F × 1) = 16 + 15 = **31** |
| Convert binary 1111 to hexadecimal | 1111 in decimal = (1×8) + (1×4) + (1×2) + (1×1) = 15. In hex, 15 = **F** |

### Task 5.2 — Verify Using Python

I opened the Python interactive shell and checked each conversion:

```
>>> bin(13)
'0b1101'        ✓ matches my manual answer

>>> bin(25)
'0b11001'       ✓ matches

>>> int('1010', 2)
10              ✓ matches

>>> int('1101', 2)
13              ✓ matches

>>> int('A', 16)
10              ✓ matches

>>> int('1F', 16)
31              ✓ matches

>>> hex(15)
'0xf'           ✓ binary 1111 = decimal 15 = hex F, matches
```

All my manual calculations matched the Python results.

### Task 5.3 — Number Converter Program

I created `number_converter.py` with the following logic:
1. Ask the user to enter a positive decimal number using `input()`.
2. Convert the input to an integer using `int()`.
3. Convert to binary using `bin()` and to hexadecimal using `hex()`.
4. Display all three representations.

**Test results:**

| Test Number | Binary Output | Hexadecimal Output |
|------------|--------------|-------------------|
| 10 | 0b1010 | 0xa |
| 255 | 0b11111111 | 0xff |
| 42 | 0b101010 | 0x2a |

The `bin()` function takes a decimal integer and returns a string starting with `0b` followed by the binary digits. The `hex()` function does the same but returns a string starting with `0x` followed by the hexadecimal digits. The `0b` and `0x` prefixes tell you which base the number is in.

### Task 5.4 — How Is Text Stored?

- The ASCII decimal code for uppercase **A** is **65**.
- The ASCII decimal code for lowercase **a** is **97**.

**Why does a computer need an encoding standard?**
Computers only understand numbers (specifically binary — zeros and ones). When I type the letter "A", the computer needs a rule that says "A = 65" so it can store the number 65 in memory and later display it back as "A" on screen. Without an agreed encoding standard, different computers might store the same letter as different numbers, and text files would become unreadable on other systems.

**A character not part of basic ASCII:**
The emoji 😊 is not part of basic ASCII. ASCII only covers 128 characters (English letters, digits and some symbols). Characters like emojis, Chinese characters, or the rupee symbol ₹ need UTF-8, which can represent over a million different characters from every writing system in the world.

## 5. Difficulties Faced

I initially forgot to convert the `input()` result to an integer using `int()`, so my program gave an error when I tried to pass a string to `bin()`. The error message said `TypeError: 'str' object cannot be interpreted as an integer`.

## 6. How I Resolved Them

I wrapped the input in `int()` like this: `number = int(decimal_input)`. That converts the user's text input into an actual number that `bin()` and `hex()` can work with.

## 7. Evidence / Files

- `mission-05-numbers-data/README.md` — this file with all conversions, verification and explanations
- `mission-05-numbers-data/number_converter.py` — the working Python converter program

## 8. Commit Details

**Commit message:** "Build number converter and practise data representation"
Work has been pushed to GitHub and verified.
