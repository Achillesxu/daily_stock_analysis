# -*- coding: utf-8 -*-
"""
@Time : 2026 3月 17 10:13
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
import requests
import json


# 使用示例
WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=666dcbbac401122d54db1ca909d062082c4cac079ca5b6fb46e99311c635cc5d"

def send_dingtalk_text(webhook_url: str, content: str, at_mobiles: list = None, at_all: bool = False):
    """
    发送文本消息
    :param webhook_url: 钉钉机器人 Webhook 地址
    :param content: 消息内容
    :param at_mobiles: 需要 @ 的手机号列表
    :param at_all: 是否 @ 所有人
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": at_mobiles or [],
            "isAtAll": at_all
        }
    }
    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    return response.json()



if __name__ == '__main__':
    result = send_dingtalk_text(WEBHOOK, "股测试，你好，这是一条测试消息", at_mobiles=['13302191383'])
    print(result)  # {'errcode': 0, 'errmsg': 'ok'}

