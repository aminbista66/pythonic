from typing import Literal


class Stack[T]:
    def __init__(self):
        self._container: list[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()
    
    def __str__(self) -> str:
        return str(self._container)
    
class NumericStack[T: (int, float)](Stack[T]):
    def sum(self) -> T | Literal[0]:
        return sum(self._container)

if __name__ == '__main__':
    stack = Stack[int]()
    stack.push(1)
    item = stack.pop()

    str_stack = Stack[str]()
    str_stack.push("a")
    item_str = str_stack.pop()
    item_str.upper()

    num_stack = NumericStack[int]()
    num_stack.push(1)
    num_stack.push(2)
    num_stack.push(3)
    print(num_stack.sum())
