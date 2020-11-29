# 종목명 얻기 
from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

name = kiwoom.GetMasterCodeName("005930")
print(name)