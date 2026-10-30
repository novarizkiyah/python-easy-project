# Lesson 3 — Decisions: if / elif / else

**Date:** 2026-10-30 · **Status:** 🔄 In progress — quiz delivered, waiting for solutions

## Concepts learned

- `if condition:` — **colon required**, body indented 4 spaces
- Comparison operators: `== != > < >= <=`; `=` assigns, `==` compares
- `else` — runs when the `if` is False; exactly one branch runs
- `elif` chains: top to bottom, **first True condition wins**
- Order of conditions matters (check specific cases before broad ones)
- Logical operators: `and`, `or`, `not`
- `input()` returns a string, so `int(input(...))` before numeric comparisons
- String comparisons are case-sensitive: `"Yes" != "yes"` (use `.lower()` to normalize)

## Quiz tasks

- [ ] **Q1 — `q1_grade.py`**: ask score, print letter grade
  - `>= 90` → `Grade: A`, `>= 80` → `B`, `>= 70` → `C`, `>= 60` → `D`, else `F`
  - Test: 95, 85, 70, 60, 42

- [ ] **Q2 — `q2_age_check.py`**: name + age → sentence
  - under 13 → child, 13–17 → teenager, 18–64 → adult, 65+ → senior
  - Test boundaries: 12, 13, 17, 18, 64, 65

- [ ] **Q3 — `q3_login.py`**: username + password
  - both `admin` / `python123` → `Access granted`
  - username not `admin` → `Unknown user`
  - admin but wrong password → `Wrong password`
  - Test all three cases; think about condition order

- [ ] **Q4 — `q4_bugfix.py`**: four bugs to find by running
  ```python
  age = input("Age? ")
  if age >= 18
      print("Adult")
  else:
  print("Minor")
  ```
  - Must end up printing `Adult` for 20 and `Minor` for 15

## Tutor comments

- Run the file after every fix. Python reports only the **first** error; new ones appear as you fix them — that's normal debugging, not failure.
- Expected error types here: `TypeError` (string vs number), `SyntaxError` (missing colon), `IndentationError` (body not indented).
- The order of `if`/`elif` conditions is part of the logic — test the cases listed above, not just one happy path.

## How to submit

Send each file as it's finished, with the terminal output. I'll review and update this note with the results.
