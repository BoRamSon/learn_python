import random
import time
import math

# 🟩 Step 14 : [오늘은 뭐 드실?] 제작하기(3)



# ----------------------------------------------------
# 🟡 집합을 사용하기

set_lunch = set(["된장찌개", "피자", "제육볶음", "짜장면"])
item = "짜장면"
# 위 2개를 차집합으로 계산을 해볼 것입니다.

# set_lunch - item  # ❌ 이렇게하면 집합끼리의 계산이 아니기 때문에 에러가 납니다.
                    # ❌ TypeError: unsupported operand type(s) for -: 'set' and 'str'

# item을 강제로 집합으로 만들어주면 됩니다!!!  = set([item])
print(set_lunch - set([item]))
# 결과 = {'제육볶음', '된장찌개', '피자'}


# ----------------------------------------------------
# 🟡 위와 같이 그렇다고 해서 set_lunch 값이 완전히 변한 것이 아니잖아요???
# 결과값을 다시 set_lunch에 넣어주어야 합니다!!!!!!!!!

print(set_lunch) # 바뀌지 않은 것

set_lunch = set_lunch - set([item]) # 원하는 값으로 바뀐 것
print(set_lunch)








