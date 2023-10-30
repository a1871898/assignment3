class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.book_next = None
        self.next_frequent_search = None


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

    def print_book(self, book_name):
        current = self.head
        file_name = f"book_{str(self.counter).zfill(2)}.txt"
        with open(file_name, "w") as f:
            while current:
                if hasattr(current, 'book_next'):
                    f.write(current.data + "\n")
                    current = current.book_next
                else:
                    current = current.next
            self.counter += 1
        print(f"Book written to {file_name}")


# Example usage
shared_list = SharedList()




import argparse

# Assuming the Node and SharedList classes are defined here

# Add the following code to handle command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('-p', action='store_true', help='Allow the option to be passed to the script.')
    args = parser.parse_args()

    if args.p:
        print("Option -p is allowed.")

    # Rest of your code here
    shared_list = SharedList()

    # Add nodes to the shared list
    books = ["Robin Hood", "The Apple", "The Road to Oz"]
    for book in books:
        shared_list.add_node(book)

    # Simulating multiple reads
    shared_list.head.book_next = Node("Page 1 of Robin Hood")
    shared_list.head.book_next.book_next = Node("Page 2 of Robin Hood")
    shared_list.head.next.book_next = Node("Page 1 of The Apple")
    shared_list.head.next.next.book_next = Node("Page 1 of The Road to Oz")

    # Print each book
    shared_list.print_book("Robin Hood")
    shared_list.print_book("The Apple")
    shared_list.print_book("The Road to Oz")
