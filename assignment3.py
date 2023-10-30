class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.book_next = None

class SharedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 1

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        print(f"Node with data '{data}' added to the shared list.")

    def print_book(self):
        current = self.head
        file_name = f"book_{str(self.counter).zfill(2)}.txt"
        with open(file_name, "w") as f:
            while current:
                f.write(current.data + "\n")
                current = current.book_next
        self.counter += 1
        print(f"Book written to {file_name}")


# Example usage
shared_list = SharedList()

# Add nodes to the shared list
lines = ["Line 1", "Line 2", "Line 3"]
for line in lines:
    shared_list.add_node(line)

# Simulate book creation with additional pointers
shared_list.head.book_next = Node("Line 1 of Book")
shared_list.head.book_next.book_next = Node("Line 2 of Book")
shared_list.head.next.book_next = Node("Line 1 of Another Book")

# Print each book
shared_list.print_book()
