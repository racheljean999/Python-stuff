# Valentine's Day secret santa program woooooooooo. Get done by Feb. 7th!!!
import random

# load peeps into an array
peeps = ["Bob", "Alice", "Dan", "Billy"]

# copy array so there's 2 arrays :O
list2 = peeps.copy()

# Guess this is gonna be a loop (while arraySize2 > 0)
loopCount = 0
while len(list2) > 0:
    # pick a random number between 0 and arraySize2
    print(len(list2))
    x = random.randint(0, len(list2)-1)
    #print('x:')
    #print(x)
    # if name @ array1(loopCount) != array2 then print out pair and delete name in array2
    print(x)
    print(loopCount)

    while peeps[loopCount] == list2[x]:
        x = random.randint(0, len(list2)-1)
        print(x)
   #if peeps[loopCount] != list2[x]:
    # else:
    print(peeps[loopCount] + '->' + list2[x])
    list2.pop(x)
    loopCount = loopCount + 1
    #print('list2 length:')
    #print(len(list2))
#else pick another random num and do it again