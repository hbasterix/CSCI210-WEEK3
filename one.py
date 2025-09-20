import numpy as np
import math
def is_anagram(s:str,t:str)->bool:
    myMatrix = []
    s=s.upper()
    t=t.upper()

    strOne =""
    strTwo = ""
    strThr =""
    strFr = ""

    for  ch in s:
        if ch not in strThr:
            strThr += ch

    for  ch in t:
        if ch not in strFr:
            strFr += ch

    for ch in strThr:
        if ch.isalpha():
            strOne += ch

    
    for ch in strFr:
        if ch.isalpha():
            strTwo += ch

    for chOne in strOne:
        for chTwo in strTwo:
            if(chOne == chTwo):
                myMatrix.append(1)
            else:
                myMatrix.append(0)

    # Convert to NumPy array
    npArray = np.array(myMatrix)
    # Calculate side length for square matrix
    listLength = len(strOne)  
    # Reshape into a square matrix
    squareMatrix = npArray.reshape(listLength, listLength)
    a = abs(np.linalg.det(squareMatrix))
    return a

result = is_anagram("apple","papel")
if result == 1:
    print("Correct")
else:
    print("not correct")