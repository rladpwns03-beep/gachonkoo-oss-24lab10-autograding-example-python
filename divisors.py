#divisor.py by Ye Jun Kim, 202233958, rladpwns03@gachon.ac.kr

import sys
number = int(sys.argv[1])

for i in range(1,number+1):
        if number%i == 0:
                print(i, end=" ")

print()
