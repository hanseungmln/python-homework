def is_valid_password(pw):
    if len(pw) < 10:
        print("입력하신 password는 10자리 미만입니다.")
        return False
    if pw.isdigit():
        print("입력하신 password는 숫자로만 이루어져 있습니다.")
        return False
    if pw.isalpha():
        print("입력하신 password는 문자로만 이루어져 있습니다.")
        return False
    return True

print("password를 설정합니다. 10자리 이상의 숫자와 문자의 조합으로 입력해 주세요.")

while True:
    user_id = input("ID 입력 : ")
    password = input("password 입력 : ")
    
    if is_valid_password(password):
        break

print(f"{user_id}의 비밀번호는 {password}입니다.")
print("로그온을 위해 ID와 password를 입력하세요.")

login_id = input("ID 입력 : ")
login_pw = input("password 입력 : ")

if login_id == user_id and login_pw == password:
    print("로그온 되셨습니다.")
else:
    print("ID 또는 password가 잘못되었습니다.")
    
