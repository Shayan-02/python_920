s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s3 = s1.difference(s2) # 1, 2 ,3
s4 = s2.difference(s1) # 6, 7, 8
s5 = s1.intersection(s2) # 4, 5
s6 = s1.union(s2) # 1, 2, 3, 4, 5, 6, 7, 8
# s1.difference_update(s2)
# s2.difference_update(s1)
# s1.intersection_update(s2)
# s2.intersection_update(s1)
s7 = s1.symmetric_difference(s2)
s8 = s2.symmetric_difference(s1)
print(s3, s4, s5, s6, s7, s8, sep="\n")

s1.add(9)
s1.discard(9)