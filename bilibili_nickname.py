import requests
import json
import notify
import os


class BilibiliNickname:
    nicknames = []

    def __init__(self, nicknames):
        for nickname in nicknames.split(","):
            if nickname != None and nickname not in self.nicknames:
                self.nicknames.append(nickname)

    def run(self):
        for nickname in self.nicknames:
            try:
                response = requests.get(
                    "https://api.bilibili.com/x/web-interface/search/type?context=&search_type=bili_user&page=1&order=&keyword=%s&category_id=&user_type=&order_sort=&changing=mid&__refresh__=true&_extra=&highlight=1&single_column=0" % nickname)
                data = json.loads(response.content.decode("utf8"))
                if data['code'] != 0:
                    raise Exception("Api Error %s %s" %
                                    (data['code'], data['message']))
                if data['data']['numResults'] == 0:
                    print("no repeat")
                    notify.cqhttp("bilibili用户名 %s 可以注册" % (nickname))
                else:
                    print("has repeat")

            except Exception as e:
                print(e)
                pass


if __name__ == "__main__":
    b = BilibiliNickname(os.getenv("BILIBILI_NICKNAMES"))
    b.run()
