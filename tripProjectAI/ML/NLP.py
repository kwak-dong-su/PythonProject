from konlpy.tag import Okt
from nltk import FreqDist

class NLP:
    t = Okt()
    stopwords = ["한국", "서울", "풍경", "최고", "추천", "사람", "또한", "방문", "여행",
                 "시간", "타고", "정말", "가장", "항상", "도착", "다른", "매우", "경우",
                 "우리", "이용", "모든", "때문", "장소", "지역", "그것", "가세", "이름",
                 "위치"]

    def mostCommonWord(self, place_name, pos_reviews, neg_reviews, top=8):
        pos_review_list=[]
        neg_review_list=[]

        # 긍정 리뷰 str join
        for one in pos_reviews:
            pos_review_list+=list(one.values())
        # print(' '.join(pos_review_list))

        # 부정 리뷰 str join
        for one in neg_reviews:
            neg_review_list+=list(one.values())
        # print(' '.join(neg_review_list))

        tokens_pos_review = self.t.nouns(' '.join(pos_review_list)) # 긍정 리뷰를 형태소 분석
        tokens_neg_review = self.t.nouns(' '.join(neg_review_list)) # 부정 리뷰를 형태소 분석

        stopwords=self.stopwords+self.t.nouns(place_name)+[place_name] # 불용어에 여행지명과 그 형태소를 추가

        tokens_pos_review = [w for w in tokens_pos_review if w not in stopwords and len(w) > 1]
        tokens_neg_review = [w for w in tokens_neg_review if w not in stopwords and len(w) > 1]
        # 불용어를 제외한 리스트

        fd_pos_review = FreqDist(tokens_pos_review) # 긍정 단어 빈도수 분석
        fd_neg_review = FreqDist(tokens_neg_review) # 부정 단어 빈도수 분석

        # print('fd_pos_review.most_common() >>', dict(fd_pos_review.most_common()))
        # print('fd_neg_review.most_common() >>', dict(fd_neg_review.most_common()))
        # print(fd_pos_review.most_common() + fd_neg_review.most_common())

        # 딕셔너리로 형변환
        fd_pos_review=dict(fd_pos_review.most_common())
        fd_neg_review=dict(fd_neg_review.most_common())

        # 긍정 부정 명시를 위해 value 값 수정
        for key, value in fd_pos_review.items():
            fd_pos_review[key] = ['pos_word', value]
        for key, value in fd_neg_review.items():
            fd_neg_review[key] = ['neg_word', value]

        # print(fd_pos_review)
        # print(fd_neg_review)

        # print(list(fd_pos_review.items())[0][1][0]) # ('바다', ['긍정', 1]) 중 '긍정' (리뷰 없을땐 에러이므로 주석 처리)
        # print(list(fd_pos_review.items()))

        # 긍정, 부정 리뷰 list를 합하여 total_list 생성
        total_list = list(fd_pos_review.items()) + list(fd_neg_review.items())
        print('total_list >> ', total_list)

        # 빈도수 기준으로 내림차순 정렬, 값이 동일할 시 긍정리뷰 우선
        for i in range(len(total_list)):
            for j in range(i+1, len(total_list)):
                if(total_list[i][1][1]<total_list[j][1][1] or ( (total_list[i][1][1]==total_list[j][1][1]) and (total_list[i][1][0]=='neg_word') )):
                    temp=total_list[i]
                    total_list[i]=total_list[j]
                    total_list[j]=temp


        # 중복 키워드 제거, 빈도수 높은 것을 우선으로 함, 값이 동일할  시 부정리뷰 우선
        # 제거할 때 마다 total_list의 길이가 1씩 줄어드므로 total_list[i]에서 index 에러가  남. 이후 break문으로 반복문 종료
        # 중복은 하나만 있으므로, 중복 제거 성공시 break문을 사용해 j의 반복문 종료
        for i in range(len(total_list)-1):
            try:
                for j in range(i+1, len(total_list)):
                    if(total_list[i][0]==total_list[j][0]):
                        if(total_list[i][1][1]<total_list[j][1][1]):
                            del total_list[i]
                            break
                        elif(total_list[i][1][1]==total_list[j][1][1]):
                            if(total_list[i][1][0]=='pos_word'):
                                del total_list[i]
                                break
                            else:
                                del total_list[j]
                                break
                        else:
                            del total_list[j]
                            break
            except:
                break # 리스트 안의 값을 한번이라도 삭제시 total_list[i]는 인덱스 에러가 남. 중복을 모두 제거했다는 의미이므로 break


        print('total_list >> ', total_list)

        # jQCloud 생성을 위한 list, top 개수만큼 선언
        top_word=['']*top
        pos_or_neg=['']*top
        # total_list의 길이가 top 미만일 경우 에러, break문으로 반복문 종료
        for i in range(top):
            try:
                top_word[i]=total_list[i][0]
                pos_or_neg[i]=total_list[i][1][0]
            except:
                break

        print('top_word >> ',top_word)
        print('pos_or_neg >> ', pos_or_neg)

        return top_word, pos_or_neg # 단어 빈도수와 분석 감정을 top 순위까지 list로 return


    # 모든 리뷰의 키워드 순위 분석
    def mostCommonWord_total(self, place_name, reviews, top=8):
        review_list=[]

        # 리뷰 str join
        for one in reviews:
            review_list+=list(one.values())
        # print(' '.join(review_list))

        tokens_review = self.t.nouns(' '.join(review_list)) # 리뷰를 형태소 분석

        stopwords=self.stopwords+self.t.nouns(place_name)+[place_name] # 불용어에 여행지명과 그 형태소를 추가

        tokens_review = [w for w in tokens_review if w not in stopwords and len(w) > 1]
        # 불용어를 제외한 리스트

        fd_review = FreqDist(tokens_review) # 긍정 단어 빈도수 분석

        # print('fd_review.most_common() >>', dict(fd_review.most_common()))

        # 딕셔너리로 형변환
        fd_review=dict(fd_review.most_common())


        print(fd_review)
        print(list(fd_review)[:top])

        return list(fd_review)[:top] # 단어 빈도수와 분석 감정을 top 순위까지 list로 return
