from __future__ import annotations
from typing import cast

def function(a: str) -> int | None:
    try:
        return int(a)
    except ValueError:
        return None
    

def main() -> None:
    a: int | None = function("a128")
    b: int = 5

    c: int = cast(int, a)
    print(c + b)

if __name__ == "__main__":
    main()