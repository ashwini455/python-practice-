for i in range(1, 11):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(5, 0, -1):
    print(i)

for i in range(5):
    print("Hello")

for i in range(5):
    print("Python")

for i in range(2, 21, 2):
    print(i)

for i in range(1, 21, 2):
    print(i)


for i in range(5, 51, 5):
    print(i)


for i in range(10, 21):
    print(i)

for i in range(1, 6):
    print(i * i)





total = 0

for i in range(1, 11):
    total = total + i

print(total)



total = 0

for i in range(2, 11, 2):
    total = total + i

print(total)


total = 0

for i in range(1, 11, 2):
    total = total + i

print(total)


for i in range(1, 11):
    print(2 * i)



n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


for i in range(1, 6):
    print(i * i * i)

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)


n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)



for i in range(1, 31):
    if i % 3 == 0:
        print(i)


for i in range(1, 51):
    if i % 5 == 0:
        print(i)


n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)


n = int(input("Enter a number: "))

for i in range(10):
    print(n)


count = 0

for i in range(1, 51):
    if i % 2 == 0:
        count += 1

print(count)


n = int(input("Enter a number: "))
total = 0

for digit in str(n):
    total += int(digit)

print(total)



n = input("Enter a number: ")

for digit in n:
    print(digit)


n = input("Enter a number: ")
count = 0

for digit in n:
    count += 1

print(count)



for i in range(10, 0, -1):
    print(i)


total = 0

for i in range(1, 6):
    total += i * i

print(total)



for i in range(1, 6):
    print(2 ** i)


s = "Python"

for ch in s:
    print(ch)


s = "Python"
count = 0

for ch in s:
    count += 1

print(count)


s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print(count)



s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1

print(count)



s = "python"

for ch in s:
    print(ch.upper())


s = "ABC"

for ch in s:
    print(ord(ch))


for i in range(5):
    print("*")


for i in range(5):
    print("* " * 5)


for i in range(5):
    print("1 2 3 4 5")


for i in range(1, 21):
    if i % 4 == 0:
        print(i)



for ch in range(65, 91):
    print(chr(ch))




for i in range(1, 6):
    print(i, i * 2)




for i in range(1, 11):
    print(7 * i)



for i in range(3):
    print("Hi")


for i in range(5, 11):
    print(i)



for i in range(1, 6):
    print(i * 10)



for i in range(2, 9, 2):
    print(i)


for i in range(1, 6):
    print(4 * i)


for i in range(1, 6):
    print(i ** 3)

for i in range(8, 3, -1):
    print(i)



for ch in "Code":
    print(ch)



for i in range(10, 51, 10):
    print(i)                                                        





