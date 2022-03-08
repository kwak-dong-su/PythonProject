class Shop:
    name=''
    location=''

    def total_price(self, num, price):
        print('총 결제금액은 {0}원입니다.'.format(num*price))

    def total_count(self, count=100):
        print('오늘은 평균보다 {0}명 많이 들어왔어요.'.format(count-100))

    def __str__(self):
        return str(self.name)+','+str(self.location)
