currency = float(input('How much would you like to exchange in GBP to USD? '))
converter = currency * 1.35
print('{:.2f} British Pound Sterling worth {:.2f} American Dollar'.format(currency, converter))