from django.contrib import admin
from django.urls import path

import member.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member.views.main),
    path('main/', member.views.main),
    path('member/insert', member.views.insert),
    path('member/insert2', member.views.insert2),
    path('member/update/<id>', member.views.update),
    path('member/update2', member.views.update2),
    path('member/delete', member.views.delete),
    path('member/delete2', member.views.delete2),
    path('member/all', member.views.all),
    path('member/search', member.views.search),
    path('member/search2', member.views.search2),
    path('member/login', member.views.login),
    path('member/login2', member.views.login2),
    path('member/logout', member.views.logout),
    path('member/question_list', member.views.question_list),
    path('member/insert_question/<name>', member.views.insert_question),
    path('member/insert_question2', member.views.insert_question2),
    path('member/update_question/<id>', member.views.update_question),
    path('member/update_question2', member.views.update_question2),
    path('member/delete_question/<id>', member.views.delete_question),
]
