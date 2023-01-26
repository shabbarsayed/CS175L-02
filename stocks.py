#Shabbar Sayed
#CS175L 02
#stocks

Commission_Rate = float(input('Please enter the commission rate as percent (Ex: 0.05): '))
Num_Shares = int(input('Please enter the number of shares: '))
Purchase_Price = float(input('Please enter purchase price (Ex: 35.00): '))
Selling_Price = float(input('Please enter selling price (Ex: 37.50): '))

amountPaidForStock = Num_Shares * Purchase_Price
purchaseCommission = Commission_Rate * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = Num_Shares * Selling_Price
sellingCommission = Commission_Rate * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid

print(' ')
print(f'Amount paid for stock: ${amountPaidForStock:,.2f}')
print(f'Commission paid on the purchase: ${purchaseCommission:,.2f}')
print(f'Amount the stock sold for: ${stockSoldFor:,.2f}')
print(f'Commission paid on the sale: ${sellingCommission:,.2f}')
print(f'Profit (or loss if negative): ${profitOrLoss:,.2f}')
