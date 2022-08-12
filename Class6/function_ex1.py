# def get_max_1 (n1,n2,n3):
#     if n1 > n2:
#         if n1 > n3:
#             return n1
#     elif n2 > n1:
#         if n2 > n3:
#             return n2
#         else:
#
#     elif n3 > n1:
#         if n3 > n2:
#             return n3
#
# #When function, need to tell it what to do: print
# print(get_max_1(1,2,3))

# def get_max_2(n1, n2, n3):
#     if n1 > n2 and n1 > n3:
#         return n1
#     if n2 > n3:
#         return n2
#     else:
#         return n3
# print(get_max_2(1,2,3))


def get_max_1(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(n1)
    if n2 > n3:
        print(n2)
    print(n3)

def get_min(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        print(n1)
    if n2 < n3:
        print(n2)
    print(n3)

#Return ALWAYS BETTER, you can do stuff with output, its dynamic and usable for further computation
def get_max_1(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return(n1)
    if n2 > n3:
        return(n2)
    return(n3)

def get_min(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return(n1)
    if n2 < n3:
        print(n2)
    return(n3)




span_of_numberts = get_max_1(6,7,8) - get_min(6,7,8)
print(span_of_numberts)


# ##LIST
#
# def get_max_3(n1, n2, n3):
#     temp_list = [n1, n2, n3]
#     return max(temp_list)
#
# print(get_max_3(7,8,9))