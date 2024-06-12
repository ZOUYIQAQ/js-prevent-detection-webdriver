# 这是什么?
这是一个使用js注入来防止网页检测webdriver环境的demo, 用于对抗反爬虫检测. 如淘宝对自动化引擎的检测. 
# 用了些什么?
python中的playwright库和js
# 它做了什么
使用一些代理上的技巧来使navigator.webdriver的返回值为undefined, 和使_.has(navigator, 'webdriver')的返回值为false
# 如何实现的?
1. 在网页启动时注入js脚本.
2. js为简单的代理设置, 详情看代码, 一看就懂.