 # -*- coding: UTF-8 -*-
#By WhitemuTeam
#如果您更新后不能打开tool.py，请至仓库页下载最新的工具箱
import os
import sys
import win32api
import win32con
import json
import requests as r
import datetime
import zipfile

def dexit():
    os.system('rd /S /Q __pycache__')
    exit()

def end():
    dir=sys.argv[0]
    run='py '+dir
    os.system('cls')
    os.system(run)

def uac():
    bat=open('UAC.bat','w')
    dir=os.path.dirname(os.path.abspath(__file__))
    ml='py '+dir+r'\main.py'+' & '+'del '+dir+r'\UAC.bat'
    print('@echo off',file=bat)
    print('if exist "%SystemRoot%\SysWOW64" path %path%;%windir%\SysNative;%SystemRoot%\SysWOW64;%~dp0',file=bat)
    print('bcdedit >nul',file=bat)
    print("if '%errorlevel%' NEQ '0' (goto UACPrompt) else (goto UACAdmin)",file=bat)
    print(':UACPrompt',file=bat)
    print('%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit',file=bat)
    print('exit /B',file=bat)
    print(':UACAdmin',file=bat)
    print(ml,file=bat)
    bat.close()
    os.system('UAC.bat&del UAC.bat')
#检查版本并更新
def checkupdate(ver):
    print('当前的版本：',ver)
    #获取最新的版本号
    try:
        url = 'https://api.github.com/repos/WhitemuTeam/toolbox/releases/latest'
        txt = r.get(url)
        open('temp.json', 'wb+').write(txt.content)
        with open('temp.json','r',encoding='utf-8') as t:
            data=t.read()
        data2 = json.loads(data)
        newver=data2['tag_name']
        print('最新的版本是:',newver)
        if newver>ver:
            print('获取压缩包...')
            zip=r.get('https://codeload.github.com/WhitemuTeam/toolbox/zip/refs/heads/main')
            zipname='temp.zip'
            open(zipname,'r').write(zip.content)
            print('解压压缩包...')
            with zipfile.ZipFile(zipname) as zf:
                zf.extractall()
            name='v'+newver
            ml='ren toolbox-main '+name
            os.system(ml)
            os.remove(zipname)
        else:
            print('您已是最新版本，不需要升级')
        os.remove('temp.json')
        input('更改已完成，按任意键返回')
        end()
    except:
        print('请检查您的网络是否可用且可以连接到Github服务器')
        input('按任意键返回')
        end()

def virus():
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
        input('更改已完成，按任意键返回')
        end()
    elif b==1:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'software\microsoft\windows\currentVersion\policies\system',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisableTaskmgr',0,win32con.REG_DWORD,0)
        input('更改已完成，按任意键返回')
        end()
    elif b==2:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'software\microsoft\windows\currentVersion\policies\system',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisableRegistryTools',0,win32con.REG_DWORD,0)
        input('更改已完成，按任意键返回')
        end()
    elif b==3:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'SOFTWARE\Policies\Microsoft\Windows\System',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisableCMD',0,win32con.REG_DWORD,0)
        input('更改已完成，按任意键返回')
        end()
    elif b==4:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\POLICIES\EXPLORER',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'RESTRICTRUN',0,win32con.REG_DWORD,0)
        input('重启你的电脑以应用更改')
        end()
    elif b==5:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'DisabledHotkeys',0,win32con.REG_SZ,'')
        input('重启你的电脑以应用更改')
        end()
    elif b==6:
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
        input('更改已完成，按任意键返回')
        end()

#收集蓝屏dmp文件（https://answers.microsoft.com/zh-hans/windows/forum/all/page-fault-in-nonpaged-area/bcb7eafc-abaf-44a3-b552-d243f1b432fa）
#你需要提前打开【控制面板】>【系统】>【高级系统设置】>【高级】>【启动和故障恢复】>【设置】>写入调试信息 > 选择【小内存转储（256KB）】>路径选择【默认】，【确定】并重启计算机
def dmp():
    os.system('copy %SystemRoot%\minidump %systemdrive%\dmp')
    print('dmp文件已存储到系统盘下的dmp文件夹中')
    b=int(input('更改已完成，按任意键返回'))
    end()

