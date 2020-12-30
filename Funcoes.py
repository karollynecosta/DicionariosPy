# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:56:56 2020

@author: kr0l
"""
def perguntar():
    return input("O que deseja realizar?\n" +
              "<I> - Para Inserir um usuario\n"
              "<P> - Para Pesquisar um usuario\n"
              "<E> - Para Excluir um usuario\n"
              "<L> - Para Listar um usuario: ").upper()

def inserir(dicionario):
     dicionario[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: ").upper(),
                                                     input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)
