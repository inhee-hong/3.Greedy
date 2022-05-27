def split(s):
    queue = []
    positive = 0
    negative = 0
    while s:
        c = s.pop(0)
        queue.append(c)
        if c == "(":
            positive += 1
        else:
            negative += 1
        if positive == negative:
            break
    return queue, s


def is_correct(s):
    if len(s) == 0:
        return True

    stack = []
    while s:
        c = s.pop(0)
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return not stack


def reverse(strings):
    r = {"(":")", ")": "("}
    return [r[s] for s in strings]


def solution(p):
    p = list(p)

    def recursive(s):
        if not s:
            return []
        u, v = split(s)
        if is_correct(list(u)):
            return u + recursive(v)
        else:
            u = u[1:-1]
            return ["("] + recursive(v) + [")"] + reverse(u)

    answer = recursive(p)
    return "".join(answer)
