## tri-gram

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = sys.stdin.read()
    s = list(s.lower().split('.'))

    tri_list = []
    for sen in s:
        sen = list(sen.split())
        for i in range(len(sen)):
            if i+3 == len(sen):
                tri_list.append(sen[i:])
                break
            else:
                tri_list.append(sen[i:i+3])
    
    dic = {}
    max_ = 0
    max_value = 0
    for j in range(len(tri_list)):
        dic[str(tri_list[j])] = tri_list.count(tri_list[j])
        if max_value < tri_list.count(tri_list[j]):
            max_value = tri_list.count(tri_list[j])
            max_ = tri_list[j]

    print(*max_)
