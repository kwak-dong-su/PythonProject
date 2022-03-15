
p_list=[]
for i in range(10):
    if i==0:
        p_list.append(i+1)
    elif i==1:
        p_list.append(p_list[i-1])
    else:
        p_list.append(p_list[i-1]+p_list[i-2])

print(p_list)

x = y = 40
z = 1 + x if x > y else y + 2
print(z) # x>y가 False이므로 y(40)+2를 반환, 이후 z에 대입


x = y = 40
z = 1 + (x if x > y else y) + 2 #괄호 안의 코드부터 수행 -> x>y가
print(z)


