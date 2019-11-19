"""
空洞文件（占空间）
"""
f = open('test','wb')
f.write(b'S')
f.seek(1024*1024)
f.write(b'E')
f.close()