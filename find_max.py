def find_max(a_list):
    # if a_list == []:
    #     return 0

    if not a_list:
        return 0
    else:
        now = a_list[0]
        for a in a_list:
            if a > now:
                now = a 
        return now
                

print(find_max([1,2,3]))
print(find_max([]))