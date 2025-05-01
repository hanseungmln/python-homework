num=int(input("3자리 정수를 입력하시오:")) 
hundreds=num//100
tens=(num%100) // 10
ones=num%10

print("백의자리",hundreds)
print("십의자리:",tens)
print("일의자리:",ones)