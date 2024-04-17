
class MyQueue:
    def __init__(self):
        # Two stacks for managing the queue
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        # Push item onto the inbound stack
        self.stack_in.append(item)

    def transfer_stacks(self):
        # Transfer elements from in-stack to out-stack to prepare for dequeue
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def dequeue(self):
        # Ensure there are items in the out-stack
        self.transfer_stacks()
        if self.stack_out:
            return self.stack_out.pop()

    def print_element(self):
        # Ensure there are items to print
        self.transfer_stacks()
        if self.stack_out:
            print(self.stack_out[-1])
        else:
            print("Queue is empty")



# Main execution logic
if __name__ == '__main__':
    q = int(input())
    queue = MyQueue()

    for _ in range(q):
        temp = input()  # Read the command from stdin
        if temp.startswith("1"):
            _, value = temp.split()  # Split the input to get the command and the value
            queue.enqueue(int(value))  # Enqueue the integer value into the queue
        elif temp == "2":
            queue.dequeue()  # Dequeue the element at the front of the queue
        elif temp == "3":
            queue.print_element()  # Print the element at the front of the queue
    