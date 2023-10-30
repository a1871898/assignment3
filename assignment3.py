class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class BookNode:
    def __init__(self, book_name):
        self.book_name = book_name
        self.head = None

class SharedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def update_book_next(self, book_name, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            if not hasattr(current, 'book_next'):
                setattr(current, 'book_next', new_node)
            else:
                while getattr(current, 'book_next'):
                    current = getattr(current, 'book_next')
                setattr(current, 'book_next', new_node)

    def print_book(self, book_name):
        current = self.head
        while current:
            if hasattr(current, 'book_next'):
                print(current.data)
                current = getattr(current, 'book_next')
            else:
                current = current.next


# Example usage
shared_list = SharedList()
books = ['Robin Hood', 'The Apple', 'The Road to Oz']

for book in books:
    shared_list.add_node(book)

# Update book_next pointers
shared_list.update_book_next('Robin Hood', "Page 1 of Robin Hood")
shared_list.update_book_next('Robin Hood', "Page 2 of Robin Hood")
shared_list.update_book_next('The Apple', "Page 1 of The Apple")
shared_list.update_book_next('The Road to Oz', "Page 1 of The Road to Oz")

# Print a book
shared_list.print_book('Robin Hood')
