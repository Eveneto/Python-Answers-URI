# -*- coding: utf-8 -*-


nome = input()
salario = float(input())
vendas = float(input()) 

salariofinal = salario + (vendas * 15/100) 

print(f'TOTAL = R$ {salariofinal:.2f}')
