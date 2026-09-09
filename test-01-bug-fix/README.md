# Test 01 — Bug Fix ⭐

## Your Mission

There are **2 bugs** hidden inside `src/string_utils.py`. Find them, fix them, and commit your changes.

---

## The File

`src/string_utils.py` contains three string utility functions:

- `reverse_string(s)` — should return the string reversed
- `count_vowels(s)` — should return the count of vowels (a, e, i, o, u) in the string
- `title_case(s)` — should return the string in Title Case

---

## Pass Criteria ✅

All of the following must be true:

| Test | Expected Output |
|------|----------------|
| `reverse_string("hello")` | `"olleh"` |
| `reverse_string("abcd")` | `"dcba"` |
| `count_vowels("hello world")` | `3` |
| `count_vowels("rhythm")` | `0` |
| `title_case("the quick brown fox")` | `"The Quick Brown Fox"` |

---

## Fail Criteria ❌

- Any of the above calls return a wrong value
- You modify `title_case` (it is already correct — don't touch it)
- No commit is made after the fix

---

## Rules

1. Only edit `src/string_utils.py`
2. Make **one commit** with a clear message describing what you fixed
3. Do not add any new dependencies

---

## Hints (read only if stuck)

<details>
<summary>Hint 1</summary>
Look carefully at what each function is actually returning vs. what it should return.
</details>

<details>
<summary>Hint 2</summary>
Python string slicing `[::-1]` reverses a string. The vowel set is `{'a', 'e', 'i', 'o', 'u'}`.
</details>
