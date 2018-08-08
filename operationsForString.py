s = " python string"
print(s)  # " python string"
print("p" in "python")  #True


# 去首尾空格
print(s.strip()) #python string

print(s.lstrip())

print(s.rstrip())

str = 'mississippi'
print(str.rstrip('ip'))

str = 'ab c\n\nde fg\rkl\r\n'
print(str.splitlines())    # ['ab c', '', 'de fg', 'kl']   按照行('\r', '\r\n', \n')分隔
print(str.splitlines(True))  # ['ab c\n', '\n', 'de fg\r', 'kl\r\n'] 如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符

#查找:
s = " python string"
print(s.find("s"))  #8
print(s.index("s")) #8

print(s.rfind("s")) #8
print(s.rindex("i")) #11


#替换
print(s.replace('p','c'))

#计数
print(s.count("t")) #2
print(s.count("tr")) #1


s = "098"
print(int(s))