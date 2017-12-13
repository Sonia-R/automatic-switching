import re
import telnetlib
import time

cpe_address= "C1:CF:28:A9:57:A6"
host="localhost"
prompt=">"
var=1
tel= telnetlib.Telnet(host,"9999")
time.sleep(3)
tel.write("l %s LED* \r\n"%cpe_address)
time.sleep(2)
print tel.read_very_eager()
var=1
#time.sleep(2)
while(var<=3):
        time.sleep(2)
        t=tel.write("s GET_VARS_NAME %s NAME=LED%d_lvl\r\n"%(cpe_address,var))
#       tel.read("LED%d_lvl"%var)
#if int(t)==0:
        time.sleep(2)
        tel.write("s VAR_NUMBER %s NAME=LED%d_lvl NUMBER=100\r\n"%(cpe_address,var))
        var=var+1
print tel.read_very_eager()
#if (LED%d_lvl==0): #cheking if the LED is on or not
#       time.sleep(2)
#def switch_ON(self,var):
#tel.write("s VAR_NUMBER %s NAME=LED%d_lvl NUMBER=100\r\n"%(cpe_address,var))
#tel.read_until(">")
