from random import randint

products = ['milk','bread','tomato','cucumber','salt']
prices = {'milk':70, 'bread':80, 'tomato':120, 'cucumber':130, 'salt':60}
product = products[randint(0, len(products)-1)]
price = prices[product]

print (product,price)