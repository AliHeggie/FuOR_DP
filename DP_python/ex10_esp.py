# Excercise 10 for FuOR tutorial 2
from __future__ import division

def recEsp(PumpProfit,PumpPower,PowerSupply):
    MaxProfit = 0
    if len(PumpProfit) <=1 and PumpPower[0]<=PowerSupply:
        MaxProfit = PumpProfit[0]
    elif len(PumpProfit) <=1 and PumpPower[0]>PowerSupply:
            MaxProfit = 0
    else:

         if PowerSupply>= PumpPower[0]:
             profitTakePump  = PumpProfit[0] + recEsp(PumpProfit[1:len(PumpProfit)],PumpPower[1:len(PumpPower)],PowerSupply-PumpPower[0])
             profitLeavePump = recEsp(PumpProfit[1:len(PumpProfit)],PumpPower[1:len(PumpPower)],PowerSupply)
             MaxProfit = max(profitLeavePump,profitTakePump)
         else:
             MaxProfit = recEsp(PumpProfit[1:len(PumpProfit)],PumpPower[1:len(PumpPower)],PowerSupply)
    return MaxProfit

PumpPower = [2,3,2,4,6]
PumpProfit = [6,14,7,18,24]
PowerSupply = 8

print(recEsp(PumpProfit,PumpPower,PowerSupply))