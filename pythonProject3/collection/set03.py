title=['영어','수학','국어','컴퓨터']
term1=[100, 99, 88, 77]

# 2학기 점수는 1학기와 거의 동일하다.
term2=term1.copy()
# 국어점수만 66점으로 됨.
term2[2]=66
# 1학기보다 성적이 떨어진 과목은?
for i in range(4):
    if term2[i]<term1[i]:
        print(title[i], end=' ')
print()
# 1,2학기 점수가 동일한 과목은?
for i in range(4):
    if term2[i]==term1[i]:
        print(title[i], end=' ')
