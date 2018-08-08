import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    prices = list(map(int,line.split(',')))
    line = sys.stdin.readline().strip()
    weights = list(map(int,line.split(',')))
    line = sys.stdin.readline().strip()
    cap = int(line)

    if cap < min(weights):
        p = 0

    elif cap>sum(weights):
        p = 0
        for pri in prices:
            p +=pri

    else:
        s = 0
        indexs = [0,1,2,3,4]
        for i in indexs:      #1
            tmp = prices[i]
            if tmp>s and weights[i]<=cap:
                s = tmp
        l_tmp = []
        for i in indexs:    #2
            for j in range(i+1,len(indexs)):
                tmp = prices[i]+prices[j]
                tmp_w = weights[i]+weights[j]
                if tmp>s and tmp_w<=cap:
                    s =tmp

        # print(s)
        for i in indexs:   #3
            for j in range(i+1,len(indexs)):
                for k in range(j+1,len(indexs)):
                    tmp = prices[i]+prices[j]+prices[k]
                    tmp_w = weights[i]+weights[j]+weights[k]
                    if tmp>s and tmp_w<=cap:
                        s = tmp

        for i in indexs:
            for j in range(i+1,len(indexs)):
                for k in range(j+1,len(indexs)):
                    for r in range(k+1,len(indexs)):
                        tmp = prices[i] + prices[j] + prices[k]+prices[r]
                        tmp_w = weights[i] + weights[j] + weights[k]+weights[r]
                        if tmp > s and tmp_w <= cap:
                            s = tmp
        p = s
    print(p)