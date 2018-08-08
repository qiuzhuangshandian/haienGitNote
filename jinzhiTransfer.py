

ch = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ch_dict = {}
for i,c in enumerate(ch):
    ch_dict[c] = i
print(len(ch))
def tenToAny(num,t):
    collect = ''
    while num!=0:
        res = num % t
        c = ch[res]
        collect = c+collect
        num = int(num / t)
    return collect

def anyToTen(str,t):
    s = 0
    for i,item in enumerate(str[::-1]):
        s+=ch_dict[item]*t**(i)
    print(s)

a = tenToAny(100,7)
print(a)
print('true:',hex(100))

anyToTen('101',2)