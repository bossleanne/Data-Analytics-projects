# from wxpy import *
# import itchat
#
# #初始化
# bot = Bot()
import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

itchat.auto_login()
itchat.run()
