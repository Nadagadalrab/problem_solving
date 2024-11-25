borrowed_book = {}

num_entries = int(input("Enter the number of books you want to borrow "))

for i in range (num_entries):
    key = input("Enter the book title: ")
    value = int(input("Enter the days borrowed: "))
    borrowed_book[key] = value


days = list(borrowed_book.values())
days.sort()
highest_num = max(days)
lowest_num = min(days)
avg_num = sum(days)/ len(days)
books = list(borrowed_book.keys())
books_set = set(books)

borrowed_book_sorted = dict(sorted(borrowed_book.items(), key=lambda item: item[1], reverse=True))

print("the book with the highest borrowing days: ",
list(borrowed_book.keys())
    [list(borrowed_book.values()).index(highest_num)])
print("the book with the lowest borrowing days: ",list(borrowed_book.keys())
    [list(borrowed_book.values()).index(lowest_num)])
print("the average borrowing time: ", round(avg_num,2))
print(borrowed_book_sorted)
print("Unique titles: ", books_set)
