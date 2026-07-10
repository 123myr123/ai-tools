import datetime
import platform

print(platform.system())
local_now = datetime.datetime.now()
print(local_now.strftime("%d/%m/%Y, %H:%M:%S"))