from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from placeReview.models import review
from ML.tripReviewML import ML

def main(request):
    return render(request, 'placeReview/main.html')


def reviewList(request, review_place_name, member_name):
    print(review.objects.filter(review_place_name=review_place_name).order_by('-id'))
    print(member_name)
    result = {
        'review_place_name': review_place_name,
        'member_name': member_name,
        'list': review.objects.filter(review_place_name=review_place_name).order_by('-id')
    }
    return render(request, 'placeReview/reviewList.html', result)

def insertReview(request):
    data=request.POST
    print(data)
    ml=ML()
    pos_neg=ml.predict(data['review_content']) # 딥러닝 모델 불러와서 감정 분석 후 결과값 넣기
    one = review(review_place_name=data['review_place_name'], review_pos_neg=pos_neg, review_content=data['review_content'], review_writer=data['review_writer'])
    one.save()
    return redirect('/placeReview/reviewList/'+data['review_place_name']+'/'+data['review_writer'])

def deleteReview(request, review_place_name, id, member_name):
    print(id)
    one = review.objects.get(id=id)
    one.delete()

    return redirect('/placeReview/reviewList/'+review_place_name+'/'+member_name)