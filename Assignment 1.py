''' Celsius into Farenheit '''
c = input("Please Enter Celsius:")
c = int(c)
f = (c * 9/5) + 32
print('Farenheit ',f)

''' Farenheit into Celsius '''
f = input("Please Enter Farenheit:")
f = int(f)
c = (f - 32) * 5/9
print('Celcius ',int(c))