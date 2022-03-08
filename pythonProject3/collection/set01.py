jumsu_1={100, 99, 88, 77}
jumsu_2={90, 99, 88, 66}

#두 학기 내내 동일한 성적인 점수는?, 과목 수는?
i= jumsu_1 & jumsu_2
print('성적이 동일한 과목들의 점수는 {0}이고, 과목 수는 {1}개입니다.'.format(i,len(i)))

#두 학기를 비교했을 때 1학기 성적 중 2학기와 다른 성적은?
i=(jumsu_1-jumsu_2) | (jumsu_2-jumsu_1)
print('성적이 다른 과목들의 점수는 {0}입니다'.format(i))

#두 학기 동안 내가 획득한 전체 점수 목록은?
i=jumsu_1|jumsu_2 # | : 버티컬 바
print('전체 점수 목록은 {0}입니다.'.format(i))

#정렬하고 싶어요!
result=list(i) #list()한 결과, 비파괴형 함수
result.sort() #void, 파괴형 함수
print(result)
result.reverse()
print(result)

#1학기 성적에 음악점수 50점 추가
jumsu_1.add(50)
print(jumsu_1)

#2학기 성적에 음악 77, 컴퓨터 100점 추가
jumsu_2.update({77, 100})
print(jumsu_2)

#1학기 성적 모두 삭제
jumsu_1.clear()
print(jumsu_1)




