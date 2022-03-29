#def isYearLeap(year):
#
# tu código del laboratorio anterior
#    if not year %4 and (year%100 or not year %400):
#        return True
#    else:
#       return False

def daysInMonth(year, month):
    if not year %4 and (year%100 or not year %400):
       # mesAño= ["enero", "febrero","marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre","noviembre", "diciembre"]
        mesAño= [0,31,29,31,30,31,30,31,31,30,31,30,31]
        return (mesAño[month])
    else:            
        mesAño= [0,31,28,31,30,31,30,31,31,30,31,30,31]
        return (mesAño[month])


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
