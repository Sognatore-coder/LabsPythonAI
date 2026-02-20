numbers = list(map(int,input().split()))
for i in range(1,len(numbers)):
    if(numbers[i] * numbers[i - 1] > 0):
        print(numbers[i-1],numbers[i])
        break