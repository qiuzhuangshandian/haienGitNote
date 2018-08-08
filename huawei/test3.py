import sys

if __name__=="__main__":
    line = sys.stdin.readline().strip().rstrip(';')
    items = line.split(";")
    check_name = sys.stdin.readline().strip()
    target_dict = {}
    flag = False

    # try:
    #     keyWord, ttype, name = items[0].split(' ')
    # except:
    #     print('none')


    for i,block in enumerate(items):
        keyWord,ttype,name = block.strip(' ').split(' ')
        ##################
        if i == 0:
            try:
                keyWord, ttype, name = block.strip(' ').split(' ')
            except:
                print('none')
                flag = True
                break
            if ttype not in ['short','int','long','char','float','double', 'short','int','long','char','float','double'] and not flag:
                print('none')
                flag = True
                break

        ################
        if i == 1:
            if ttype not in list(target_dict.keys()):
                print('none')
                flag = True
                break
        #################
        target_dict[name] = ttype
        if '*' not in ttype:
            target_dict[name+"*"] = ttype+"*"
            target_dict[name+"**"] = ttype+"**"

    if not flag:
        while target_dict[check_name] in list(target_dict.keys()):
            check_name = target_dict[check_name]

        if '*'in target_dict[check_name]:
            cnt = target_dict[check_name].count("*")
            tmp = target_dict[check_name].rstrip("*")

            for _ in range(cnt):
                tmp = tmp+" "+"*"
        else:
            tmp = target_dict[check_name]
        print(tmp)

