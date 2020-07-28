# i=1
# sum=0
# while i<=100 :
#     if ( i != 1 and i % 2 == 0 or i % 3 == 0 or i % 5 ==0 or i % 7 == 0  ):
#         i += 1
#     else:
#         print(f"{i}")
#         sum += i
#         i += 1
#     i += 1
# print(sum+2+3+5+7-1)

1234567891011
i = 2   # 1不是质数，所以直接从2开始
result = 0  #接收我们打印出来的质数并求和
while i <= 100  :#循环2-100之间的所有的数
    j = 2    #质数是除了1和它本身以外的的数都不能除尽，所以没必要判断1
    while j < i:    #将所有的比本身小的数除一遍，如果都有余数，那么这个数是一个质数
        if i % j == 0 : 
            break   #如果是通过break退出，则不执行else语句
        j += 1
    else:   #如果循环是正常退出，执行else语句。
        result += i
    i += 1
print(result)
