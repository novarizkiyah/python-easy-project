# Lesson 2 — input(), Strings, f-strings

**Date:** 2026-10-30 · **Status:** ✅ Complete

## Concepts learned

- `input("prompt")` pauses and returns **a string, always**
- Convert before math: `int(...)`, `float(...)`, `str(...)`
- `ValueError` if `int()` receives non-digits (handling comes in Lesson 8)
- Strings are sequences: `word[0]`, `word[-1]`, `word[start:stop]`
- **Slicing rule:** start included, stop excluded
- `len()` counts characters
- Methods: `.strip() .upper() .lower() .title() .replace() .split()`
- Strings are immutable — methods return a new string: `name = name.strip()`
- f-strings: `f"Hello, {name}!"` — expressions live inside `{ }`
- Number formatting: `f"{total:.2f}"` → always two decimals
- **Golden rule:** inside an f-string, everything outside `{ }` is literal text — including commas

## Quiz and my work

### Q1 — `q1_greeting.py` ✅ (passed on 4th attempt)

```python
name = input("What's your name? ")
print(f"Hello, {name.title()}! Your name has {len(name)} letters. In caps: {name.upper()}")
```

**Tutor comment:** The journey: comma-style print → f-string with commas kept inside → commas removed. Final line is exactly right. This was the most important syntax correction of the lesson.

### Q2 — `q2_age.py` ✅

```python
name = input("Your name? ")
birth_year = input("Birth year? ")

birth_year1 = int(birth_year)

current_year = 2026
age = current_year - birth_year1

print(f"Hi {name.title()}, you are about {age} years old in 2026")
```

**Tutor comment:** Logic complete: input → `int()` → subtraction → f-string. Mistakes fixed along the way: filename had a space (`q2_ age.py`), `name.title` needed `()`, literal commas inside the f-string, `yeard` typo. Nits: missing final `.`, and `{current_year}` would be better than the hardcoded `2026`. `birth_year1` is an unnecessary copy — `birth_year = int(input(...))` is cleaner.

### Q3 — `q3_receipt.py` ✅

```python
price_per_item = float(input("Price per item? " ))
quantity = int(input("Quantity? "))
total = price_per_item*quantity

print(f"Total: {total:.2f}")
```

**Tutor comment:** Correct conversions, multiplication, lowercase variable, and `:.2f` formatting. Two small fixes along the way: the format spec, then the missing colon. Output for 2.5 and 3: `Total: 7.50`.

### Q4 — `q4_predict.py` ✅ Predictions 5/5

```python
fruit = "Learning"
print(fruit[0]) # A: L
print(fruit[-3:]) # B: ing
print(fruit[:4:]) # C: Lear
print(len(fruit)) # D:8
print(fruit.upper()) #E: LEARNING
```

**Tutor comment:** All five predictions correct. Earlier attempt with `"Loveyou"` had B as `ove` — the `-3:` lesson landed: negative indexes count from the end, so `-3:` is the **last three** characters. Notes: `[:4:]` is valid but the standard spelling is `[:4]`; variable is named `fruit` but the quiz used `word` (cosmetic); the extra `word[2:5]` line was not added. Run the file once to confirm predictions against real output.

## Mistakes worth remembering

1. **Commas inside an f-string print literally.** Braces are the only thing evaluated.
2. Methods need parentheses: `name.title()` — without `()` you print the method object, not the result.
3. Never put spaces in filenames — terminals require quoting, imports can break.
4. Comments `#` are for humans and run to the end of the line; used here as a prediction answer sheet.
5. Exact text again: `Hi Nova,` (no comma after Hi), final period, `Total:` colon.
