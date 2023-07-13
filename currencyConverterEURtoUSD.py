currency = float(input('How much would you like to exchange in EUR to USD? '))
converter = currency * 1.14
print('{:.2f} Euros worth {:.2f} American Dollar.'.format(currency, converter))