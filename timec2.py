import winreg,time
import ctypes


k32=ctypes.windll.kernel32
def debug(strr):
    s="[processes] "+strr
    k32.OutputDebugStringW(s)

def int_queryValue(rootkey,subkey,value):
    try:
        hkey=winreg.CreateKeyEx(rootkey,subkey,0,winreg.KEY_QUERY_VALUE)
        t,p=winreg.QueryValueEx(hkey,value)
        winreg.CloseKey(hkey)
        t=int.from_bytes(t,byteorder="little",signed=False)
        return t
    except Exception as e:
        #debug(str(e))
        return 0


def nowtime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def ttime(tn):
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(tn))

x=ctypes.c_ulong*256
lip=x()
czneed=ctypes.sizeof(lip)
zzx=ctypes.c_ulong
psapi=ctypes.windll.psapi
psapi.EnumProcesses(ctypes.byref(lip),czneed,ctypes.byref(zzx()))




for i in range (0,100):
    if i>5 and lip[i]==0:
        pass
    else:
        debug("pid: "+str(lip[i]))
        handle=k32.OpenProcess(1040,False,lip[i])
        lpFilename=ctypes.create_unicode_buffer(256)
        size=1024
        psapi.GetModuleFileNameExW(handle,None,lpFilename,256)
        debug(lpFilename.value)
        k32.CloseHandle(handle)

debug(nowtime())

