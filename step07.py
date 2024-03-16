import random
import time


# 🟡 Step 7 : List와 Dictionary
# 🔥 파이썬 코드는 순차적인 실행을 한다.



information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"} # 이것을 dictionary라고 합니다.
foods = ["된장찌개", "피자", "제육볶음"] # 이것을 list라고 합니다.




# ◼︎ Dictionary에 데이터 가져오기 & 추가 & 삭제하기
print(information.get("취미"))

information["특기"] = "피아노"  # 이렇게 하면 dictionary에 '특기 = 피아노'가 추가가 됩니다.
information["사는곳"] = "서울"  # 이렇게 하면 dictionaey에 '사는곳 = 서울'이 추가가 됩니다.
               # 🆘 이거 뭐지... 이거 어렵네.. 왜 추가를 이따구로 하지.. information.add 로 하면 되잖아!!!!
del information["좋아하는 음식"] # 이렇게 하면 dictionary에 '좋아하는 음식'이 삭제가 됩니다. (이건 del이라는 명령어로 뚜렸함)
print(information)

print(len(information)) # length 길이를 뜻하며, dictionary에 있는 것의 개수가 출력이 됩니다.
information.clear() # 이렇게 하면 dictionary에 있는 모든 것이 삭제가 됩니다.
print(information)





# ◼ List(배열)에 데이터 가져오기 & 추가 & 삭제하기
print(foods[1])  # 평범한 배열 데이터 가져오기 (당연히 2번째 값을 가져온다.)
foods.append('김밥')  # 이렇게 하면 배열에 '김밥'이 맨 뒷쪽에 추가가 됩니다.
del foods[1]  # 이렇게 하면 배열에 있는 1번째 값이 삭제가 됩니다.
print(foods) 
