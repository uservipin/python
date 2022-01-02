
books = ['a','b','c','d']

books_dict = [{"name": 'a', 'writer': "testA"},{"name": 'b', 'writer': "testB"},{"name": 'c', 'writer': "testC"},{"name": 'd', 'writer': "testD"}]

detail_books_dict= {}
#print(books_dict[1])
book_id = 100

for i in range (len(books)):
    # int_value= ord(i)
    # print(int_value)
    print((type(i)))
    print(i)
    detail_books_dict.setdefault(book_id,books_dict[1])
    book_id+= 1

print(detail_books_dict)