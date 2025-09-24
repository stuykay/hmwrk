inp = input('Введите фрукты через запятую: ')
l = inp.split(',')
for i in range(len(l)):
	a = l[i].replace(' ', '')
	a.lower()
	a = a[0].upper() + a[1:]
	l[i] = a

s = set(l)
s = list(s)
s.sort(key= lambda x: x[0])
print(s)

maxcnt = 0
maxf = ''
tup = []
unique = []
for fruit in s:
	cnt = l.count(fruit)
	tup.append((fruit, cnt))
	if cnt > maxcnt:
		maxcnt = cnt
		maxf = fruit
	if cnt == 1:
		unique.append(fruit)
d = dict(tup)
unique = tuple(unique)
print(d)
print(maxf)

if ('Banana' or 'Mango' or 'Pineapple') in s: print('Есть бананчики или манго или пинапле')
else: print('No бананчики')

n = int(input('Введите N: '))
if n >= len(s):
	print(s)
else:
	print(s[:n])