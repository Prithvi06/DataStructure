prices = [2,4,1,0,3,6]
'''l=[]
for i in range(len(prices)-1):
    sell_index=prices.index(max(prices[i+1:]))
    l.append(prices[sell_index]-prices[i])
if max(l) < 0:
    print(0)
else:
  print(max(l))'''
if not prices:
    print(0)

maxProfit = 0
minPurchase = prices[0]
for i in range(1, len(prices)):
    maxProfit = max(maxProfit, prices[i] - minPurchase)
    minPurchase = min(minPurchase, prices[i])
print(maxProfit)