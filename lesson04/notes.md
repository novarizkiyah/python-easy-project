# Lesson 4 — Loops: for and while

**Date:** 2026-11-01 · **Status:** 🟨 In progress — Q1 ✅, Q2–Q4 pending

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

- [ ] **Q2 — `q2_times_table.py`**: loop variable inside an f-string
  - Ask `Number? `, then print 10 lines: `n x i = n*i` for `i` from 1 to 10
  - Use `for` and `range(1, 11)`; keep the exact format `7 x 1 = 7`
  - Test with 7 and 3 — first and last line for 7: `7 x 1 = 7` … `7 x 10 = 70`

- [ ] **Q3 — `q3_sum_until_zero.py`**: while loop with a sentinel
  - Keep asking `Number? ` and adding each number to a total; stop when the user enters `0`
  - `0` ends the loop and is **not** added; then print `Total: X` once
  - Test: `10, 5, 2, 0` → `Total: 17`; entering `0` immediately → `Total: 0`; `5, -2, 0` → `Total: 3`
  - Think: what must happen before the loop, what goes inside, and what runs after?

- [ ] **Q4 — `q4_bugfix.py`**: four bugs to find by running
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

## How to submit

Send each file as it's finished, with the terminal output. I'll review and update this note with the results.
