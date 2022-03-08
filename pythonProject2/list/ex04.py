score_list=[]

for i in range(5):
	score_list.append([input('{0}번 과목의 이름입력'.format(i+1))])
	score_list[i].append(int(input('점수입력')))

for i in range(5):
	if score_list[i][1]>=95:
		score_list[i].append(4.5)
		score_list[i].append('A+')
	elif score_list[i][1]>=90:
		score_list[i].append(4.0)
		score_list[i].append('A')
	elif score_list[i][1]>=85:
		score_list[i].append(3.5)
		score_list[i].append('B+')
	elif score_list[i][1]>=80:
		score_list[i].append(3.0)
		score_list[i].append('B')
	elif score_list[i][1]>=75:
		score_list[i].append(2.5)
		score_list[i].append('C+')
	elif score_list[i][1]>=70:
		score_list[i].append(2.0)
		score_list[i].append('C')
	elif score_list[i][1]>=65:
		score_list[i].append(1.5)
		score_list[i].append('D+')
	elif score_list[i][1]>=70:
		score_list[i].append(1.0)
		score_list[i].append('D')
	else:
		score_list[i].append(0)
		score_list[i].append('F')

high_index=0
for i in range(1,5):
	if score_list[high_index][1]<=score_list[i][1]:
		high_index=i
print('가장 점수가 높은 과목은 {0}, 학점은 {1}입니다.'.format(score_list[high_index][0],score_list[high_index][3]))

average=0
fail=0
for i in  range(5):
	average+=score_list[i][2]
	if score_list[i][2]==0:
		fail+=1
average=average/5
if fail<2:
	print('평균 학점은 {0}점 입니다.'.format(average))
else:
	print('낙제!')





