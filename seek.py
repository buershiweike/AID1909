"""
seek.py 文件偏移量示例
"""

f = open('test','wb+') #读写

f.write(b"Hello world\n")
f.flush()
print("文件偏移量大小：",f.tell())

#修改文件偏移量
f.seek(0,0)
data = f.read()
print(data)

f.close()