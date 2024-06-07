from 温度监测器_上传版 import Start
data = {
    "Name":"io1",
    "设备GPIO口":16,
    "传输地址":"http://你的IP/你的接口",
    "间隔时间":3
}
Start(data, 80)