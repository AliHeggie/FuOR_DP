# Excercise 2 from FuOR tutorial 1

def recPumps(Demands,ProductionCosts):#,CurrentInventory,InventoryCost,InventoryLimit):
   if len(Demands) <=1:
        cost = ProductionCosts[Demands[0]]
   return cost


print(recPumps([2],[0,1,3,5]))