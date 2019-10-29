f=None
try:
    # print(i)
    f=open("123.txt","r")
    print("hello")
except (FileNotFoundError,NameError) as errormsg:  #捕获多个异常
    print("FileNotFoundError")
    print(errormsg)
else:
    print("木有异常")  #没有异常的时候执行
finally:
    print("finally")   #不管有没有异常总是会执行
    f.close()