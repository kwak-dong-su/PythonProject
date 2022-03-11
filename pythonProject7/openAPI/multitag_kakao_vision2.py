import sys
import argparse
from tkinter import messagebox

import requests #알트+엔터(cmd+1)
from collections import Counter

#kakao연결 + 신청해놨던 키.
API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'a7b67eb75e39a57c2ef640b5fffb81dd'

def multi_tag(image_url):
    header={'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    img_data={'image_url' : image_url}
    requests.post(API_URL, headers=header, data=img_data)
    response=requests.post(API_URL,
                           headers=header,
                           data=img_data)
    #print(response)사람들
    json_result=response.json()
   # print(json_result)
    result=json_result['result']
    #print(result)
    label_kr=result['label_kr']
    #print(label_kr)
    return label_kr


if __name__=='__main__':
    img_list=['https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTFfMTM3%2FMDAxNjQ0NTQxMzUzMzEy.ihz9DF1aDBi7OvqsxMWjTvwAfD5sgymT2d0kT9BKFzUg.U70Z8i2BTJeHBjz5n4wXNEadE8Z0hkrnDLny718ybyYg.JPEG.ameliepink%2FIMG_9694.jpg&type=sc960_832',
              'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTEwMzBfNiAg%2FMDAxNjM1NTgxODkyMDQy.lW33tKnk3EcG4-arS82NW4nwCrLRotM4oIC6_hnxnqgg.OLaiYRA2HeumwOoTNCk4bbx8zO0IuYgFjua12B0u0VUg.JPEG.hee112424%2Fpok8.jpg&type=sc960_832',
              'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzAzMThfMTQx%2FMDAxNDg5ODQ0NTI2Njg0.aw5kiA64GDFkMWEN9Rb1KZBjV0yc_kMPzq-wHp_f_m4g.tWywBdOcg1R0WzXvak9fgGvZOG6OQAEn0wCSyjVodfsg.JPEG.dovmfwoa%2F2014097_1488890242694.jpg&type=sc960_832',
              'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F003%2F2022%2F01%2F03%2FNISI20220103_0018302143_web_20220103124328_20220103124407058.jpg&type=sc960_832',
              'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F396%2F2021%2F08%2F01%2F0000588233_001_20210801173212646.jpg&type=sc960_832',
              'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20110812_283%2Fxmagicno1_1313118145668yu1FR_JPEG%2FF110812_008.jpg&type=sc960_832',
              'http://img4.tmon.kr/cdn3/deals/2019/09/30/2469722914/2469722914_front_d74828778c.jpg',
              'https://dimg.donga.com/a/540/0/90/5/wps/NEWS/IMAGE/2020/01/15/99227983.1.jpg'
              ]
    result_list=[]
    for img in img_list:
        result_list+=multi_tag(img)

    print(result_list)

    count_result=Counter(result_list)
    print(count_result)
    print(count_result.get('사람'))
    print(count_result.most_common(5))
    order_5=count_result.most_common(5)
    print(order_5[0])
    order_1=order_5[0]
    print('제일 빈도수가 높은 단어는 ', order_1[0], ', 빈도수는 ', order_1[1] )

    if order_1[0]=='사람':
        tour='제주도'
    elif order_1[0]=='남성':
        tour='등산'
    else:
        tour='놀이공원'
    messagebox.showinfo('추천', '당신에게 '+tour+'를 추천합니다.')


