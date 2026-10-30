# Lesson 1 — First Steps

**Date:** 2026-10-30 · **Status:** ✅ Complete

## Concepts learned

- A program runs top to bottom, one line at a time
- `print()` displays values; text needs quotes, numbers don't
- Comments with `#` (Python ignores them)
- Variables: `name = "Nova"`, reassignment
- Naming: `snake_case`, letters/digits/`_`, no leading digit, case-sensitive
- Types: `str`, `int`, `float`, `bool`; check with `type()`
- Arithmetic: `+ - * / // % **`, parentheses first
- `/` always returns a float; `//` floor division; `%` remainder
- Printing several items with commas adds spaces
- `TypeError` when mixing `str + int`

## Quiz and my work

### Q1 — `q1_hello.py` ✅

```python
print ("Hello, world")
print("My name is Nova.")
```

**Tutor comment:** Structure correct. Two details still open: the spec wanted `Hello, world!` (missing `!`), and standard style is `print(...)` with no space before the parenthesis.

### Q2 — `q2_variables.py` ✅ (passed on 3rd attempt)

```python
my_name = "Nova"
my_age = 30
wants_to_code = True

print("my_name =", my_name, type(my_name))
print("my_age=", my_age, type(my_age))
print("wants_to_code=", wants_to_code, type(wants_to_code))
```

**Tutor comment:** Got there in the end. First attempt printed only values, second combined everything into one line — the required pattern is one line per variable with label, value, and type. Tiny nit: `my_age=` should be `my_age =` for consistent spacing.

**Lesson learned:** commas in `print()` separate arguments and add spaces; `type()` is just another expression you can print.

### Q3 — `q3_math.py` ✅ Perfect, first try

```python
width = 12
height = 5

score1 = 88
score2 = 92
score3 = 79

avg = (score1+score2+score3)/3

area = width*height
perimeter = 2*(width+height)
print("Area:", area)
print("Perimeter:", perimeter)
print("Average score:", avg)
```

**Tutor comment:** Correct formulas, correct parentheses, correct reuse of variables. Output: `Area: 60`, `Perimeter: 34`, `Average score: 86.33333333333333`.

### Q4 — `q4_bugfix.py` ✅ Both bugs fixed

```python
name = "Aki"
age = 16

print("Hello,", name)
print(name, "is", age, "years old")
```

**Tutor comment:** Bug 1 — the variable was inside quotes (`"Hello, name"`); moved out correctly. Bug 2 — `str + int` TypeError; solved with commas. Alternative valid fix: `str(age)`.

## Mistakes worth remembering

1. **The output is the spec.** Exact text (commas, periods, exclamation marks) matters.
2. `print("a", "b")` → `a b` (space added, comma not printed).
3. `"Age: " + 30` → TypeError. Use a comma for now; f-strings later.
4. Variables are lowercase nouns: `age`, not `Age` or `old`.
