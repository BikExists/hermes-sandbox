# Test 03 — Refactor ⭐⭐⭐

## Your Mission

`src/stats.py` is a working but **terrible** script. It produces correct output but the code is a mess: no functions, magic numbers, duplicate logic, and global mutable state.

Your job:
1. **Refactor** the code into clean, well-named functions
2. **Write 5 unit tests** using `pytest` that verify the output matches the original

---

## The File

`src/stats.py` — calculates statistics (mean, median, mode, variance, standard deviation) for a hardcoded dataset.

---

## Refactoring Requirements

Your refactored version must:

- [ ] Define a separate function for each statistic: `mean()`, `median()`, `mode()`, `variance()`, `std_dev()`
- [ ] Each function accepts a **list of numbers** as its only argument
- [ ] No global variables
- [ ] No magic numbers (e.g., hardcoded `100` for dataset size)
- [ ] A `main()` function that prints all results, called via `if __name__ == "__main__"`
- [ ] Match the **exact same printed output** as the original script

---

## Test Requirements

Create `src/test_stats.py` with **at least 5 pytest tests**, for example:

```python
def test_mean_basic():
    assert mean([1, 2, 3, 4, 5]) == 3.0

def test_median_odd():
    ...

def test_mode_returns_most_common():
    ...

def test_variance_known_value():
    ...

def test_std_dev_known_value():
    ...
```

---

## Pass Criteria ✅

- `python src/stats.py` produces **identical output** to the original script
- `pytest src/test_stats.py` — all 5+ tests **pass**
- No global variables in the refactored file
- Each statistic is computed in its own function

---

## Fail Criteria ❌

- Output of `stats.py` changes after refactor
- Fewer than 5 tests
- Any test fails
- Functions still rely on global state

---

## Rules

1. Refactor `src/stats.py` in place (don't rename it)
2. Create `src/test_stats.py` as the test file
3. Only stdlib + `pytest` allowed
4. Commit with message: `refactor: clean up stats.py + add pytest tests`
