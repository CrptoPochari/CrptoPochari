def count_products(data):
    wrd_cnt = {}
    for d in data:
        # ds = d.split()
        # ds0 = ds[0]
        # ds1 = int(ds[1])

        name, count = d.split()
        count = int(count)
        if name in wrd_cnt:
            wrd_cnt[name] += count
        else:
            wrd_cnt[name] = count
    return wrd_cnt


data = ["Nac 2", "boo 3", "mac 1","mac 3", "boo 1"]
print(count_products(data))