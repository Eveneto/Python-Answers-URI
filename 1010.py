# -*- coding: utf-8 -*-

codeprod1, units1, price1  = input().split() 
codeprod1=int(codeprod1) 
units1=int(units1) 
price1= float(price1)
codeprod2, units2, price2  = input().split() 
codeprod2 = int(codeprod2) 
units2 = int(units2) 
price2 = float(price2)

valortotal = (price1 * units1) +  (price2 * units2)

print(f'VALOR A PAGAR: R$ {valortotal:.2f}')
