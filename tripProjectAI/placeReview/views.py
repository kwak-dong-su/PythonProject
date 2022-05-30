from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from placeReview.models import review
from ML.tripReviewML import ML
<<<<<<< HEAD
from ML.NLP import NLP
=======
>>>>>>> a4dd04e6cc2b279de64c8fc7ad6f96536f1bb6ff

def main(request):
    return render(request, 'placeReview/main.html')


def reviewList(request, review_place_name, member_name, page):
    print(review.objects.filter(review_place_name=review_place_name).order_by('-id'))
    print(member_name)
    index=(int(page)-1)*5 # 가져올 페이지 리뷰의 시작 인덱스
    empty=[0]*(5-review.objects.filter(review_place_name=review_place_name).order_by('-id')[index:index+5].count())
    # 페이지 row를 5개로 맞추기 위한 빈칸 출력용 변수

    nlp = NLP()  # 자연어 처리를 위한 객체

    pos_reviews=review.objects.filter(review_place_name=review_place_name, review_pos_neg=1).values('review_content') # 긍정 리뷰의 review_content 컬럼만 필터링하여 가져옴. QuerySet 타입
    neg_reviews=review.objects.filter(review_place_name=review_place_name, review_pos_neg=2).values('review_content') # 부정 리뷰의 review_content 컬럼만 필터링하여 가져옴. QuerySet 타입
    topWord, posOrNeg=nlp.mostCommonWord(review_place_name, pos_reviews, neg_reviews) #여행지명과 필터링된 긍/부정 QuerySet을 인자값으로 넘겨줌. 디폴트값 top=8

    result = {
        'review_place_name': review_place_name,
        'member_name': member_name,
<<<<<<< HEAD
        'list': review.objects.filter(review_place_name=review_place_name).order_by('-id')[index:index+5], # 시작 인덱스부터 5개 가져옴
        'empty': empty,
        'pos': review.objects.filter(review_place_name=review_place_name, review_pos_neg=1).count(),
        'neg': review.objects.filter(review_place_name=review_place_name, review_pos_neg=2).count(),
        'page': page,
        'totalPage': int((review.objects.filter(review_place_name=review_place_name).count()-1)/5)+1, # 총 페이지 개수
        'topWord': topWord, # 빈도수 n위까지의 list
        'posOrNeg': posOrNeg # jQCloud의 색상 지정을 위한 긍정 부정 구분 list
=======
        'list': review.objects.filter(review_place_name=review_place_name).order_by('-id'),
        'pos': review.objects.filter(review_place_name=review_place_name, review_pos_neg=1).count(),
        'neg': review.objects.filter(review_place_name=review_place_name, review_pos_neg=2).count()
>>>>>>> a4dd04e6cc2b279de64c8fc7ad6f96536f1bb6ff
    }
    return render(request, 'placeReview/reviewList.html', result)

def insertReview(request):
    data=request.POST
    print(data)
<<<<<<< HEAD
    ml=ML() #감정 분석을 위한 객체
=======
    ml=ML()
>>>>>>> a4dd04e6cc2b279de64c8fc7ad6f96536f1bb6ff
    pos_neg=ml.predict(data['review_content']) # 딥러닝 모델 불러와서 감정 분석 후 결과값 넣기
    one = review(review_place_name=data['review_place_name'], review_pos_neg=pos_neg, review_content=data['review_content'], review_writer=data['review_writer'])
    one.save()
    return redirect('/placeReview/reviewList/'+data['review_place_name']+'/'+data['review_writer']+'/1')
    # insert 후 1페이지로

def deleteReview(request, review_place_name, id, member_name, page):
    print(id)
    one = review.objects.get(id=id)
    one.delete()

    return redirect('/placeReview/reviewList/'+review_place_name+'/'+member_name+'/'+page)
    # delete 후 해당페이지로