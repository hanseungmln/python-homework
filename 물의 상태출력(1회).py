temp=float(input("섭씨 온도를 입력:"))
if temp<=0:
    print("물의 상태는 얼음")
elif temp>0 and temp<100:
    print("물의 상태는 액체")
else:
    print("물의 상태는 기체")