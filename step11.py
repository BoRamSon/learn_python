import random

# 🟩 Step 11 : 만약에

foods = random.choice(["pasta", "pizza", "salad", "sandwich", "soup"])

if foods == "pizza":   # 강의에서는 괄호가 들어가던데... 왜 들어가는거지??
    print('곱배기 주세요!!!!!!')
else:
    print('그냥 주세요')
print('종료')


# [참고] if 조건문에 괄호를 넣을 때에는 이럴 때 사용해주는 것이 좋을 것 같습니다.
# if (foods == "pizza" or foods == "spaghetti") and size == "large":
#     print('곱배기 주세요!!!!!!')


