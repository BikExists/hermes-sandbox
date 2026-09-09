class TodoList:
    """A simple in-memory todo list manager."""

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add(self, title: str) -> dict:
        """Add a new task and return it."""
        task = {"id": self._next_id, "title": title, "done": False}
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_all(self) -> list:
        """Return all tasks."""
        return list(self._tasks)

    def mark_done(self, task_id: int) -> bool:
        """
        Mark the task with the given ID as done.

        Returns True if successful, False if task_id not found.
        Raises ValueError if the task is already done.
        """
        # TODO: implement this method
        pass

    def remove(self, task_id: int) -> bool:
        """
        Remove the task with the given ID.

        Returns True if removed, False if task_id not found.
        """
        # TODO: implement this method
        pass

    def clear_done(self) -> int:
        """
        Remove all completed tasks.

        Returns the number of tasks removed.
        """
        # TODO: implement this method
        pass
