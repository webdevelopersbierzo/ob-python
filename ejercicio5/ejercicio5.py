def es_bisiesto(year):
	return not year % 4 and (year % 100 or not year % 400)

print(es_bisiesto(1981))