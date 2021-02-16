from wxpy import *
import time


# Author Admin6016 @Github
class WX:
    bot = 0
    name = 0

    def login(self):
        self.bot = Bot()


if __name__ == '__main__':
    bot = Bot()
    print('账号', bot.self.nick_name, '登录成功，共有', len(bot.friends()), '位好友')
    for i in bot.friends():
        time.sleep(1.5)
        try:
            m = i.send_raw_msg(
                # 名片的原始消息类型
                raw_type=42,
                # 注意 `username` 在这里为不存在的微信 ID，这样发送的名片消息会被屏蔽达到静默发送
                raw_content='<msg username="dfsfsfccd3432" nickname="清理僵尸粉"/>'
            )
            print('好友', i.nick_name, '检测完成')
        except:
            print('好友', i.nick_name, '检测失败')

    print('好友列表僵尸粉检测完毕，请返回聊天界面即可查看。')
