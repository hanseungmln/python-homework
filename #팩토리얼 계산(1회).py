n = int(input("정수를 입력하세요: "))

if n <= 0:
        print("음수는 팩토리얼을 계산할 수 없습니다")
else: 
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"{n}! = {fact}이다")
