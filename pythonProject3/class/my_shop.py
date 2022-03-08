from function.exam.shop import Shop

shop1=Shop()

shop1.name='가게1'
shop1.location='서울'
print(shop1)

shop1.total_price(5, 3000)
shop1.total_count(200)