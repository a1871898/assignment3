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


import threading
import time

# Define the shared data structure and other necessary classes

class AnalysisThread(threading.Thread):
    def __init__(self, shared_list, search_pattern, interval):
        super(AnalysisThread, self).__init__()
        self.shared_list = shared_list
        self.search_pattern = search_pattern
        self.interval = interval
        self.running = True

    def run(self):
        while self.running:
            time.sleep(self.interval)
            frequency_dict = {}
            current = self.shared_list.head
            while current:
                if self.search_pattern in current.data:
                    frequency_dict[current.data] = frequency_dict.get(current.data, 0) + 1
                current = current.next

            sorted_books = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

            if sorted_books:
                print(f"Most frequent occurrences of '{self.search_pattern}':")
                for book, count in sorted_books:
                    print(f"Book: {book}, Count: {count}")
                print("\n")


# Example usage
shared_list = SharedList()  # Assuming you have already defined the SharedList class

# Simulate the addition of nodes to the shared list
books = ["Robin Hood", "The Apple", "The Road to Oz"]
for book in books:
    shared_list.add_node(book)

# Create and start multiple analysis threads
search_pattern = "to"  # Example search pattern, you can set this from the command line
interval_seconds = 5  # Example interval, you can configure this according to your requirements

analysis_thread_1 = AnalysisThread(shared_list, search_pattern, interval_seconds)
analysis_thread_2 = AnalysisThread(shared_list, search_pattern, interval_seconds)

analysis_thread_1.start()
analysis_thread_2.start()

# Allow the threads to run for a specified duration or until a stopping condition is met

# Properly handle thread termination and clean up resources when the program ends
