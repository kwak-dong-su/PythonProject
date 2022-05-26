from django.contrib import admin
from django.urls import path

import placeReview.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', placeReview.views.main),
    path('placeReview/insertReview', placeReview.views.insertReview),
    path('placeReview/deleteReview/<review_place_name>/<id>/<member_name>', placeReview.views.deleteReview),
    path('placeReview/reviewList/<review_place_name>/<member_name>', placeReview.views.reviewList),
]
