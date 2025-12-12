#!/usr/bin/env python3 
import sys
import re

pattern = "z"


if not len(sys.argv) > 1:
    print("none")    
else:
    result = ""
    argumento = sys.argv[1]
    if pattern in argumento:
        for item in argumento:
            letras = re.findall(pattern, item)
            for letra in letras:
                result += letra
        print(result)
    elif len(result) != 1:
        print("none")
    
