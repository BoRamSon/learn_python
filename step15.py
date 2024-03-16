import random
import time
import math

# 🟩 Step 15 : [오늘은 뭐 드실?] 제작하기(4)


# ----------------------------------------------------
# 🟡 추가해보고, 차집합으로 삭제해보고, 랜덤돌려서 랜덤으로 나오는 메뉴를 선정한다.

# 🟡 추가
lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if(item == "q"):  # q를 입력하여 이 while문을 종료한다.
        break
    else:
        lunch.append(item) # q가 아닌 메뉴를 입력 시 추가해주는 과정.
print(lunch)
    # 추가해주는 과정이 끝났다.

set_lunch = set(lunch) 
    # 지금 현재 lunch의 리스트는 음식을 추가한 상태이고, 이 상태로 집합으로 만든다.



# 🟡 삭제 (차집합)
while True:
    print(set_lunch) # 집합으로 만든 set_lunch를 출력해주고
    item = input("음식을 삭제해주세요 : ")
    if(item == "q"):  # q를 입력하여 이 while문을 종료한다.
        break
    else:
        set_lunch = set_lunch - set([item])
            # 집합으로 만든 set_lunch에서 item을 차집합으로 계산하여 삭제하는 과정.



# 🟡 추가 및 삭제 후 결과 알려주기
print(set_lunch, "중에서 선택합니다.")


# 🟡 시간초 세기
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)


# 🟡 random 나옴
print(random.choice(list(set_lunch)))
    # 1. set_lunch는 지금 집합형태인데 이것을 리스트형태로 만들어주었고,
    # 2. 그 리스트형태의 set_lunch에서 random.choice를 사용하여 하나를 선택하여 출력하였다.











