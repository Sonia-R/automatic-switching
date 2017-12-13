import re
import telnetlib
import time

cpe_address= "C1:CF:28:A9:57:A6" #the address of CPE used
host="localhost"
prompt=">"
var=1
tel= telnetlib.Telnet(host,"9999") #connection to telnet
#time.sleep(3)
#tel.write("l %s LED* \r\n"%cpe_address)
time.sleep(2)
#print tel.read_very_eager()
var=1
while(var<3):
time.sleep(2)
t=tel.write("s GET_VARS_NAME %s NAME=LED%d_lvl\r\n"%(cpe_address,var))
time.sleep(2)
#else:
#       tel.write("s VAR_NUMBER %s NAME=LED%d_lvl NUMBER=100\r\n"%(cpe_address,var))
output =tel.read_very_eager()
time.sleep(2)
value=re.search=('(?<==)', ('LED%d')%var)
time.sleep(2)
value.group(0)
time.sleep(2)
print value(0)
if value==0: #cheking if LED value is 0 #switched_off
        tel.write("s VAR_NUMBER %s NAME=LED%d_lvl NUMBER=100\r\n"%(cpe_address,var)) #turn the LED on
 else:
        tel.write("s VAR_NUMBER %s NAME=LED%d_lvl NUMBER=0\r\n"%(cpe_address,var))
var=var+1
#def switch_ON(self,var):
#tel.write("s VAR_NUMBER %s NAME=LED%d_lvl NUMBER=100\r\n"%(cpe_address,var))
#tel.read_until(">")
