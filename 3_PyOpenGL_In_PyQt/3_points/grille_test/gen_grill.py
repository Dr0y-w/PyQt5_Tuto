import random as rd


def flou(format, height, ecart):
    li = []
    for j in range(format):
        for i in range(format):
            if i!=0:
                li.append(li[-1])
            li.append(height-i-1-j+rd.randint(-ecart, ecart))
    return li[1:]
def gril(format):
    l = []
    for i in range(format):
        for j in range(format):
            l.append([i, j, 0])
    return l
