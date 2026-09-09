"""
Route handlers for the simple API.
"""

# In-memory item store
ITEMS = [
    {"id": 1, "name": "apple"},
    {"id": 2, "name": "banana"},
    {"id": 3, "name": "app-config"},
    {"id": 4, "name": "cherry"},
    {"id": 5, "name": "date"},
]

PAGE_SIZE = 2


def handle_list_items(request: dict) -> dict:
    """
    GET /items?page=<n>
    Returns a paginated slice of ITEMS.
    Pages are 1-indexed.
    """
    query = request.get("query", {})
    page = int(query.get("page", "1"))

    # BUG 2: off-by-one — should be (page - 1) * PAGE_SIZE
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    slice_ = ITEMS[start:end]

    return {
        "status": 200,
        "body": {
            "items": slice_,
            "page": page,
            "total": len(ITEMS),
        },
    }


def handle_create_item(request: dict) -> dict:
    """
    POST /items/create
    Creates a new item from request body {"name": "..."}.
    """
    body = request.get("body", {})
    name = body.get("name", "")
    if not name:
        return {"status": 400, "body": {"error": "name is required"}}

    new_id = max(item["id"] for item in ITEMS) + 1
    new_item = {"id": new_id, "name": name}
    ITEMS.append(new_item)
    return {"status": 201, "body": {"item": new_item}}


def handle_item_stats(request: dict) -> dict:
    """
    GET /items/stats
    Returns summary statistics about the items list.
    """
    total = len(ITEMS)
    names = [item["name"] for item in ITEMS]
    avg_name_len = sum(len(n) for n in names) / total if total else 0

    stats = {
        "total": total,
        "avg_name_length": round(avg_name_len, 2),
    }
    # BUG 3: missing return statement — stats are computed but never returned
