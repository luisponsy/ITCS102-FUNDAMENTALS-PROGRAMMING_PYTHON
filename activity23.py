x = ['January','February','March','April','May','June','July']

x.insert(7,"August")
print(x)
x.append("September")
print(x)
x.pop(8)
print(x)
x.remove("August")
print(x)

for i in x:
    print(i)

full_name = 'Luis Ponsy Atienza Buñag'
for i in full_name[0:1]:
    print(i)
for i in full_name[::-1]:
    print(i)

x.reverse()
print(x)

y = list(full_name)
y.reverse()
print(y)