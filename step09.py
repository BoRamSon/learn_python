import random
import time
import math

# 🟡 Step 9 : 집합 알아보기

# 집합에는 index[1], index[2] 이런 것들이 없다. 그 묶음자체가 집합이다.
# 집합은 같은 원소(같은 내용)이 같이 존재할 수 없습니다.


# 합집합 연산 - 겹치는 원소를 하나로 합쳐서 만들어줌
# 차집합 연산 - 겹치는 원소를 그냥 빼버리는 역할
# 교집합 연산 - 겹치는 원소만 출력


foods = ["된장찌개", "피자", "제육볶음"]
foods_set1 = set(foods)
foods_set2 = set(["된장찌개", "피자", "제육볶음"])
print(foods_set1)
print(foods_set2)



# 예시
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.union(s2))  # 합집합: {1, 2, 3, 4}
print(s1.intersection(s2))  # 교집합: {2, 3}
print(s1.difference(s2))  # 차집합: {1}