
def parse_input_str(seq = ' '):
    rawString = input()
    items = rawString.split(seq)
    return items

def parse_input_to_num(seq = " "):
    rawString = input()
    items = rawString.split(seq)
    nums = []
    for item in items:
        nums.append(int(item))
    return nums


def error_check_for_input(x):
    if False:
        print("error")
        exit()

def for_output(x,seq=" "):
    return seq.join([str(item) for item in x])


"""
    for line in sys.stdin:
        a = line.split()
        print(int(a[0]) + int(a[1]))
        
    import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)      
"""
if __name__=="__main__":
    # a = parse_input_str()
    # print(a)
    # print("\n")
    #
    # b =parse_input_to_num()
    # print(b)
    print(' '.join(['er','wer','sadsf']))
    y = for_output([23,45,'rtrew',56])
    # 本题为考试单行多行输入输出规范示例，无需提交，不计分。
    # coding=utf-8
    import sys

