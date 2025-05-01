price= float(input("제품의 가격을 입력하세요(만원):"))
if price>=100:
    dis_rate=0.85
    print("사은품을 받아가세요 ")
else:
    dis_rate=0.9
dis_price=dis_rate*price
print("할인된 상품의 가격(만원)=",dis_price)