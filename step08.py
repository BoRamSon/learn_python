import random
import time

# 🟡 Step 8 : 끝까지 반복하기


# ◼︎ List의 기본 for문 익히기
for x in range(30):
    print(x)
        # ● for문 이해하기
            # x에 range(30)을 0~29까지 한번넣고 끝나고, 다음꺼 한번넣고 끝나고,.. 이런식으로 30번 반복이 됩니다.


# ◼︎ List의 for문을 통해 1개씩 출력하기
foods = ["된장찌개", "피자", "제육볶음"]
# print(foods)
# print(foods[0])
# print(foods[1])
# print(foods[2]) # 이렇게 해버리면 수작업이 너무 많아진다.

for y in range(3):
    print(foods[y]) 
        # 이렇게 하면 0, 1, 2를 반복하게 되어서, foods[0], foods[1], foods[2]를 출력하게 됩니다.
        # 하지만, 나중에 추가했을 때, 딱 4번째 자리까지만 출력되기 때문에 이것은 좋은 방법이 아닙니다.





# ◼︎ List의 for문 출력 쉽게 만들기
for ff in foods:
    print(ff) # 이렇게 하면 foods에 있는 것을 하나씩 출력하게 됩니다. 원래 이렇게 하는 것이 맞습니다.





# ◼︎ Dictionary의 for문 출력
information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
    # 아시다시피 key:value 2가지가 1개처럼 구성되어 있습니다.

for x, y in information.items():
    print(x)
    print(y)
