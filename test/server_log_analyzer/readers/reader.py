from typing import Protocol

class Reader(Protocol):
    def read_lines(self) -> list[str]:
        ...