# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 上午9:30
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : get_phone_msg.py
# @Software: PyCharm

from apptoolkit import Device

android_devices = Device.get_android_devices()
ios_devices = Device().get_ios_devices()

print(android_devices[0].get('model'))
print(ios_devices)
