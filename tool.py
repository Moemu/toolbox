#By WhitemuTeam
#请使用管理员方式运行此程序
import os
import win32api
import win32con

ver='1.2'

print('欢迎使用沐の工具箱')
print('版本',ver,' 作者:WhitemuTeam')
print('使用前请确保您以管理员打开本程序，不然部分程序可能出现无法按预期运行的情况')
print('----------菜单栏----------')
print('1.常见病毒攻击修复')
print('2.收集收集蓝屏dmp文件')
print('3.Windows Update菜单')
print('4.自动系统扫描')
print('5.关闭Windows Defender')
print('0.检查更新')
print('----------菜单栏----------')
print('输入序号来做出你的选择吧~')
a=int(input('请输入: '))

#检查版本并更新
if a==0:
    print('当前的版本：',ver)
    #获取最新的版本号
    import requests
    url = 'https://cdn.jsdelivr.net/gh/WhitemuTeam/toolbox/ver.txt'
    txt = requests.get(url)
    open('temp.txt', 'wb').write(txt.content)
    with open("temp.txt", "r") as f:  # 打开文件
        newver = f.read()  # 读取文件
    print('最新的版本是:',newver)
    if newver==ver:
        print('您已是最新版本，不需要升级')
    else:
        #更新tool.py
        url = 'https://cdn.jsdelivr.net/gh/WhitemuTeam/toolbox/tool.py'
        newpy = requests.get(url)
        newname = 'tool(v'+newver+').py'
        open(newname, 'wb').write(newpy.content)
        print('已下载新版本，名称为：',newname)
        #更新ver.txt
        newvertxt=open('ver.txt','w')
        print(newver,file=newvertxt)
        print('更新ver.txt完成')
        #更新readme.md
        url = 'https://cdn.jsdelivr.net/gh/WhitemuTeam/toolbox/readme.md'
        newmd = requests.get(url)
        open('readme.md', 'wb').write(newmd.content)
        print('更新readme.md完成')
        print('更新完成')
    os.remove('temp.txt')
    input('按任意键退出')
if a==1:
    print('选项：常见病毒修复')
    print('----------菜单栏----------')
    print('0.显示被隐藏的关机，重启等按钮')
    print('1.启用任务管理器')
    print('2.启用注册表')
    print('3.启用cmd')
    print('4.启用组策略')
    print('5.启用Win快捷键')
    print('6.我全都要！(不需要重启系统)')
    print('----------菜单栏----------')
    print('输入序号来做出你的选择吧~')
    b=int(input('请输入: '))
    if b==0:
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\current\device\Start',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'HideShutdown',0,win32con.REG_SZ,'0')
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HideSleep',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HideSignOut',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HideShutDown',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HideRestart',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HidePowerButton',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HideLock',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        input('按任意键退出')
    if b==1:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'software\microsoft\windows\currentVersion\policies\system',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisableTaskmgr',0,win32con.REG_DWORD,0)
        input('按任意键退出')
    if b==2:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'software\microsoft\windows\currentVersion\policies\system',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisableRegistryTools',0,win32con.REG_DWORD,0)
        input('按任意键退出')
    if b==3:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'SOFTWARE\Policies\Microsoft\Windows\System',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisableCMD',0,win32con.REG_DWORD,0)
        input('按任意键退出')
    if b==4:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\POLICIES\EXPLORER',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'RESTRICTRUN',0,win32con.REG_DWORD,0)
        input('重启你的电脑以应用更改')
    if b==5:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisabledHotkeys',0,win32con.REG_SZ,'')
        input('重启你的电脑以应用更改')
    if b==6:
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\current\device\Start',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'HideShutdown',0,win32con.REG_SZ,'0')
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HideSleep',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HideSignOut',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HideShutDown',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HideRestart',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HidePowerButton',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\PolicyManager\default\Start\HideLock',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'value',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'software\microsoft\windows\currentVersion\policies\system',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisableTaskmgr',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'software\microsoft\windows\currentVersion\policies\system',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisableRegistryTools',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'SOFTWARE\Policies\Microsoft\Windows\System',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisableCMD',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\POLICIES\EXPLORER',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'RESTRICTRUN',0,win32con.REG_DWORD,0)
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisabledHotkeys',0,win32con.REG_SZ,'')
        os.system('taskkill /IM explorer.exe')
        os.system('explorer.exe')
        input('按任意键退出')

