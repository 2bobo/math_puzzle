# coding=utf-8

# 解き方が思いつかなかったので写経的に

def move(log):
    cnt = 0
    if len(log) == N + 1:
        return 1
    for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        next_pos = [log[-1][0] + d[0], log[-1][1] + d[1]]
        if next_pos not in log:
            cnt += move(log + [next_pos])
    return cnt


if __name__ == '__main__':
    N = 12
    print(move([[0, 0]]))
