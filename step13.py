import random
import time
import math

# 🟩 Step 13 : [오늘은 뭐 드실?] 제작하기(2)


# ----------------------------------------------------
# 🟡 if문을 이용하여 무한반복 append를 q를 누르면 종료될 수 있도록 만들기

lunch = ['된장찌개', '피자', '제육볶음', '짜장면']

while True:
    print(lunch)
    item = input("음식을 추가해주세요 : ") # input 입력이 존재하기 때문에 무한반복이 멈춰있는 구간이 존재한다.

    if item == "q":
        break
    else:
        lunch.append(item)
        print("lunch에"+item+"을 추가되었습니다.")

# control + C 를 통해 무한반복을 종료할 수 있습니다.



