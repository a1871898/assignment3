

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
