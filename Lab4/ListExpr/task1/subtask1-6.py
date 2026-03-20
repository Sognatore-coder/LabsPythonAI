#1
my_list = [1,2,3,4,5,6,7]
new_list = [x for x in my_list if x < 5]
print(new_list)

#2
my_list2 = [1,2,3,4,5]
new_list2 = [x / 2 for x in my_list2]
print(new_list2)

#3
my_list3 = [10,18,20,5,30]
new_list3 = [x * 2 for x in my_list3 if x > 17]
print(new_list3)

#4
n = int(input("Введите число: "))
squares = [x**2 for x in range(n+1)]
print(squares)

#5
numbers = list(map(int, input().split()))
square_s = [x**2 for x in numbers]
print(square_s)

#6
print(*[x**2 for x in map(int, input().split()) if x % 2 != 0 and (x**2) % 10 != 9])