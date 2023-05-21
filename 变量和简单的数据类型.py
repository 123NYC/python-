'''
fn='123'
ln='456'
fn=f'{fn}\n\t{ln}' #format 新用法  等同  fn='{}{}'.format(fn,ln)
print(fn)
'''

#删除末尾空白  .rstrip()   开头空白 .lstrip()      字符串两边空白  .strip()
'''
n1='  sdf  gds  sdg     '
print(len(n1))
n2=n1.rstrip()
print(len(n2))
print(n1)
n3=n1.lstrip()
print(n3)
n4=n1.strip()
print(n4)
print(len(n4))
'''


# n1="one of dsf'dsfs"  #字符串中有撇号时，外面用双引号
# print(n1)



# car=['bmw','audi','toyota','subaru']
# #按照字母排序
# car.sort()       #永久改变列表顺序
# print(car)
# #按照字母倒序排序
# car.sort(reverse=True)     #永久改变列表顺序
# print(car)

# cars=['bmw','audi','toyota','subaru']
# print(cars)
# print(sorted(cars))
# print(sorted(cars,reverse=True))
# #  print(sorted(reverse=True,cars))  错误
# print(cars)

# car=['bmw','audi','toyota','subaru']
# print(car)
# car.reverse()   #按照当前顺序反转，不按照字母反转
# print(car)

#创建平方列表
squares=[]
for value in range(1,5):
    square=value**2
    squares.append(square)
    pass
print(squares)

pingfang=[val**2 for val in range(1,11)]
print(pingfang)

#asads
