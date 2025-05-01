# 복리계산 프로그램
principal = float(input("초기 원금을 입력하세요: "))        # 예: 100000
rate = float(input("연 이자율을 입력하세요 (예: 5% → 0.05): "))  # 예: 0.05
years = float(input("투자 기간(년)을 입력하세요: "))        # 예: 3

# 복리 계산
final_amount = principal * (1 + rate) ** years

# 결과 출력
print(f"{years}년 후 받을 금액은 {final_amount:.2f}원입니다.") 

