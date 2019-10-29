#encoding=utf-8
#1+2+...+99+100
# sum = 0;
# i=1;
# while i<=100:
#     sum=sum+i
#     i+=1
# print(sum)


#2. 计算1~100之间偶数的累积和（包含1和100）
# sum = 0
# i = 1
# while i<=100:
#     if i%2==0:
#         sum = sum + i
#     i += 1
# print(sum)
sum = 0
for i in range(1,101):
    sum = sum +i
print(sum)


