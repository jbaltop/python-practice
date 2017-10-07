#!/usr/local/bin/python3

class Element():
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': '1'}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)