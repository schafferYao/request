import itchat


class WeChat(object):

    _itchat = None

    def login(self):
        itchat.auto_login()
        WeChat._itchat = itchat
        return True

    def getUserName(self):
        if WeChat._itchat == None:
            WeChat.login(self)

        nickName = input('请输入好友微信昵称:')
        UserName = WeChat._itchat.search_friends(name=nickName.strip())
        while len(UserName) == 0:
            print('该昵称好友不存在，请重新输入')
            nickName = input('请输入好友微信昵称:')
            UserName = WeChat._itchat.search_friends(name=nickName.strip())
        return UserName[0]['UserName']

    def sendMessage(self,message,userName):
        if message == '':
            return False
        if WeChat._itchat == None:
            WeChat.login(self)

        WeChat._itchat.send(message,toUserName=userName)
        return True


