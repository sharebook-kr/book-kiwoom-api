# 상장일 
from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

상장일 = kiwoom.GetMasterListedStockDate("005930")
print(상장일)
print(type(상장일)) 
