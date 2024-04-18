# Enter your code here. Read input from STDIN. Print output to STDOUT

class SimpleTextEditor:
    def __init__(self):
        self.s = ""  # The text editor starts with an empty string
        self.history = []  # Stack to keep track of previous states and operations

    def append(self, w):
        self.history.append((1, self.s))  # Save current state before change
        self.s += w  # Append string w to current text

    def delete(self, k):
        self.history.append((2, self.s[-k:]))  # Save the deleted string
        self.s = self.s[:-k]  # Delete last k characters

    def print_char(self, k):
        print(self.s[k-1])  # Print k-th character, 1-indexed

    def undo(self):
        if not self.history:
            return
        last_operation, state = self.history.pop()
        if last_operation == 1:
            self.s = state  # Restore previous state
        elif last_operation == 2:
            self.s += state  # Re-append the previously deleted string

# Example of handling operations
if __name__ == "__main__":
    editor = SimpleTextEditor()
    queries = int(input())
    for _ in range(queries):
        parts = input().split()
        operation_type = int(parts[0])
        if operation_type == 1:
            editor.append(parts[1])
        elif operation_type == 2:
            editor.delete(int(parts[1]))
        elif operation_type == 3:
            editor.print_char(int(parts[1]))
        elif operation_type == 4:
            editor.undo()