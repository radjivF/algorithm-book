def coinChange(centsNeeded, coinValues):
   minCoins = [[0 for j in range(centsNeeded + 1)]
               for i in range(len(coinValues))]
   minCoins[0] = range(centsNeeded + 1)

   for i in range(1,len(coinValues)):
      for j in range(0, centsNeeded + 1):
         if j < coinValues[i]:
            minCoins[i][j] = minCoins[i-1][j]
         else:
            minCoins[i][j] = min(minCoins[i-1][j],
             1 + minCoins[i][j-coinValues[i]])

   return minCoins[-1][-1]
