# Excercise 2 from FuOR tutorial 1

def recPumps(Demands,ProductionCosts,Penalty,CurrentInventory):#,CurrentInventory,InventoryCost,InventoryLimit):
    mincost = Penalty
    if len(Demands) <=1:
        if Demands[0]-CurrentInventory < len(ProductionCosts):
            mincost = ProductionCosts[Demands[0]-CurrentInventory]
    else:
        for p in range(len(ProductionCosts)):
            cost = ProductionCosts[p] + recPumps(Demands[1:],ProductionCosts,Penalty,max(CurrentInventory+p-Demands[0],0))
            if CurrentInventory + p < Demands[0]:
                cost += Penalty
            if cost < mincost:
                mincost = cost
    return mincost

CurrentInventory = 0
Demands = [1,3,2,1]
#Demands = [1,1,2,3,4,1,3,4,5,1,4,5] #This breaks the program as the size of the problem explodes
ProductionCosts = [0,1,3,6,12]
Penalty = 999

print(recPumps(Demands,ProductionCosts,Penalty,CurrentInventory))

