contacts={}
while True:
    name=input("이름을 입력:")
    if name=='serch':
        break
    tel=input("전화번호를 입력:")
    contacts[name]=tel
while True:
    name=input("검색할 이름을 입력:")
    if name in contacts:
            print(name,"의 전화번호는", contacts[name],"입니다.")
    else:
            print("해당하는 사람이 없습니다.")
            break
