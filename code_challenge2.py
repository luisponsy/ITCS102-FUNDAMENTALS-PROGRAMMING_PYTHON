amount = int(input("Enter amount to deposit: "))

print("Here is a breakdown using PH denomination:")

print("PHP 1000:", amount // 1000)
amount = amount % 1000

print("PHP 500:", amount // 500)
amount = amount % 500

print("PHP 200:", amount // 200)
amount = amount % 200

print("PHP 100:", amount // 100)
amount = amount % 100

print("PHP 50:", amount // 50)
amount = amount % 50

print("PHP 20:", amount // 20)
amount = amount % 20

print("PHP 10:", amount // 10)
amount = amount % 10

print("PHP 5:", amount // 5)
amount = amount % 5


print("PHP 1:", amount // 1)
