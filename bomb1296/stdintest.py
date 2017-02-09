import sys
import StringIO
import subprocess
import time
from subprocess import Popen, PIPE
import os

def go(num):
    numstr = str(num)

    lotstring = (numstr + " ") * 10
    print(lotstring)
    #text = open('hello.txt','w')
    p = subprocess.Popen('./safebomb', stdin=PIPE) #stdout=text)

    args = ['Why make trillions when we could make... billions?',
        '0 1 1 2 3 5',
        '7 j 764',
        '11 1 DrEvil',
        '5 115',
        '1 6 5 4 2 3',
        numstr]

    out, err = p.communicate(os.linesep.join(args))
    print("exe done")
    #print(out)
    #text.close()

    '''text = open('hello.txt','r')
    solved = False
    for line in text:
        for word in line.split(" "):
            if word is "defused":
                solved = True

    if not solved:
        print("Bad result from: " + numstr)
        ret =  1
    else:
        print("==============================================")
        print(numstr + " ")
        print("==============================================")
        ret = 0
    text.close()
    return ret
    ''' 

go(200)


'''for i in range(190, 220):
    if go(i) is 0:
        print(i)
        break
    time.sleep(.4)
#print("Bad" if go(i) is 1 else "good")

'''
