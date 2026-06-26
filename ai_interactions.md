# AI Interactions Log

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Empty input | "Generate a pytest case that tests what happens when the user submits an empty string to parse_guess" | `assert ok == False` and `assert error == "Enter a guess."` | Yes ✅ | Empty input should never be treated as a valid guess |
| Non-numeric input | "Generate a pytest case that tests what happens when the user types letters instead of a number" | `assert ok == False` and `assert error == "That is not a number."` | Yes ✅ | Letters cannot be converted to integers so should return an error |
| Negative number | "Generate a pytest case that tests whether negative numbers are handled correctly by parse_guess" | `assert ok == True` and `assert guess_int == -5` | Yes ✅ | Negative numbers are valid integers and should parse successfully |
| Decimal input | "Generate a pytest case for decimal numbers like 42.7 being entered as a guess" | `assert ok == True` and `assert guess_int == 42` | Yes ✅ | Decimals should be converted to integers by truncating the decimal part |
| None input | "Generate a pytest case that tests what happens when None is passed to parse_guess" | `assert ok == False` and `assert error == "Enter a guess."` | Yes ✅ | None input should be caught and return a friendly error message |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.


**Prompt used:**

```
**Prompt used:**

```
1. Add professional docstrings to every function in logic_utils.py 
   following PEP 257 conventions. Each docstring should include a 
   description, Args section, Returns section, and an Example section.

2. Generate pytest edge case tests for parse_guess function covering:
   empty input, non-numeric input, negative numbers, decimal input, 
   and None input.
```
```

**Linting output before:**

```
No linting errors found. Code was already following PEP 8 style 
guidelines. Main improvement was adding missing docstrings to all 
functions in logic_utils.py for professional documentation.

**Changes applied:**

**Changes applied:**

- Added a full docstring to `get_range_for_difficulty` explaining 
  the difficulty parameter and return value with an example
- Added a full docstring to `parse_guess` explaining the three-part 
  return tuple and showing both success and failure examples
- Added a full docstring to `check_guess` explaining the guess and 
  secret parameters and the possible outcome values
- Added a full docstring to `update_score` explaining how points are 
  calculated based on outcome and attempt number
- All docstrings follow PEP 257 format with Args, Returns, and 
  Example sections for professional readability

---

## Model Comparison (SF11)

> Not attempted for this submission.