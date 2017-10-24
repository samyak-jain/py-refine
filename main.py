from itertools import chain, combinations


listOfColumns = []
fd = {}
comb = chain(*map(lambda x: combinations(listOfColumns, x), range(0, len(listOfColumns)+1)))

def attr_closure(i, f):
	result = {i: set()}
	oldresult = {}
	while result != oldresult:
		oldresult = result
		for e in f.items():
			if e[0] in result.keys():
				result[i] += e[1]

	for ele in i:
		result[i].discard(ele)

	if result[i] == set():
		del result[i]

	return result


def closure(f):
	re = {}
	for j in comb:
		i = tuple(j)
		result = attr_closure(i, f)
		re = {**re, **result}

	return re

def superkey(attr, cf):
	return set(cf[attr] + attr) == set(listOfColumns)


def bcnf(si, f):
	cf = closure(f)
	for i in cf.keys():
		if not superkey(i, cf):
			return False

	return True


def decompose(r, si, f):
	out = []
	if bcnf(r, f):



r = []

for i in f.items():
	if len(i[0])>1:
		k = []
		for j in i[0]:
			if not i[1] in attr_closure(i[0] - {j}, f)[i[0]]:
				k.append(j)
	cfd[k] = i[1]



for i in listOfColumns:
	if bcnf(i,cfd)==True:
		r.append(i)
	else:
		merge(decompose(r, i,cfd), r)

print(r)