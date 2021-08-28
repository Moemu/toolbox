# 沐の工具箱

## 功能

修复由病毒引起的禁用注册表等问题（禁用注册表，任务管理器等）

快捷收集蓝屏产生的dmp文件

修复Windows Update无法更新的问题（包括但不限于重置 Windows 更新组件）

禁止Windows自动更新（切换至手动更新）

关闭Windows Defender

自动系统扫描（修复部分系统文件缺失）

获取今日Bing每日美图

获取计算机上的主题壁纸文件

激活Windows10和Office（未测试）

查询Windows激活状态和您的激活密钥

检查更新并获取最新的沐の工具箱

支持以管理员模式重启tool.py

支持退出时自动删除目录下的__pycache__文件夹（需要从程序中退出）

可修复部分运行库（dx9,vc全家桶,Microsoft.Net修复）（对Windows10可能无效）

## 使用

### 准备

Python环境（[点我跳转](www.python.org)）

安装库，或运行main.py后自动安装

```powershell
pip install pypiwin32
pip install requests
```

### 使用

下载源码后以管理员方式打开cmd，输入（路径可填，最好在源码根目录打开带管理员模式的cmd或使用cd指令）：

```powershell
py main.py
```

## 注意

请使用管理员方式运行此程序

使用本程序相关功能时，请仔细阅读对应功能所涉及到的源码，不然程序可能不能按预期工作

## 后话

许可证：[Apache-2.0 License](https://github.com/WhitemuTeam/toolbox/blob/master/LICENSE) （未经许可，严禁商用）

部分源码来源：（见源码注释）

作者：WhitemuTeam

版本：2.0（源1.6版本）
