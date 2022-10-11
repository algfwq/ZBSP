import os
import platform
import hashlib as hl
import enum
import uuid



class ConnectionProtocol(enum.Enum):
    UDP=1
    TCP=2


class MyFrp():
    def __init__(self):
        print(platform.system())
        if(platform.system() == "Windows"):
            self.frpfile="frpc.exe"
            self.frpfilemd5="622f060fce624bdca9a427c3edec1663"
        elif(platform.system() == "Linux"):
            self.frpfile="frpc"
            self.frpfilemd5="2eead3e509a19002d80f48d431922f1e"

    def GetMD5(self,filepath) -> int:
        filemd5=hl.md5(open(filepath,'rb').read())
        md5code = filemd5.hexdigest()
        print(md5code)
        return md5code

    def RunFrp(self,localport:int,teleport:int,protocol=ConnectionProtocol.TCP):
        self.ptc = "tcp"
        if protocol == ConnectionProtocol.TCP:
            self.ptc="tcp"
        elif protocol == ConnectionProtocol.UDP:
            self.ptc="udp"
        if self.GetMD5(self.frpfile) != self.frpfilemd5:
            print("stop")
            return
        print(os.system("{0} tcp -i 127.0.0.1 -l {1} -n {3} -r {2} -s frp.easyfrp.top:25600 -t nfs532tc2xiuo6fw -p tcp".format(self.frpfile,localport,teleport,uuid.uuid1() )))


