result = ''
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    for i in range(1, n):
        for j in range(i+1, n):
            if n % (i + j) != 0:
                continue
            else:
                result += str(i)
                result += str(j)

print(f'{n} - {result}')





