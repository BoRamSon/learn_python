import random
import time
import math

# 🟩 Step 12 : [오늘은 뭐 드실?] 제작하기(1)

# ----------------------------------------------------
# 🟡 

# lunch = ['된장찌개', '피자', '제육볶음', '짜장면']

# 추가하기
# lunch.append('돈가스')

# print(lunch)


# ----------------------------------------------------
# 🟡 input을 사용하여 사용자에게 음식을 추가할 수 있도록 하기
lunch = ['된장찌개', '피자', '제육볶음', '짜장면']
item = input("음식을 추가해주세요 : ")
lunch.append(item)
print("lunch에"+item+"을 추가되었습니다.")
print(lunch)




# ----------------------------------------------------
# 🟡 무한반복 써주기 - 지속적인 추가루프를 돌게됩니다.

lunch = ['된장찌개', '피자', '제육볶음', '짜장면']

while True:
    item = input("음식을 추가해주세요 : ") # input 입력이 존재하기 때문에 무한반복이 멈춰있는 구간이 존재한다.
    lunch.append(item)
    print("lunch에"+item+"을 추가되었습니다.")
    print(lunch)
    # control + C 를 통해 무한반복을 종료할 수 있습니다.



