import operator

def solution_asc(dic):
    sored_list = []
    dic_key = dic.keys()
    dic_values = dic.values()
    sor_dic_values = sorted(dic_values)
    for e in sor_dic_values:
        sored_elem = (e, dic[e])
        sored_list.append(sored_elem)
    return sored_list

def solution_desc(dic):
    x = solution_asc(dic)
    sored_list_rev = sorted(x, reverse = True)
    print sored_list_rev
    return sored_list_rev

Dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
solution_asc(Dictionary)
solution_desc(Dictionary)
