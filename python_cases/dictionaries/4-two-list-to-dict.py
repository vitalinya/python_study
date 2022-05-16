from random import randint

products = ['milk','bread','tomato','cucumber','salt']

prices = [70, 80, 120, 130, 60]

dict = { products[x]:prices[x] for x in range(len(prices)) }

print (dict)