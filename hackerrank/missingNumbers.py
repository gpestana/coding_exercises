def process(originalArr, modifiedArr):
    res = []
    nrFreq = {}
    
    for c in originalArr:
        nr = int(c)
        if nr in nrFreq:
            nrFreq[nr] += 1 
        else:
            nrFreq[nr] = 1

    for c in modifiedArr:
        nr = int(c)
        nrFreq[nr]-=1
    
    for k, v in nrFreq.iteritems():
        if v != 0 and k not in res:
            res.append(k)
            
    res.sort()
    str_len = str(res[0])
    for r in xrange(1, len(res)):
        str_len+=' '+str(res[r])

    return str_len
        

if __name__ == '__main__':
    sizeModified = int(raw_input())
    modifiedArr = raw_input().split(" ")
    sizeOriginal = int(raw_input())
    originalArr = raw_input().split(" ")
    
    print process(originalArr, modifiedArr)