def update():
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
        end()
    elif b==2:
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
        input('更改已完成，重启你的电脑吧~')
        end()
    elif b==3:
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
        input('更改已完成，按任意键返回')
        end()

#自动系统扫描(https://answers.microsoft.com/zh-hans/windows/forum/all/%e7%97%85%e6%af%92%e4%bf%ae%e6%94%b9%e4%ba%86/b3ef7a46-1159-404a-b629-b1af9bc8d24f)
def systemcheck():
    os.system('Dism /Online /Cleanup-Image /CheckHealth')
    os.system('Dism /Online /Cleanup-Image /ScanHealth')
    os.system('Dism /Online /Cleanup-Image /RestoreHealth')
    os.system('sfc /scannow')
    print('修复完成~')
    print('如果出现“有一些文件无法修复”，请重新运行本程序')
    input('重启你的电脑吧~')
    end()

#关闭Windows Defender(https://cloud.tencent.com/developer/article/1674518)
def defender():
    key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,r'SOFTWARE\Policies\Microsoft\Windows Defender',0, win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key,'DisableAntiSpyware',0,win32con.REG_DWORD,1)
    win32api.RegCreateKey(key,'Real-Time Protection')
    key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,r'SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection',0, win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key,'DisableBehaviorMonitoring',0,win32con.REG_DWORD,1)
    win32api.RegSetValueEx(key,'DisableOnAccessProtection',0,win32con.REG_DWORD,1)
    win32api.RegSetValueEx(key,'DisableScanOnRealtimeEnable',0,win32con.REG_DWORD,1)
    key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,r'SYSTEM\CurrentControlSet\Services\SecurityHealthService',0, win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key,'Start',0,win32con.REG_DWORD,4)
    input('更改已完成，按任意键返回')
    end()

#壁纸相关
def bizi():
    print('壁纸主题相关')
    print('----------菜单栏----------')
    print('0.获取今日Bing每日美图')
    print('1.获取Windows聚焦美图')
    print('2.获取当前桌面壁纸')
    print('3.获取全部Windows10自带壁纸')
    print('4.获取主题文件（含壁纸）')
    print('----------菜单栏----------')
    print('输入序号来做出你的选择吧~')
    b=int(input('请输入: '))
    if b==0:
        print('获取今日Bing每日美图...')
        print('源码参考：WhitemuTeam/GetBingImg')
        time = datetime.datetime.now()
        realtime = time.strftime("%Y-%m-%d")
        print('今天是:',realtime)
        print('获取中...')
        img = r.get('https://bing.mcloc.cn/api')
        name = 'Bing('+realtime+').jpg'
        open(name, 'wb').write(img.content)
        input('获取成功，按任意键退出')
        end()
    if b==1:
        print('获取Windows聚焦美图')
        print('复制文件...')
        filedir=r'C:\Users\%username%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\*'
        dir=os.getcwd()
        print(dir)
        ml='cd '+dir
        os.system('md img')
        imgdir=dir+'\img'
        ml='copy '+filedir+' '+imgdir
        os.system(ml)
        print('重命名文件...')
        #遍历文件夹中的所有文件
        for file in os.listdir(imgdir):
            newname=file+'.jpg'
            new_name=file.replace(file,newname)
            #重命名
            os.renames(os.path.join(imgdir,file),os.path.join(imgdir,new_name))
        print('已完成，请到img目录下查看')
        input('按任意键返回')
        end()
    if b==2:
        print('获取当前桌面壁纸...')
        print('复制文件...')
        filedir=r'C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Themes\CachedFiles\*'
        dir=os.getcwd()
        print(dir)
        ml='cd '+dir
        os.system('md img')
        imgdir=dir+'\img'
        ml='copy '+filedir+' '+imgdir
        os.system(ml)
        print('已完成，请到img目录下查看')
        input('按任意键返回')
        end()
    if b==3:
        print('获取全部Windows10自带壁纸...')
        print('复制文件...')
        filedir=r'C:\Windows\Web'
        dir=os.getcwd()
        print(dir)
        ml='cd '+dir
        os.system('md img')
        imgdir=dir+'\img'
        ml='Xcopy '+filedir+' '+imgdir+' /E'
        os.system(ml)
        print('已完成，请到img目录下查看')
        input('按任意键返回')
        end()
    if b==4:
        print('获取主题文件...')
        print('复制文件...')
        filedir=r'C:\Users\%username%\AppData\Local\Microsoft\Windows\Themes'
        dir=os.getcwd()
        ml='cd '+dir
        os.system('md img')
        imgdir=dir+'\img'
        ml='Xcopy '+filedir+' '+imgdir+' /E'
        os.system(ml)
        print('已完成，请到img目录下查看')
        input('按任意键返回')
        end()

