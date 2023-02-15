# 60 점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무 메시지도 전하지 않는 프로그램

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)
