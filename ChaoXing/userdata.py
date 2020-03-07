# url改成课程首页（学习进度页面）的url
# cookies要登录后提取

class user():
    url = ''
    cookies = ''
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}