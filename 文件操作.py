import os
# #文件写入w
# f = open(r'E:\test\test.txt','w')
# f.write("avsdasd")
# f.close()
# #文件读取r
# f = open(r'E:\test\test.txt', 'r')
# print(f.read())
# f.close()
# #文件追加
# f = open(r'E:\test\test.txt','a')
# f.write("avsdasd")
# f.close()

f = open(r'E:\test\test.txt','r')
print(f.readlines())
f.close()

#判断现在正在实用的平台，Windows 返回 ‘nt'; Linux 返回’posix' rename(需要修改的文件名, 新的文件名) 也可以做剪切。
print(os.name)
#得到当前工作的目录。
print(os.getcwd())
#指定所有目录下所有的文件和目录名。以列表的形式全部列举出来，其中没有区分目录和文件。
print(os.listdir())
#删除指定文件
# os.remove("helloWorld.py")

