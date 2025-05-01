Input = int(input("입력 진수 결정(16/10/8/2):"))
num1 = int(input("첫 번째 값 입력: "), Input)
num2 = int(input("두 번째 값 입력: "), Input)
Output = int(input("출력 진수 결정(16/10/8/2):"))

res = num1 + num2

if Output == 2:
    res = bin(res)
elif Output == 8:
    res = oct(res)
elif Output == 16:
    res = hex(res)

print(f"{Output}진수=> {res}")