# ChaoXingDownloader
用来批量下载超星学习通课程页面“资料”里面的内容

# 使用
此爬虫使用scrapy编写，使用前请安装好  
在运行爬虫前务必先修改userdata.py内的内容

# 命令
在ChaoXingDownloader文件夹内运行cmd或powershell  
- scrapy crawl ziliao ： 爬取资料内所有文件  
- scrapy crawl test ： 测试userdata.py内的参数有没有设置正确，如正确，应该会显示"&lt;title&gt;学习进度页面&lt;/title&gt;"  
- scrapy crawl kejian ： 不建议使用，不完善。只能爬取首页内只有一个视频或者PPT的页面内的文件