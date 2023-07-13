currency = float(input('How much would you like to exchange in USD to CAD? '))
converter = currency * 1.30
print('{:.2f} American Dollar worth {:.2f} Canadian Dollar.'.format(currency, converter))
