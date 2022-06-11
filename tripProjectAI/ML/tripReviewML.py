import os #절대경로 조회를 위한 라이브러리
import joblib
import re
# pandas 1.3.5,  numpy 1.19.0, konlpy 0.6.0

class ML:
    trip_review_SA_lr = joblib.load(os.path.abspath('ML/trip_review_SA_lr.pkl'))
    trip_review_tfidf = joblib.load(os.path.abspath('ML/trip_review_tfidf.pkl'))
    # 다른 곳에서 import하기 위해 절대 경로로 불러와 줌

    def predict(self, str):
        str=re.sub(r'[^ ㄱ-ㅎ|가-힣]+', "", str)

        st_tfidf_df = self.trip_review_tfidf.transform([str])

        result = self.trip_review_SA_lr.predict(st_tfidf_df[0])

        if (result[0] == 0):
            print('부정')
            return 2
        else:
            print('긍정')
            return 1

