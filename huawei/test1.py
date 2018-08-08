import sys

if __name__=="__main__":

    strs = sys.stdin.readline().strip()
    cs = list(strs)
    new_cs = []
    for c in cs:
        if ord(c)>=ord('a') and ord(c)<=ord('z'):
            new_cs.append(c.upper())
        elif ord(c)>=ord('A') and ord(c)<=ord('Z'):
            new_cs.append(c.lower())
        else:
            new_cs.append(c)

    print(''.join(new_cs))