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

    def print_book(self, book_name):
        current = self.head
        file_name = f"book_{str(self.counter).zfill(2)}.txt"
        with open(file_name, "w") as f:
            while current:
                if current.data == book_name:
                    book_current = current.book_next
                    while book_current:
                        f.write(book_current.data + "\n")
                        book_current = book_current.book_next
                    break
                current = current.next
        self.counter += 1
        print(f"Book written to {file_name}")


class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


# Example usage
shared_list = SharedList()

# Add nodes to the shared list
books = [
    "Robin Hood",
    "The Apple",
    "The Road to Oz",
    "An introductory lecture on archæology",
    "The Cornhill Magazine",
    "The doctor",
    "Die Stadt am Inn",
    "The Delinquent",
    "Old comrades",
    "Angel's Christmas and little Dot"
]

for book in books:
    shared_list.add_node(book)

# Simulating multiple reads
shared_list.head.book_next = Node("Page 1 of Robin Hood")
shared_list.head.book_next.book_next = Node("Page 2 of Robin Hood")
shared_list.head.next.book_next = Node("Page 1 of The Apple")
shared_list.head.next.next.book_next = Node("Page 1 of The Road to Oz")

# Print each book
for book in books:
    shared_list.print_book(book)
