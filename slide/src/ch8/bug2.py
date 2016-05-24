import pdb
books = ['Python', 'XML', 'Information Retrieval']
for book in books:
    print(book)

pdb.set_trace()
if book.price > 50:
    print('High price.')
