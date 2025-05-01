hours=float(input("주당 근무시간을 입력하시오:"))
wage=float(input("시간당 임금을 입력하시오"))

if hours<=40:
    totalwages=hours*wage
else:
    overtime=hours-40
    totalwages=wage*40+(1.5*wage)*overtime
print("총임금은",totalwages,"원")