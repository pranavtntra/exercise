def fibonnaci(n):
    s = [0,1]
    list(map(lambda _: s.append(sum(s[-2:])),range(2,n)))
    return s[:n]