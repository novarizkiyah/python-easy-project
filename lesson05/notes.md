# Lesson 5 — Lists and tuples

**Date:** 2026-11-12 · **Status:** ⬜ Ready to start — Q1–Q4 pending

## Concepts to learn

- A **list** holds many values in one variable, in order: `scores = [90, 85, 77]`
- **Indexing starts at 0**: `scores[0]` is the first item, `scores[1]` the second; `scores[-1]` is the last
- A 3-item list has valid indices `0, 1, 2` (and `-1, -2, -3`) — asking for `scores[3]` raises `IndexError`
- `len(scores)` → number of items
- **Slicing** `scores[1:3]` → items at index 1 and 2; the stop index is **excluded** (same rule as `range` and strings); a slice returns a **new** list
- Lists are **mutable**: `scores[0] = 95` changes the item in place
- `scores.append(100)` adds one item to the end — and returns **`None`**. Writing `scores = scores.append(100)` silently replaces the list with `None` (classic bug)
- Loop over values with `for score in scores:`
- Loop over positions with `for i in range(len(scores)):`
- `x in scores` checks membership and gives `True`/`False`
- A **tuple** is like a list but **immutable**: `point = (3, 5)`; `point[0] = 10` raises `TypeError`
- Tuples support **unpacking**: `x, y = point`
- Use a list when the collection will change; use a tuple for fixed data (coordinates, RGB, dates)

Type and run the examples — predict each output before running:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])          # apple
print(fruits[-1])         # cherry
print(len(fruits))        # 3
print(fruits[1:3])        # ['banana', 'cherry'] — stop index 3 excluded

fruits[1] = "mango"       # lists can change
fruits.append("kiwi")
print(fruits)             # ['apple', 'mango', 'cherry', 'kiwi']

for fruit in fruits:
    print(fruit)          # one fruit per line

for i in range(len(fruits)):
    print(i, fruits[i])   # 0 apple / 1 mango / 2 cherry / 3 kiwi

point = (3, 5)
x, y = point
print(x, y)               # 3 5
print(x + y)              # 8
# point[0] = 10           # TypeError: 'tuple' object does not support item assignment
```

## Quiz tasks

- [ ] **Q1 — `q1_list_basics.py`**: indexing, negative indexing, `len`, slicing
  - Create `numbers = [4, 8, 15, 16, 23, 42]`
  - Print exactly these five lines, in this order:
    ```
    First: 4
    Last: 42
    Length: 6
    Middle: [8, 15, 16]
    All: [4, 8, 15, 16, 23, 42]
    ```
  - Use `numbers[0]` for First, **negative indexing** for Last, `len()` for Length, a slice for Middle, and print the list itself for All
  - Predict every line before running

- [ ] **Q2 — `q2_grades.py`**: loop over a list + accumulator
  - Start with `scores = [88, 42, 95, 67, 73]`
  - Loop over the list: for each score print `{score}: pass` if it is `>= 60`, otherwise `{score}: fail`
  - After the loop, print the average of all scores (add them up in a loop, divide by `len(scores)`)
  - Expected output:
    ```
    88: pass
    42: fail
    95: pass
    67: pass
    73: pass
    Average: 73.0
    ```
  - One loop, not five separate `if`s. The average line is unindented (after the loop)

- [ ] **Q3 — `q3_shopping.py`**: list + `append` + sentinel loop (Lesson 4 pattern)
  - Start with `shopping = []`
  - Keep asking `Item? ` and `append` each answer; stop when the user types `done`
  - `done` is the sentinel: it ends the loop and is **not** added
  - After the loop print exactly:
    ```
    Items: ['milk', 'eggs']
    Count: 2
    ```
  - Tests: `milk, eggs, done` → `Items: ['milk', 'eggs']` and `Count: 2`; typing `done` immediately → `Items: []` and `Count: 0`
  - Think: list before the loop, what repeats inside, which prints run after

- [ ] **Q4 — `q4_bugfix.py`**: four bugs to find by running
  ```python
  scores = [90, 85, 70]
  print(scores[3])
  for i in range(len(scores))
      print(scores[i])
  scores = scores.append(100)
  print(scores)
  top = (100, 95)
  top[0] = 99
  ```
  - Target output:
    ```
    70
    90
    85
    70
    [90, 85, 70, 100]
    (100, 95)
    ```
  - Two bugs stop the program at the start or on its first lines; one stops it later; one produces wrong output with **no error at all** — the last line should print the tuple, not change it
  - Fix one error, run again, repeat — each run reveals the next problem

## Tutor comments

_To be filled in after each quiz submission._

## How to submit

Send each file as it's finished, with the terminal output. I'll review and update this note with the results.
