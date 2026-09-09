# Test 05 — Full Feature Build ⭐⭐⭐⭐⭐

## Your Mission

Build a **markdown note-taking CLI tool** from scratch inside the empty `src/` folder.

This test has no starter code. You design the architecture, write the code, handle the edge cases, and document it.

---

## Specification

### Commands

| Command | Description |
|---------|-------------|
| `python notes.py add "<title>" "<body>"` | Create a new note |
| `python notes.py list` | List all notes (ID + title) |
| `python notes.py view <id>` | Print a note's full content |
| `python notes.py delete <id>` | Delete a note by ID |
| `python notes.py search <keyword>` | Search note bodies for a keyword |

### Storage

- Notes are stored as **individual `.md` files** in a `notes/` subdirectory
- File naming: `<id>.md` (e.g., `1.md`, `2.md`)
- Each file contains:
  ```
  # <title>

  <body>
  ```
- IDs are **auto-incremented** and never reused (use a `meta.json` to track next ID)

### Output Format

```
# add
Note #3 created: "My Title"

# list
[1] First note
[2] Second note
[3] My Title

# view 2
ID: 2
Title: Second note
---
Body of the second note here.

# delete 2
Note #2 deleted.

# search hello
2 result(s) for "hello":
[1] First note
[4] Another note with hello in body

# search xyz
No notes found for "xyz".
```

### Error Handling

All error cases must print a user-friendly message and exit with code `1`:

| Scenario | Message |
|----------|---------|
| `view <id>` — ID not found | `Error: note #<id> not found.` |
| `delete <id>` — ID not found | `Error: note #<id> not found.` |
| Unknown command | `Error: unknown command "<cmd>". Use: add, list, view, delete, search` |
| `add` with missing arguments | `Error: usage: notes.py add "<title>" "<body>"` |

---

## Deliverables

Your `src/` folder must contain:

- [ ] `notes.py` — the main CLI entry point
- [ ] `storage.py` — handles reading/writing `.md` files and `meta.json`
- [ ] `commands.py` — one function per command (`cmd_add`, `cmd_list`, etc.)
- [ ] `notes/` — directory created automatically on first run (don't create it manually)
- [ ] `test_notes.py` — at least **3 pytest tests** (test add, test list, test search at minimum)
- [ ] `README.md` — brief usage guide (different from this file — write it yourself)

---

## Pass Criteria ✅

- All 5 commands work as specified
- All error cases exit with code 1 and print the right message
- `pytest src/test_notes.py` — all tests pass
- Notes persist between runs (stored in files)
- IDs are never reused after deletion
- Your own `src/README.md` clearly explains how to use the tool

---

## Fail Criteria ❌

- Any command crashes with an unhandled exception
- Notes are stored in memory only (not persisted to disk)
- ID reuse after deletion
- Fewer than 3 tests, or any test fails
- Missing any of the required files
- No commit after completion

---

## Rules

1. All code goes inside `src/`
2. Only Python stdlib + `pytest` allowed
3. Must work with `python src/notes.py <command>`
4. Commit with: `feat: build markdown notes CLI from scratch`

---

## Scoring Rubric

| Aspect | Points |
|--------|--------|
| All 5 commands work correctly | 40 |
| Error handling (all 4 cases) | 20 |
| File persistence + no ID reuse | 15 |
| 3+ passing pytest tests | 15 |
| Clean architecture (3 files) | 5 |
| Your own README.md | 5 |
| **Total** | **100** |
