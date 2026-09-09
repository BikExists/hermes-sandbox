"""
Simple API dispatcher — routes a request dict to the correct handler.
A request dict looks like:
  {
    "method": "GET" | "POST" | ...,
    "path": "/items",
    "query": {"page": "1"},   # optional
    "body": {"name": "foo"},  # optional
  }

A response dict looks like:
  {"status": 200, "body": {...}}
"""

from routes import (
    handle_list_items,
    handle_create_item,
    handle_item_stats,
)

ROUTES = {
    ("GET",  "/items"):        handle_list_items,
    ("GET",  "/items/create"): handle_create_item,   # BUG 1: wrong method
    ("GET",  "/items/stats"):  handle_item_stats,
}


def handle(request: dict) -> dict:
    """Dispatch a request to the appropriate handler."""
    method = request.get("method", "GET")
    path   = request.get("path", "/")
    key    = (method, path)

    if key not in ROUTES:
        return {"status": 404, "body": {"error": f"route not found: {method} {path}"}}

    handler = ROUTES[key]
    return handler(request)
