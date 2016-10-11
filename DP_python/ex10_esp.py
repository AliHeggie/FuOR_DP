# Excercise 10 for FuOR tutorial 2
from __future__ import division

def recEsp(PumpProfit,PumpPower,PowerSupply):
    MaxProfit = 0
    if len(PumpProfit) <=1 and PumpPower[0]<=PowerSupply:
        MaxProfit = PumpProfit[0]
    elif len(PumpProfit) <=1 and PumpPower[0]>PowerSupply:
            MaxProfit = 0
    else:
         for p in range(len(PumpPower)):
             if PumpPower[p] <=PowerSupply:
                 remainingPumpProfit = PumpProfit
                 remainingPumpPower = PumpPower
                 remainingPowerSupply = PowerSupply - PumpPower[p]
                 del remainingPumpProfit[p]
                 del remainingPumpPower[p]
                 profit = PumpProfit[p] + recEsp(remainingPumpProfit,remainingPumpPower,remainingPowerSupply)
             else:
                profit = 0
             if profit > MaxProfit:
                MaxProfit = profit
    return MaxProfit

PumpPower = [2,3,2,4,6]
PumpProfit = [6,14,7,18,24]
PowerSupply = 8

print(recEsp(PumpProfit,PumpPower,PowerSupply))