set1 = {1 ,  3 , 4}
set2 = {13 , 21 , 9}

intersec = set1.intersection(set2)
print(intersec)
#იყებს საერთო ელემენტებს

union = set1.union(set2)
print(union)
#აერთებს ყველაფერს

difference = set1.difference(set2)
print(difference)
#პირველიდან იყებს იმ ელემენტებს რომლებიც არ არიან მეორეში

sym_dif = set1.symmetric_difference(set2)
print(sym_dif)
#იყებს ყველა ელემენტს საერთოს გარდა
