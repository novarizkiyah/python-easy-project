# Lesson 4 — Loops: for and while

**Date:** 2026-11-01 · **Status:** ✅ Complete — all four quizzes passed

## Concepts to learn

- `for i in range(5):` — repeats the indented body 5 times; `i` takes each value in turn
- `range(5)` → `0 1 2 3 4` — the stop value is **excluded** (same rule as string slicing)
- `range(start, stop, step)`: `range(1, 11)` → 1–10, `range(5, 0, -1)` → 5–1, `range(1, 11, 2)` → odd numbers
- `while condition:` — checks the condition before **each** pass; runs while it is True
- The loop body is indented 4 spaces; the colon after `for`/`while` is required
- **The counter must change inside the loop** — if it never does, the loop never ends. `Ctrl+C` in the terminal stops a runaway program
- Accumulator pattern: `total = 0` before the loop, `total = total + x` inside, print after
- `+=` shorthand: `total += x` is the same as `total = total + x`; `count -= 1` also works
- A **sentinel** is a special value that tells the loop to stop (Q3 uses `0`)
- `break` exits the loop immediately; `continue` skips to the next pass (used less)
- `for` when you know how many times; `while` when you loop until a condition changes
- Lines **after** the loop (not indented) run once, after the loop finishes

Type and run the examples — predict each output before running:

```python
for i in range(5):
    print(i)              # 0 1 2 3 4 — 5 is never printed

for i in range(1, 11, 2):
    print(i)              # 1 3 5 7 9

count = 3
while count > 0:
    print(count)
    count = count - 1     # without this line, the loop never ends

total = 0
for i in range(1, 4):
    total += i
print(total)              # 6 — printed once, after the loop
```

## Quiz tasks

- [x] **Q1 — `q1_countdown.py`**: for loop with a negative step ✅
  - Print `5` down to `1`, one number per line, then `Blastoff!`
  - Use `for` with `range(5, 0, -1)` — do not type five `print`s
  - Expected output:
    ```
    5
    4
    3
    2
    1
    Blastoff!
    ```

- [x] **Q2 — `q2_times_table.py`**: loop variable inside an f-string ✅
  - Ask `Number? `, then print 10 lines: `n x i = n*i` for `i` from 1 to 10
  - Use `for` and `range(1, 11)`; keep the exact format `7 x 1 = 7`
  - Test with 7 and 3 — first and last line for 7: `7 x 1 = 7` … `7 x 10 = 70`

- [x] **Q3 — `q3_sum_until_zero.py`**: while loop with a sentinel ✅
  - Keep asking `Number? ` and adding each number to a total; stop when the user enters `0`
  - `0` ends the loop and is **not** added; then print `Total: X` once
  - Test: `10, 5, 2, 0` → `Total: 17`; entering `0` immediately → `Total: 0`; `5, -2, 0` → `Total: 3`
  - Think: what must happen before the loop, what goes inside, and what runs after?

- [x] **Q4 — `q4_bugfix.py`**: four bugs to find by running ✅
  ```python
  count = 1
  total = 0
  while count < 5
  total = total + count
  count = count + 1
  print(total)
  ```
  - Target: print `15` (the sum 1+2+3+4+5)
  - Fix one error, run again, repeat — the first three bugs stop or stall the program; the fourth is a logic bug Python will not complain about
  - **If it hangs with no output, press `Ctrl+C`** — a loop that never ends is one of the bugs, not a broken keyboard

## Tutor comments

### Q1 — `q1_countdown.py` ✅

```python
for i in range(5, 0, -1):
    print (i)
print("Blastoff!")
```

**Tutor comment:** Correct on the first try — I ran it and got exactly `5 4 3 2 1 Blastoff!`. The `range(5, 0, -1)` is right: start at 5, stop before 0, step -1 counts down. And `print("Blastoff!")` is unindented, so it runs once after the loop instead of being repeated inside it — that is the detail most people get wrong on this exercise. One style nit: `print (i)` has a space between the function name and the parenthesis. Python accepts it, but it is inconsistent with `print("Blastoff!")` two lines below; PEP 8 (Python's style guide) says no space. `print(i)` is the standard form.

### Q2 — `q2_times_table.py` ✅

```python
n = int(input("Number? "))
for i in range(1, 11, 1):
    print(f"{n} x {i} = {n * i}")
```

**Tutor comment:** Correct on the first try — I ran it with 7 and 3 and both tables are right, first line `7 x 1 = 7` and last line `7 x 10 = 70`. The important structure is right: `input()` happens once before the loop (so the user is asked once, not ten times), `int()` converts the text to a number, and the f-string puts both variables plus the product (`{n * i}`) into the exact required format. One small simplification: `range(1, 11, 1)` writes the step out explicitly, but the default step is already 1, so `range(1, 11)` means the same thing — use the shorter form unless you actually need a step other than 1. Not a bug, just tidier.

### Q3 — `q3_sum_until_zero.py` ✅

```python
total = 0

number = int(input("Number? "))

while number != 0 :
    total = total + number
    number = int(input("Number? "))
print(f"Total: {total}")
```

**Tutor comment:** Correct — all three tests pass (`Total: 17`, `Total: 0`, `Total: 3`), including the two edge cases that matter: entering `0` straight away (the loop body never runs, total stays at 0) and a negative number (`5 + (-2) = 3`, added normally). The structure is the classic sentinel pattern: the first input sits before the loop so the condition has something to test, the next input is the last line of the body so every pass refreshes the value, and the print is unindented so it runs once. The same input line appearing twice is correct here — it is not duplication to remove. One style nit: `while number != 0 :` has a space before the colon; PEP 8 writes it `while number != 0:`. The earlier version hung for exactly the reason this one works: `number` never changed, so `number != 0` stayed True forever.

### Q4 — `q4_bugfix.py` ✅

```python
count = 1
total = 0

while count <= 5:
    total = total + count
    count = count + 1

print(total)
```

**Tutor comment:** All four bugs fixed — I ran it and got `15`. The four were: (1) missing colon after `while count < 5` → `SyntaxError`, so the file never ran at all; (2) `total = total + count` not indented → `IndentationError` (expected an indented block); (3) `count = count + 1` not indented, so it sat outside the loop — `count` never changed, the loop ran forever and printed nothing; (4) `count < 5` misses 5, so the sum stops at 1+2+3+4 = 10 — Python gives no warning for this one, only checking the result reveals it. Notice the three different timings: bugs 1–2 are caught before any code runs (Python parses and indent-checks the whole file first), bug 3 appears as a hang while running, and bug 4 appears only when you compare the output with the expected answer. Fixing one thing and re-running is what makes each bug visible in turn.

## How to submit

Send each file as it's finished, with the terminal output. I'll review and update this note with the results.
