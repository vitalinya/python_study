def amount(amt,rate,years):
	if years == 0:
		return round(amt,2)
	else:
		return amount(amt+rate/100*amt,rate,years-1)

amt = 10000
rate = 3.5
years = 7

print(amount(amt,rate,years))