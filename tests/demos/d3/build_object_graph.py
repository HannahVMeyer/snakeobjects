def run(proj,OG):
    OG.add("base","o", {"a":"alabala nica"})
    for i in range(2):
        OG.add("sample","sample%d" % (i),{"g":"value%d" % (i)},OG["base"])
    OG.add("report","o", {}, OG["sample"])
