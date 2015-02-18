def process(string):
    count = 0
    N = int(string)
    for char in string:
        nr = int(char)
        if nr != 0:
            if N%nr==0:
                count+=1
    return count
        
if __name__ == '__main__':
    nrInput = raw_input()
    for i in xrange(int(nrInput)):
        string = raw_input()
        print process(string)
