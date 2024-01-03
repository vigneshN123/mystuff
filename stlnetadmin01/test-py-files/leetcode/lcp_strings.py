import ipdb

def longestCommonPrefix(strs):
    e_list = []
    x = 0
    while x < len(strs):
        strs[x] = list(strs[x])
        e_list.append(len(strs[x]))
        x+=1
    #ipdb.set_trace()
    e_list.sort()
    print(e_list)
    new_list = []
    for i in range(len(strs)):
        #ipdb.set_trace()
        if len(strs[i]) == e_list[0]:
            new_list = strs.pop(i)
            break
        else :
            pass
    y = 0
    list_c = []
    list_d = []
    while y < len(strs):
        for i in strs[y]:
            for j in new_list:
                if i == j:
                    # record that value
                    list_c.append(i)
                else:
                    pass
            print(list_c)
            list_d.append(list_c)
       # ipdb.set_trace()
        y+=1
    #print(list_d)
    z = "".join(list_d[0])
    return z

test_list = ["apple", "pineapple", "custardaple"]
longestCommonPrefix(strs = test_list)

