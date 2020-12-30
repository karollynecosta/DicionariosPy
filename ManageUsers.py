# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:48:18 2020

@author: kr0l
"""
from Funcoes import perguntar, inserir, pesquisar, excluir, listar
usuarios={}

opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    if opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()