import sys
from time import sleep
import winsound

inp=sys.argv
print(".")

try:
    minu=int(inp[1])
    print(".")
    if minu<0:
        print("Time should be greater than 0")
        sys.exit(1)
except ValueError:
    print("Int argument Expected")
    sys.exit(1)

if minu==1:
    wordunit='minute'
else:
    wordunit='minutes'

try:
    print("Your CountDown Starts now : ")
    for i in range(minu*60):
        j=minu*60-i
        if j<5:
            print(j,end='\r')
            sleep(1)
            winsound.Beep(500,100)
        else:
            print(j,end='\r')
            sleep(1)
    print("Finished",end='\r')
    winsound.Beep(500,400)
    for i in range(5):
        winsound.Beep(500,200)
        sleep(0.1)
        winsound.Beep(400,300)
        sleep(1)
except:
    print("Error occured")
    sys.exit(1)


