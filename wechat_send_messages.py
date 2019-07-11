#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:59:22 2019

@author: alexliu
"""


import requests
import itchat

import itchat



def SentChatRoomsMsg(name, context):
    itchat.get_chatrooms(update=True)
    iRoom = itchat.search_chatrooms(name)
    print(iRoom)
    for room in iRoom:
        if room['NickName'] == name:
            userName = room['UserName']
            print("--------=======--------"+userName)
            break
    itchat.send_msg(context, userName)
    print("发送到：" + name + "\n"
                          "发送内容：" + context + "\n")
    print("*********************************************************************************")


def loginCallback():
    print("***登录成功***")


def exitCallback():
    print("***已退出***")



itchat.auto_login(hotReload=True, enableCmdQR=2, loginCallback=loginCallback, exitCallback=exitCallback)


wechat_name_list = ["wechat1_name","wechat2_name","wechat3_name"]
context = '''This is for context'''

for i in range(0, len(wechat_name_list)):
    name = wechat_name_list[i]
    context = context
    print("----------------第 "+str(i+1)+" 次---------------")
    print(name,context)
    SentChatRoomsMsg(name,context)






