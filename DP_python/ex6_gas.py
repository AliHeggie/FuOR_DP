# Excercise 2 from FuOR tutorial 1
from __future__ import division

def recGas(Price,CurrentVolume,ExtractionLimit):#,CurrentInventory,InventoryCost,InventoryLimit):
    MaxProfit = 0
    if len(Price) <=1:
        MaxProfit = Price[0]*CurrentVolume
    else:
        ProfitExtractAll = Price[0]*CurrentVolume*ExtractionLimit + recGas(Price[1:],CurrentVolume-(CurrentVolume*ExtractionLimit),ExtractionLimit)
        ProfitExtractNothing = recGas(Price[1:],CurrentVolume,ExtractionLimit)
        if ProfitExtractAll < ProfitExtractNothing:
             MaxProfit = ProfitExtractNothing
        else:
             MaxProfit = ProfitExtractAll
    return MaxProfit

Price = [12,15,20,11,8]
InitalVolume = 8
ExtractionLimit = 1/2

print(recGas(Price,InitalVolume,ExtractionLimit))