#收集蓝屏dmp文件（https://answers.microsoft.com/zh-hans/windows/forum/all/page-fault-in-nonpaged-area/bcb7eafc-abaf-44a3-b552-d243f1b432fa）
#你需要提前打开【控制面板】>【系统】>【高级系统设置】>【高级】>【启动和故障恢复】>【设置】>写入调试信息 > 选择【小内存转储（256KB）】>路径选择【默认】，【确定】并重启计算机
if a==2:
    os.system('copy %SystemRoot%\minidump %systemdrive%\dmp')
    print('dmp文件已存储到系统盘下的dmp文件夹中')
    b=int(input('按任意键退出'))

if a==3:
    print('Windows Update菜单')
    print('----------菜单栏----------')
    print('1.修复Windows10无法更新的问题')
    print('2.重置Windows Update组件')
    print('3.关闭自动更新（切换为手动更新）')
    print('----------菜单栏----------')
    print('输入序号来做出你的选择吧~')
    b=int(input('请输入:'))
    if b==1:
        #修复Windows10无法更新的问题（https://answers.microsoft.com/zh-hans/insider/forum/all/windows10/58bca578-56ff-4323-88db-ab36fb7ebd0d/https://answers.microsoft.com/zh-hans/insider/forum/all/windows%e6%97%a0%e6%b3%95%e8%8e%b7%e5%8f%96/8f36b349-b22f-42f8-bfe5-87d5b86c79c9）
        #你也可以尝试Run FIx It: https://aka.ms/wudiag 
        #你也可以尝试屏蔽某些更新：https://www.majorgeeks.com/files/details/microsoft_show_or_hide_updates_troubleshooter.html (https://answers.microsoft.com/zh-hans/windows/forum/all/windows%e6%9b%b4%e6%96%b00x800f0990%e6%8a%a5/c8e5508d-3930-4036-a28d-d098b664e992)
        os.system('SC config wuauserv start= auto')
        os.system('SC config bits start= auto')
        os.system('SC config cryptsvc start= auto')
        os.system('SC config trustedinstaller start= auto')
        os.system('SC config wuauserv type=share')
        os.system('net stop wuauserv')
        os.system('net stop cryptSvc')
        os.system('net stop bits')
        os.system('net stop msiserver')
        os.system('ren C:\Windows\SoftwareDistribution SoftwareDistribution.old')
        os.system('ren C:\Windows\System32\catroot2 catroot2.oldold')
        os.system('net start wuauserv')
        os.system('net start cryptSvc')
        os.system('net start bits')
        os.system('net start msiserver')
        os.system('netsh winsock reset')
        input('请重启你的Windows然后再次尝试更新吧~')
    if b==2:
        #重置 Windows 更新组件（https://docs.microsoft.com/zh-cn/windows/deployment/update/windows-update-resources）
        #停止相关服务
        os.system('net stop bits')
        os.system('net stop wuauserv')
        os.system('net stop cryptsvc')
        #删除 qmgr*.dat 文件
        os.system(r'Del "%ALLUSERSPROFILE%\Application Data\Microsoft\Network\Downloader\qmgr*.dat"')
        #重新注册 BITS 文件和 Windows 更新 文件
        os.system('cd /d %windir%\system32')
        os.system('regsvr32.exe /s atl.dll')
        os.system('regsvr32.exe /s urlmon.dll')
        os.system('regsvr32.exe /s mshtml.dll')
        os.system('regsvr32.exe /s shdocvw.dll')
        os.system('regsvr32.exe /s browseui.dll')
        os.system('regsvr32.exe /s jscript.dll')
        os.system('regsvr32.exe /s vbscript.dll')
        os.system('regsvr32.exe /s scrrun.dll')
        os.system('regsvr32.exe /s msxml.dll')
        os.system('regsvr32.exe /s msxml3.dll')
        os.system('regsvr32.exe /s msxml6.dll')
        os.system('regsvr32.exe /s actxprxy.dll')
        os.system('regsvr32.exe /s softpub.dll')
        os.system('regsvr32.exe /s wintrust.dll')
        os.system('regsvr32.exe /s dssenh.dll')
        os.system('regsvr32.exe /s rsaenh.dll')
        os.system('regsvr32.exe /s gpkcsp.dll')
        os.system('regsvr32.exe /s sccbase.dll')
        os.system('regsvr32.exe /s slbcsp.dll')
        os.system('regsvr32.exe /s cryptdlg.dll')
        os.system('regsvr32.exe /s oleaut32.dll')
        os.system('regsvr32.exe /s ole32.dll')
        os.system('regsvr32.exe /s shell32.dll')
        os.system('regsvr32.exe /s initpki.dll')
        os.system('regsvr32.exe /s wuapi.dll')
        os.system('regsvr32.exe /s wuaueng.dll')
        os.system('regsvr32.exe /s wuaueng1.dll')
        os.system('regsvr32.exe /s wucltui.dll')
        os.system('regsvr32.exe /s wups.dll')
        os.system('regsvr32.exe /s wups2.dll')
        os.system('regsvr32.exe /s wuweb.dll')
        os.system('regsvr32.exe /s qmgr.dll')
        os.system('regsvr32.exe /s qmgrprxy.dll')
        os.system('regsvr32.exe /s wucltux.dll')
        os.system('regsvr32.exe /s muweb.dll')
        os.system('regsvr32.exe /s wuwebv.dll')
        #重置 Winsock
        os.system('netsh winsock reset')
        #重启相关服务
        os.system('net start bits')
        os.system('net start wuauserv')
        os.system('net start cryptsvc')
        input('重启你的电脑吧~')
    if b==3:
        #停止并禁用Windows Update服务
        #os.system('net stop wuauserv')
        #os.system('sc config wuauserv start=disabled')
        #注册表修改(https://zhuanlan.zhihu.com/p/116531539)
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,r'SOFTWARE\Policies\Microsoft\Windows',0, win32con.KEY_ALL_ACCESS)
        win32api.RegCreateKey(key,'WindowsUpdate')
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate',0, win32con.KEY_ALL_ACCESS)
        win32api.RegCreateKey(key,'AU')
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'AUOptions',0,win32con.REG_DWORD,2) #通知下载和自动安装
        win32api.RegSetValueEx(key,'NoAutoUpdate',0,win32con.REG_DWORD,1) #禁止自动更新
        input('按任意键退出')

#自动系统扫描(https://answers.microsoft.com/zh-hans/windows/forum/all/%e7%97%85%e6%af%92%e4%bf%ae%e6%94%b9%e4%ba%86/b3ef7a46-1159-404a-b629-b1af9bc8d24f)
if a==4:
    os.system('Dism /Online /Cleanup-Image /CheckHealth')
    os.system('Dism /Online /Cleanup-Image /ScanHealth')
    os.system('Dism /Online /Cleanup-Image /RestoreHealth')
    os.system('sfc /scannow')
    print('如果出现”有一些文件无法修复“，请重新运行本程序')
    input('重启你的电脑吧~')

#关闭Windows Defender(https://cloud.tencent.com/developer/article/1674518)
if a==5:
    key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,r'SOFTWARE\Policies\Microsoft\Windows Defender',0, win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key,'DisableAntiSpyware',0,win32con.REG_DWORD,1)
    key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,r'SYSTEM\CurrentControlSet\Services\SecurityHealthService',0, win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key,'Start',0,win32con.REG_DWORD,4)
    input('按任意键退出')