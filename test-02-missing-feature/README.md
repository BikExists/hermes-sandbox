# Test 02 — Missing Feature ⭐⭐

## Your Mission

You have a `TodoList` class in `src/todo_list.py`. The `add()` and `list_all()` methods are already implemented. Your job is to **implement 3 missing methods**.

---

## The File

`src/todo_list.py` — a `TodoList` class managing a list of tasks.

Each task is a dict: `{"id": int, "title": str, "done": bool}`

---

## Methods You Must Implement

### `mark_done(task_id: int) -> bool`
- Mark the task with the given ID as done (`done = True`)
- Return `True` if successful, `False` if the ID doesn't exist
- Raise `ValueError` if the task is **already marked done**

### `remove(task_id: int) -> bool`
- Permanently remove the task with the given ID
- Return `True` if removed, `False` if the ID doesn't exist

### `clear_done() -> int`
- Remove **all** tasks where `done == True`
- Return the **number of tasks removed**

---

## Pass Criteria ✅

```python
tl = TodoList()
tl.add("Buy milk")       # id=1
tl.add("Write tests")    # id=2
tl.add("Fix bugs")       # id=3

assert tl.mark_done(1) == True
assert tl.mark_done(99) == False        # ID doesn't exist
# tl.mark_done(1) should raise ValueError (already done)

assert tl.remove(2) == True
assert tl.remove(99) == False           # ID doesn't exist
assert len(tl.list_all()) == 2          # only id=1 and id=3 remain

tl.add("Deploy app")     # id=4
count = tl.clear_done()
assert count == 1                       # only id=1 was done
assert len(tl.list_all()) == 2          # id=3 and id=4 remain
```

---

## Fail Criteria ❌

- Any assertion above fails
- `mark_done` on an already-done task does NOT raise `ValueError`
- You modify the `add()` or `list_all()` methods
- No commit after completing the feature

---

## Rules

1. Only edit `src/todo_list.py`
2. Commit when done with a message like `feat: implement mark_done, remove, clear_done`
3. No external dependencies
