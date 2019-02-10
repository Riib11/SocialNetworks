def pairs_unordered(ls): # [A] -> [(A,A)]
    size = len(ls)
    return [
        (ls[i],ls[j])
        for i in range(size)
        for j in range(i+1,size) ]