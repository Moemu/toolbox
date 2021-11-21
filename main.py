#By WhitemuTeam
#请使用管理员方式运行此程序

try:
    from tool import *
except:
    print('您未安装部分库，现在为您安装...')
    import os
    os.system('pip install pypiwin32')
    os.system('pip install requests')
    from tool import *

ver='2.1'

memu='''
----------菜单栏----------
0.以管理员方式重启tool.py
1.常见病毒攻击修复
2.收集收集蓝屏dmp文件
3.Windows Update菜单
4.自动系统扫描
5.关闭Windows Defender
6.壁纸主题相关
7.激活相关
8.常见运行库修复
9.检查更新
10.退出(自动删除临时文件)
----------菜单栏----------
'''

if __name__=='__main__':
    print('欢迎使用沐の工具箱')
    print('版本',ver,' 作者:WhitemuTeam')
    print('使用前请确保您以管理员打开本程序，不然部分程序可能出现无法按预期运行的情况')
    print(memu)
    print('输入序号来做出你的选择吧~')
    a=input('请输入: ')
    switch={
    '0':lambda:uac(),
    '1':lambda:virus(),
    '2':lambda:dmp(),
    '3':lambda:update(),
    '4':lambda:systemcheck(),
    '5':lambda:defender(),
    '6':lambda:bizi(),
    '7':lambda:jihuo(),
    '8':lambda:runtime(),
    '9':lambda:checkupdate(ver),
    '10':lambda:dexit(),
    }
    os.system('cls')
    try:
        switch[a]()
    except KeyError:
        input('您的输入有误...')
        end()