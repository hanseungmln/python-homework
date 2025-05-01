number = int(input("0부터 255 사이의 정수를 입력하세요: "))

lst = []
for i in range(8):
  lst.append(number % 2)
  number = number // 2
  
for i in range(8):
  print(f"2의 {i}제곱 자리가 {lst[i]}")