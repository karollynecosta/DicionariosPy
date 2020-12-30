# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:17:47 2020

@author: kr0l
"""
usuarios = {}
emails = ["teste@xyz.com", "bob@xyz.com"]

tupla = list(enumerate(emails))

print(tupla)

for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome: "), input("digite o nivel: ")]

for chave, dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Nível...:", chave[1])