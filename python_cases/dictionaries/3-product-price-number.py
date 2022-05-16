from random import randint

products = ['milk','bread','tomato','cucumber','salt']
prices = {'milk':[70,4], 'bread':[80,2], 'tomato':[120,5], 'cucumber':[130,5], 'salt':[60,1]}
product = products[randint(0, len(products)-1)]
price = prices[product][0]
number = prices[product][1]

print (product,price,number)
