#!/usr/bin/env python3 

def array_de_nomes(_batata_macarrao_chiquinha):
    lista_nome_completo = []
    for k,v in _batata_macarrao_chiquinha.items():
        lista_nome_completo.append(k.capitalize() + " " + v.capitalize())
    return lista_nome_completo

person = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_de_nomes(person))


