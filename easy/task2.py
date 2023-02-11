from typing import Callable, List


def create_handlers(callback: Callable[[int], None]) -> List[Callable[[], None]]:
    handlers = []
    for step in range(5):
        handlers.append(lambda new_step=step: callback(new_step))
    return handlers


def execute_handlers(handlers: List[Callable[[], None]]):
    for handler in handlers:
        handler()