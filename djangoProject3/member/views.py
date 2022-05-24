from django.shortcuts import render, redirect

# Create your views here.
from member.models import Test, Question
from datetime import datetime


def main(request):
    return render(request, 'member/main.html')

def insert(request):
    return render(request, 'member/insert.html')

def insert2(request):
    data=request.POST
    print(data)
    one=Test(name=data['name'], tel=data['tel'], addr=data['addr'])
    one.save()
    return render(request, 'member/insert2.html')

def update(request, id):
    # get(주소와 함께 전달되는 값은 컨트롤러 함수 안에 같은 이름의 변수를 선언)
    print(id)
    one = Test.objects.get(id=id)
    result = {
        'one': one
    }
    return render(request, 'member/update.html', result)

def update2(request):
    data = request.POST
    filter = Test.objects.filter(id=data['id'])
    print(filter)
    filter.update(name=data['name'], tel=data['tel'], addr=data['addr'])

    return render(request, 'member/update2.html')

def delete(request):
    return render(request, 'member/delete.html')

def delete2(request):
    data=request.POST
    filter=Test.objects.filter(name=data['name'])
    # filter는 해당 조건 모두 가져옴. list형태이므로, 원하는 레코드 1개만 삭제하기 위해선 filter[0].delete()와 같이 인덱싱이 필요함
    # get은 무조건 1개만 가져옴
    print(filter)
    filter.delete()
    return render(request, 'member/delete2.html')

def all(request):
    print(Test.objects.all())
    result = {
        'list': Test.objects.all()
    }
    return render(request, 'member/all.html', result)

def search(request):
    return render(request, 'member/search.html')

def search2(request):
    data = request.POST
    one = Test.objects.get(name=data['name'])
    result={
        'one':one,
        'test':100 #테스트용
    }
    # controller에서 template으로 값을 넘길 때는 dictionary를 만들어 전달
    return render(request, 'member/search2.html', result)

def login(request):
    return render(request, 'member/login.html')

def login2(request):
    data=request.POST
    one=Test.objects.get(id=data['id'])
    print(one.name)
    if one!=None:
        login='로그인 성공'
        request.session['id']=one.id
        request.session['name']=one.name
    else:
        login='로그인 실패'

    result={'login':login}

    # return render(request, 'member/login2.html', result)
    return redirect('/main')

def logout(request):
    request.session.flush()

    return redirect('/main')

def question_list(request):
    print(Question.objects.all())
    result = {
        'list': Question.objects.all()
    }
    return render(request, 'member/question_list.html', result)

def insert_question(request, name):
    print(name)
    result = {
        'name': name
    }
    return render(request, 'member/insert_question.html', result)

def insert_question2(request):
    data = request.POST
    print(data)
    one = Question(question_text=data['question_text'], question_writer=data['question_writer'], pub_date=datetime.now())
    one.save()

    return redirect('/member/question_list')

def update_question(request, id):
    print(id)
    one = Question.objects.get(id=id)
    result = {
        'one': one
    }
    return render(request, 'member/update_question.html', result)

def update_question2(request):
    data = request.POST
    filter = Question.objects.filter(id=data['id'])
    print(filter)
    filter.update(question_text=data['question_text'])

    return render(request, 'member/update_question2.html')

def delete_question(request, id):
    print(id)
    one = Question.objects.get(id=id)
    one.delete()

    return redirect('/member/question_list')