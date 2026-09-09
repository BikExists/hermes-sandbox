# Test 04 — Debug & Extend ⭐⭐⭐⭐

## Your Mission

`src/` contains a small REST API (no framework required — it's pure Python with a simple request/response simulation). It has **3 deliberate bugs**. After fixing them, you must also **add a new `/search` endpoint**.

---

## Files

- `src/api.py` — core API dispatcher (routes requests to handlers)
- `src/routes.py` — endpoint handler functions

---

## Part 1 — Fix the 3 Bugs

Find and fix all three bugs. They are:

1. **Wrong HTTP method check** — one endpoint accepts `GET` but should accept `POST`
2. **Missing return value** — one handler processes data but never returns a response dict
3. **Off-by-one in pagination** — the `/items` endpoint's `page` parameter skips the first item on page 1

You must identify each bug, fix it, and add a comment `# BUG FIX: <description>` on the corrected line.

---

## Part 2 — Add the `/search` Endpoint

Add a `GET /search?q=<keyword>` endpoint that:

- Searches the `ITEMS` list (defined in `routes.py`) for items whose `name` contains the keyword (case-insensitive)
- Returns `{"results": [...matching items...], "count": <int>}`
- Returns `{"results": [], "count": 0}` if nothing matches
- Returns `{"error": "missing query parameter: q"}` with status `400` if `q` is not provided

---

## Pass Criteria ✅

```python
# Bug fixes verified
response = api.handle({"method": "POST", "path": "/items/create", "body": {"name": "apple"}})
assert response["status"] == 201

response = api.handle({"method": "GET", "path": "/items/stats"})
assert "total" in response["body"]          # was missing return

response = api.handle({"method": "GET", "path": "/items", "query": {"page": "1"}})
assert response["body"]["items"][0]["id"] == 1   # was skipping id=1

# New /search endpoint
response = api.handle({"method": "GET", "path": "/search", "query": {"q": "app"}})
assert response["body"]["count"] == 2       # "apple" and "app-config" match
assert response["status"] == 200

response = api.handle({"method": "GET", "path": "/search", "query": {}})
assert response["status"] == 400
```

---

## Fail Criteria ❌

- Any of the 3 bugs remains unfixed
- `/search` endpoint missing or returns wrong structure
- Bug fix comments (`# BUG FIX:`) not present
- No commit after completion

---

## Rules

1. Edit only `src/api.py` and `src/routes.py`
2. No external dependencies — pure Python only
3. Commit with: `fix: resolve 3 bugs + add /search endpoint`
