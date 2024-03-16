import random
import time

# 🟩 Step 02 : [이상형이 뭐에요?] 제작하기

# ----------------------------------------------------
# 🟡 


questionList = {}

# 키 값을 저장하는 과정
while True:
    question = input("질문을  입력해주세요 : ")
    if(question == "q"):  # q를 입력하여 이 while문을 종료한다.
        break
    else:
        questionList[question] = ""
            # 이렇게 하게 되면 questionList에 key 값이 추가되고, value 값은 빈 상태로 존재하게 됩니다.



# 벨류 값을 저장하는 과정
for i in questionList:
    print(i)
    answer = input(">> 답변을 입력해주세요 : ")
    questionList[i] = answer


print(questionList)












