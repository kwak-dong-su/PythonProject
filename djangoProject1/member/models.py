from django.db import models

# Create your models here.
# 장고는 sql문을 몰라도 테이블을 생성할 수 있도록 제공
# ORM을 models.py에 정의
# 테이블 하나당 클래스 하나로 ORM을 정의

class Member(models.Model):
    # 멤버 변수를 생성하주면
    # 1. vo의 변수 역할
    # 2. table의 항목을 생성
    user_id=models.CharField(max_length=255)
    user_pw=models.CharField(max_length=255)
    user_name=models.CharField(max_length=255)
    user_tel=models.CharField(max_length=255)

    # java vo에서의 toString()역할
    def __str__(self):
        return self.user_id+', '+self.user_pw+', '+self.user_name+', '+self.user_tel


