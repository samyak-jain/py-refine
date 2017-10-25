nr = {}


def attr_closure(i, f):
    i = tuple(i)
    result = {i: set()}
    oldresult = {}
    while result != oldresult:
        oldresult = result
        for e in f.items():
            if e[0] in result.keys():
                result[i] = result[i] | set(e[1])

    for ele in i:
        result[i].discard(ele)

    if result[i] == set():
        del result[i]

    return result


def superkey(r, attr, fd):
    cf = attr_closure(attr, fd)
    # print(cf,attr,fd)
    fin = set(attr)
    if cf.get(attr) is not None:
        fin = fin | cf.get(attr)
    return set(fin) == set(r)


def bcnf(r, fd):
    global nr
    for i in fd.items():
        if not superkey(r, i[0], fd):
            nr = i
            return False

    return True


def canon(f):
    cfd = {}
    for i in f.items():
        k = tuple()
        if len(i[0]) > 1:
            for j in i[0]:
                l = tuple(set(i[0]) - {j})
                try:
                    if not i[1] in attr_closure(l, f)[l]:
                        k = list(k)
                        k.append(j)
                        k = tuple(k)
                except KeyError:
                    k = list(k)
                    k.append(j)
                    k = tuple(k)
        else:
            cfd[i[0]] = i[1]

        if len(k) > 0:
            cfd[k] = i[1]

    return cfd


def getBCNF(rstr, fdstr):
    R = set(rstr)
    FD = fdstr
    # print(R, FD)
    S = [R]
    FD = canon(FD)

    while bcnf(S[0], FD) == False:
        S.append(set(list(nr[0]) + list(nr[1])))
        S[0] -= set(nr[1])
        del FD[nr[0]]
        if len(S[0]) < 2:
            S.pop(0)

    S = list(map(list, S))
    return S
