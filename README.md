# hermes-sandbox

## Today's Work (2026-09-08)

### Calculator Fix (`hermes/fix-calculator` branch, later merged to `main`)
- **Bug**: `add(a, b)` in `src/calculator.py` was performing subtraction (`a - b`) instead of addition (`a + b`)
- **Fix**: Changed `return a - b` to `return a + b` at line 2
- **Tests**: All 3 tests pass (add, multiply, average)

### New Feature: "Hermes First Calculator"
- Added a playful pastel-themed calculator UI as `hermes's first calculator/` folder on `main`
- **index.html** — Display + 4x4 button grid with `data-number`, `data-operator`, `data-decimal` attributes
- **style.css** — CSS variables (`--bg`, `--button-operator`, etc.), hover/press animations, responsive grid
- **script.js** — Full calculator logic: `appendNumber`, `handleOperator`, `calculate`, `clear`, `backspace`, decimal handling, `formatNumber()` with locale commas, error state for divide-by-zero

### Git Activity
- Created branch `hermes/fix-calculator` → fixed add bug → committed → pushed
- Created branch `hermes-first-calculator` → built calculator UI → merged to `main`
- Pushed 2 commits to `main` today (2026-09-08)

---

## Hermes Training Tests

Five progressive challenges for training Hermes. Each has its own folder with a `README.md` brief and starter code.

| Folder | Challenge | Difficulty |
|--------|-----------|------------|
| `test-01-bug-fix/` | Fix 2 bugs in `string_utils.py` | ⭐ Beginner |
| `test-02-missing-feature/` | Implement 3 missing methods on `TodoList` | ⭐⭐ Easy |
| `test-03-refactor/` | Refactor messy `stats.py` + write 5 pytest tests | ⭐⭐⭐ Medium |
| `test-04-debug-and-extend/` | Fix 3 bugs in an API + add `/search` endpoint | ⭐⭐⭐⭐ Hard |
| `test-05-full-feature/` | Build a markdown notes CLI from scratch | ⭐⭐⭐⭐⭐ Expert |