def jihuo():
    print('激活相关')
    print('----------菜单栏----------')
    print('1.激活Windows')
    print('2.激活Office')
    print('3.查看Windows激活情况')
    print('4.查看Windows激活密钥')
    print('----------菜单栏----------')
    print('输入序号来做出你的选择吧~')
    b=int(input('请输入: '))
    if b==1:
        #https://blog.csdn.net/syyyy712/article/details/91350308
        print('正在激活Windows...')
        os.system('slmgr.vbs /upk')
        os.system('slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
        os.system('slmgr /skms zh.us.to')
        os.system('slmgr /ato')
        print('更改完成')
        end()
    elif b==2:
        #https://www.cnblogs.com/mq0036/p/11031105.html
        path=input('请输入Office安装目录')
        ml='cd '+path
        os.system('cd')
        os.system('cscript ospp.vbs /inpkey:VYBBJ-TRJPB-QFQRF-QFT4D-H3GVB')
        os.system('cscript ospp.vbs /sethst:kms.03k.org')
        os.system('cscript ospp.vbs /act')
        os.system('cscript ospp.vbs /dstatus')
        print('更改完成')
        end()
    elif b==3:
        os.system('slmgr /dlv')
        print('请等待弹出窗口')
        end()
    elif b==4:
        key=win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform',0, win32con.KEY_ALL_ACCESS)
        keyvalue=win32api.RegQueryValueEx(key,'BackupProductKeyDefault')
        print('您的激活密钥为:',keyvalue[0])
        end()

def runtime():
    print('常见运行库修复')
    print('----------菜单栏----------')
    print('1.dx修复')
    print('2.vc全家桶修复')
    print('3.Microsoft.Net Framework修复')
    print('4.我全都要！')
    print('5.查看修复说明')
    print('----------菜单栏----------')
    print('输入序号来做出你的选择吧~')
    b=int(input('请输入:'))
    def installer(url,name):
        try:
            print('下载中....')
            exe=r.get(url)
            open(name,'wb+').write(exe.content)
            ml=name
            os.system(ml)
            print(name,'安装程序已经启动')
            input('安装结束后，按任意键继续')
            os.remove(name)
        except:
            print('请检查您是否已经联网或者是开启代理模式')
    def dx():
        installer('https://cdn.jsdelivr.net/gh/WhitemuTeam/Toolbox-online/dx/dxwebsetup.exe','dxwebsetup.exe')
    def vc():
        import platform
        ver=platform.architecture()[0]
        year=['2005','2008','2010','2012','2013','2015','2017','2019']
        if ver=='64bit':
            for i in year:
                exename='vcredist_x64_'+i+'.exe'
                url='https://cdn.jsdelivr.net/gh/WhitemuTeam/Toolbox-online/vc/64/'+exename
                installer(url,exename)
        else:
            for i in year:
                exename='vcredist_x86_'+i
                url='https://cdn.jsdelivr.net/gh/WhitemuTeam/Toolbox-online/vc/86/'+exename
                installer(url,exename)
    def net():
        installer('https://go.microsoft.com/fwlink/?linkid=2088631','4.8.exe')
    if b==1:
        dx()
    elif b==2:
        vc()
    elif b==3:
        net()
    elif b==4:
        dx()
        vc()
        net()
    elif b==5:
        txt=r.get('https://cdn.jsdelivr.net/gh/WhitemuTeam/Toolbox-online/runtime.txt')
        print(txt)
    else:
        print('您的输入有误，请重新输入...')
    end()
