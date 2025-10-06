books = [
    {"id": 1, "title": "Мастер и Маргарита", "author": "Булгаков", "year": 1966},
    {"id": 2, "title": "Преступление и наказание", "author": "Достоевский", "year": 1866},
    {"id": 3, "title": "Война и мир", "author": "Толстой", "year": 1869},
    {"id": 4, "title": "Анна Каренина", "author": "Толстой", "year": 1877},
    {"id": 5, "title": "Собачье сердце", "author": "Булгаков", "year": 1925}
]

# Task 1
neededBook = input('Введите книгу, которую вы хотите найти: ')
for book in books:
    if book['title'] == neededBook: print(book['title'])

# Task 2
neededAuthor = input('Введите автора, чьи книги вы хотите найти: ')
booksAuthorWrote = []
for book in books:
    if book['author'] == neededAuthor: booksAuthorWrote.append(book['title'])
print(booksAuthorWrote)

# Task 3
years = [x['year'] for x in books]
def bubbleSort(years):
    listLen = len(years)
    for i in range(listLen):
        swapped = False
        for j in range(0, listLen - i - 1):
            if years[j] > years[j + 1]:
                years[j], years[j + 1] = years[j + 1], years[j]
                swapped = True
        if not swapped:
            break
    return years
bubbleSort(years)

# Task 4
yearsRange = input('Введите диапазон лет в формате 1ххх-1ххх: ')
def bookSearchingByYearsRange(books, yearsRange):
    yearsRange = yearsRange.split('-')
    yearsRange = [int(x) for x in yearsRange]
    sorted(yearsRange)
    for book in books:
        if yearsRange[0] < book['year']  < yearsRange[1]:
            print(book['title'])
bookSearchingByYearsRange(books, yearsRange)