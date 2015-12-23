"""
Solves http://www.codenewbie.org/blogs/just-one-more .
"""
import re

def int_to_int(some_list):
    return [some_list[index] + 1 for index in range(len(some_list))]

def str_to_int(some_list):
    new_list = []
    for index in range(len(some_list)):
        # checks for positive and negative numbers.
        items = re.findall('(-?\d+)', some_list[index])
        if items:# Checks to make sure it is not None
            new_list.append(int(items[0])+1)
    return new_list

def str_to_str(some_list):
    result = []
    sa = []
    sn = []
    a0 = []
    a1 =[]
    n0 = []
    n1 = []
    numbers = re.compile(r"\d+")
    letters = re.compile(r"[a-z]+")
    for index in range(len(some_list)):
        # Handles the odd ball cases like 'cd100ef12'.
        if re.match(r'[a-z]+[0-9]+[a-z]+[0-9]+', some_list[index]):
            sa.extend([a for a in letters.findall(some_list[index])])
            sn.extend([str(int(i) + 1).zfill(2) for i in numbers.findall(some_list[index])])
            try:
                for i in range(len(sa)):
                    if sa[i]+sn[i]+sa[i+1]+sn[i+1] not in result:
                        if i % 2 ==0:# To make sure every other item in the list gets in.
                            result.extend([sa[i]+sn[i]+sa[i+1]+sn[i+1]])
            except IndexError:
                pass
        else:
            # Handles cases where the number is 01 or 09.
            if re.match(r'[a-z]+[0]+', some_list[index]):
                a1.extend([a for a in letters.findall(some_list[index])])
                n1.extend([str(int(i) + 1).zfill(2) for i in numbers.findall(some_list[index])])
                try:
                    result.extend([a1[i]+n1[i] for i in range(len(a1))if a1[i]+n1[i] not in result])
                except IndexError:
                    pass
            else:
                # This handles everything else that isn't odd in some way.
                a0.extend([ a for a in letters.findall(some_list[index])])
                n0.extend([str(int(i) + 1) for i in numbers.findall(some_list[index])])
                result.extend([a0[i]+n0[i] for i in range(len(a0)) if a0[i]+n0[i] not in result])
    return result
