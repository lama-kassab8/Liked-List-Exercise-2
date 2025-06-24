#  Linked List Duplicate Remover

This Python project implements a simple **singly linked list** and includes two methods to **remove duplicate elements**:

- `remove_dupes()` — removes duplicates using Python’s built-in `set()` function.
- `manual_remover()` — manually removes duplicates using a loop and a temporary list.

It also includes a method to print the linked list contents in order.

---

##  Project Structure

- `Node` class: Represents a single node in the linked list, storing data and a reference to the next node.
- `LinkedList` class: Stores the `head` node and includes:
  - `remove_dupes()`: Uses `set()` to remove duplicates, then rebuilds the list.
  - `manual_remover()`: Manually removes duplicates and rebuilds the list.
  - `print()`: Prints all elements of the linked list.

