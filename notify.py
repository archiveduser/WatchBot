import requests
import os
import time


def cqhttp(text):
    message = "[WatchBot通知]\n内容: %s\n时间: %s" % (
        text, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    try:
        requests.get("%s/send_private_msg?user_id=%s&message=%s" %
                     (os.getenv("CQHTTP_URL"), os.getenv("CQHTTP_TOQQ"), message))
        print("send message success")
    except Exception as e:
        print("error send notify %s" % str(e))
