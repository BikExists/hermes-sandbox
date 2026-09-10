# hermes-sandbox

A safe sandbox for training, testing, and experimenting with Hermes Agent.

The goal is to provide progressively harder software-development tasks that can be given to Hermes and used to evaluate how well it can understand, modify, debug, test, and extend real codebases.

> This repository is intentionally kept separate from the actual Hermes source/installation.

---

## Hermes Training Tests

Five progressive challenges for training and evaluating Hermes. Each challenge has its own folder containing a `README.md` brief and starter code.

| Folder | Challenge | Difficulty |
| ------------------------ | ---------------------------------------------- | ----------- |
| `test-01-bug-fix/` | Fix 2 bugs in `string_utils.py` | ⭐ Beginner |
| `test-02-missing-feature/` | Implement 3 missing methods on `TodoList` | ⭐⭐ Easy |
| `test-03-refactor/` | Refactor messy `stats.py` + write 5 pytest tests | ⭐⭐⭐ Medium |
| `test-04-debug-and-extend/` | Fix 3 bugs in an API + add `/search` endpoint | ⭐⭐⭐⭐ Hard |
| `test-05-full-feature/` | Build a markdown notes CLI from scratch | ⭐⭐⭐⭐⭐ Expert |

---

## Purpose

These tests are designed to progressively evaluate Hermes across different software-development abilities:

1. **Bug fixing** — Can Hermes identify and correct existing defects?
2. **Feature implementation** — Can Hermes understand incomplete code and implement missing behavior?
3. **Refactoring** — Can Hermes improve messy code without breaking functionality?
4. **Debugging + extension** — Can Hermes diagnose multiple issues while adding new functionality?
5. **Full feature development** — Can Hermes build a complete project from a specification?

The challenges become progressively more open-ended and require increasingly more independent reasoning.

---

## Current Focus

The repository is currently focused on **Hermes training and evaluation**.

Future experiments may expand the sandbox to test:

- autonomous debugging
- codebase investigation
- autonomous testing
- self-improvement through experience
- multi-agent software development
- GitHub development workflows

---

## Safety Boundary

This repository is a **sandbox**.

Experiments should be performed here before giving experimental agents access to real projects or the actual Hermes installation.

The intended workflow is:

```text
Hermes
   ↓
Sandbox
   ↓
Test / Evaluate
   ↓
Improve
   ↓
Repeat
