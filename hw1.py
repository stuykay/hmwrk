# Tasks
# 1. Добавить студента (имя, возраст, список оценок).
# 2. Показать всех студентов.
# 3. Найти студента по имени.
# 4. Удалить студента.
# 5. Добавить новую оценку студенту.
# 6. Вывести список студентов старше определённого возраста.
# 7. Показать всех студентов с оценкой выше определённого порога.
# 8. Экспортировать список студентов в CSV-вид (имя;возраст;оценки).
# 9. Импортировать студентов из CSV.
# 10. Выход.

# Requirements
#1. Данные хранить в словаре вида:
# students = {
#     		"Иван": {"age": 20, "grades": [5, 4, 3]},
#     		"Аня": {"age": 19, "grades": [4, 4, 5]}
# }
# 2. Использовать функции для каждого действия.
# 3. Использовать try/except (например, при вводе возраста, оценок, работе с файлами).
# 4. Добавить хотя бы один блок с try/except/else/finally (например, при сохранении данных).
# 5. Использовать while else — например, при поиске студента: если цикл поиска закончился без break, выводим «не найдено».
# 6. Для анализа данных использовать min/max/sum/len/sorted.
# 7. Для импорта/экспорта — текстовые файлы (CSV или обычный txt).
# 8. Сделать всевозможные проверки, чтобы программа не падала

from re import *
import csv

students = {}

# Task 1
def addStudent(data):
    name = input()
    age = int(input())
    grades = split(r'[., ]+', input())
    student = {'age': age, 'grades': grades}
    return data.update({name: student})

# Task 2
def showStudents(data):
    print(data)

# Task 3
def findStudent(data):
    print(data.get(input('Enter student name you want to find: '), 
                   'There no such student'))

# Task 4
def delStudent(data):
    try:
        del data[input('Enter student name you want to delete: ')]
    except:
        print('There is already no such student ._.')

# Task 5
def addMark(data):
    name = input('Enter student name you want to add marks: ')
    temp = data[name].get('grades')
    temp.append(int(input('Enter the mark you wanna add: ')))
    data[name]['grades'] = temp
    return data

# Task 6
def showGrannies(data):
    grannies = {}
    for keys, values in data.items():
        if values['age'] > int(input('Enter limit age: ')):
                grannies.update({keys: values})
    print(grannies)

# Task 7
def showJerks(data):
    jerks = {}
    gradeLimit = int(input('Enter limit grade: '))
    for keys, values in data.items():
        if sum(values['grades'])//len(values['grades']) > gradeLimit:
                print(sum(values['grades'])//len(values['grades']))
                jerks.update({keys: values})
    print(jerks)

# Здесь начинается боль...
# Task 8
def importFile(fileName, data=students):
    fileType = fileName[-3:]
    print(fileType)
    if fileType == 'csv':
         with open(fileName, newline='') as file:
            rdr = csv.reader(dialect='excel-tab')
            a = ''
            for i in rdr:
                a+=i
            if a.count(';') == 2:
                    a = a.split(';')
                    name = a[0]
                    age = int(a[1])
                    grades = a[2]
                    addStudent(students, name, age, grades)
    elif fileType == 'txt':
        with open(fileName, 'r') as file:
            for line in file:
                line = line.strip()
                if line.count(';') == 2:
                    line = line.split(';')
                    print(line)
                    name = line[0]
                    age = int(line[1])
                    grades = line[2]
                    addStudent(students, name, age, grades)
    else:
        input('Input file with right type: ')

# Task 9
def exportFile(data):
    fileName = input('Input name for your file: ')
    fileName = fileName + '.txt'
    with open(fileName, 'w') as file:
        for keys, values in data.items():
            file.write(f'{keys};{values['age']};{values['grades']} \n')

while True:
    print('1.Add student\n2.Show all students\n3.Find some student\n4.Delete some student\n5.Add mark to some student\n6.Show students older than\n7.Show students which have average marks higher than\n8.Import file \n9.Export file \n10.Exit')
    a = input('Enter action you wanna do: ')
    if a == '1': addStudent(students)
    elif a == '2': showStudents(students)
    elif a == '3': findStudent(students)
    elif a == '4': delStudent(students)
    elif a == '5': addMark(students)
    elif a == '6': showGrannies(students)
    elif a == '7': showJerks(students)
    elif a == '8': importFile(students)
    elif a == '9': exportFile(students)
    elif a == '10': break
    else: print('You havent chosen anything, try again')