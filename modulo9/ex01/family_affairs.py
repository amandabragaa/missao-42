#!/usr/bin/env python3 

familia_dupont = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

def find_the_redheads(familia_dupont):
    
    def is_red(valor):
        if familia_dupont[valor] == "red":
            return True
        else:
            return False
        
    final = filter(is_red,familia_dupont.keys())
    final = list(final)
    return final

print(find_the_redheads(familia_dupont))    