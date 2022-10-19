from random import*


def introduce():
    print("请输入比赛场次和两选手水平(0-1之间以逗号间隔):", end="")
    n, a, b = eval(input())
    return n, a, b


def allgames(n, a, b):
    at = bt = 0
    for i in range(n):
        s = onegame(i, a, b)
        if s == 'A':
            at += 1
        else:
            bt += 1
    return at, bt


def onegame(i, a, b):
    ae = be = 0
    char = 'A'
    while not gameover(ae, be):
        if char == 'A':
            if random() > a:
                char = 'B'
            else:
                ae += 1
        else:
            if random() > b:
                char = 'A'
            else:
                be += 1
    if ae == 15:
        print("第{:<2}场比赛 -> A{:<2}:B{:<2}, A win!".format(i+1, ae, be))
        return 'A'
    else:
        print("第{:<2}场比赛 -> A{:<2}:B{:<2}, B win!".format(i+1, ae, be))
        return 'B'


def gameover(ae, be):
    if ae != 15 and be != 15:
        return False
    else:
        return True


def main():
    n, a, b = introduce()
    at, bt = allgames(n, a, b)
    print("共进行{}场，A获胜{}场，B获胜{}场".format(n, at, bt))


main()
