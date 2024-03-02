# ESP32_ESP8266_MicroPython
大量ESP32、ESP8266代码，人工智能代码，全是MicroPython，下载烧录后，按示意图连线，激活设备即可使用，激活一次永久使用，无需网络，也可以建立自己的工厂！
激活价格基本在 1-200元 不等，根据功能复杂程度而定，给想批量制造但不想写代码的人一个创业和尝试的机会！

# 使用方法：
- 1、首先下载对应系统的固件，安装Thonny进行烧录。
- 2、分别将base.data、microdot.mpy、main.py，还有你要用的模块的mpy上传到你烧录好的板子里。
- 3、将main.py里的模块名改为你用的模块名，每个模块都有调用说明，请参照详细文档调用Start传入对应参数即可。
- 4、首次启动是AP热点模式，手机搜索名为“ESP32配网”的wifi，连入
- 5、打开浏览器，输入“192.168.4.1”进入配网界面，输入wifi名称和密码，不支持5Gwifi网络。
- 6、配网成功后，界面掉线，在Thonny中可以看到连接的内网IP，打开浏览器进入该地址打开设备界面（有些模块有，有些没有）
- 7、Wifi连接成功后，根据Thonny中的提示进行设备激活即可，激活后，重启设备即可正常使用
- 8、激活前，必须有网络！
- 8、激活后，无网络也可以使用！
- 9、激活即绑定设备，重新烧录后，同一个设备无需再次付费重新激活，所以不用担心烧录导致的文件丢失而多次付费，不存在这个问题，考出的mpy文件别的未激活设备无法使用
- [设备激活地址](http://invasion.x3322.net:82/BindMachine/)

# ESP32、ESP32-C3(4M)
- [测试体验](https://github.com/dhrdzy/ESP32_ESP8266_MicroPython/raw/main/验证激活)
- [无存储录音笔，笔丢数据不丢](https://github.com/dhrdzy/ESP32_ESP8266_MicroPython/tree/main/无存储录音笔)
- [4足机器人（开发中）]
- [6足机器人（开发中）]

# ESP8266
