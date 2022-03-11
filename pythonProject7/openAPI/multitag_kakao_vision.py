import sys
import argparse
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
    print(response)
    json_result=response.json()
    print(json_result)
    result=json_result['result']
    print(result)
    label_kr=result['label_kr']
    print(label_kr)


if __name__=='__main__':
    multi_tag('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTFfMTM3%2FMDAxNjQ0NTQxMzUzMzEy.ihz9DF1aDBi7OvqsxMWjTvwAfD5sgymT2d0kT9BKFzUg.U70Z8i2BTJeHBjz5n4wXNEadE8Z0hkrnDLny718ybyYg.JPEG.ameliepink%2FIMG_9694.jpg&type=sc960_832')

