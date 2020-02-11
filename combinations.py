from itertools import chain, combinations
def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))
stuff = [1,2,3,4]

for subset in all_subsets(stuff):
    print(subset)