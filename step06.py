import random
import time


# 🟡 Step 6 : Dictionary


# 이것은 리스트(배열)가 아니기 때문에 대괄호 대신 중괄호를 사용합니다.
information = {'고향' : '노량진', '취미' : '코딩', '좋아하는 음식' : '칼국수'} # 🔥이것을 dictionary라고 합니다

# 각각이 표시하는 것을 key라고 하고, 그에 해당하는 값은 value라고 합니다. 🔥key : value 형태입니다.

print(information)  # 출력이 아주 잘 되고 있습니다.
print(information['고향'])  # 이렇게 하면 '노량진'이 출력이 됩니다.
print(information.get('취미'))  # 🔥이렇게 get을 사용할 수도 있습니다.

information = {'특기' : '마술', '사는곳' : '춘천'}
print(information.get('특기'))
print(information.get('사는곳'))

