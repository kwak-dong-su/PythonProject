from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# member 메뉴와 관련된 컨트롤러 역할
# urls.py에 요청된 주소별로 함수가 지정되어 있어야 함
# 요청된 주소 하나당 함수 하나
# 요청된 주소에 따른 함수를 view.py에 정의

def index(request):
    print('홈페이지 시작화면입니다.')
    # return HttpResponse('내가 시작하는 첫 페이지')
    # return HttpResponse(
    #     "<body bgcolor=white>"+
    #     "<h3>장고 프로젝트1</h3><hr color=red>"+
    #     "<a href='member/'>start page</a><br>"+
    #     "<a href='member/index1'>index1 page</a><br>"+
    #     "<a href='member/index2'>index2 page</a><br>"+
    #     "<a href='member/index3'>index3 page</a><br>"+
    #     "<a href='admin/'>admin page</a><br>"+
    #     "<a href='http://www.naver.com'>naver</a><br>"+
    #     "<a href='http://www.daum.net'>daum</a>"+
    #     "</body>"

    return render(request, 'member/index.html')

def index1(request):
    return HttpResponse(
        "<body bgcolor=skyblue>"+
        "<h3>index1 페이지입니다.</h3><hr color=red>"+
        "<a href='/member/'>start page</a><br>" +
        "<a href='/'>index page</a><br>"
        "</body>"
    )

def index2(request):
    return HttpResponse(
        "<body bgcolor=lightgreen>"+
        "<h3>index2 페이지입니다.</h3><hr color=red>"+
        "<a href='/member/'>start page</a><br>" +
        "<a href='/'>index page</a><br>"
        "</body>"
    )

def index3(request):
    return render(request, 'member/index3.html')

def start(request):
    print('시작페이지 호출됨')
    return HttpResponse('내가 리턴되는 내용임')