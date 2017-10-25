decimal = 10
result = ''
while (decimal > 0):
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
print (result)
