# 辅助 MWeb 书写的 Alfred 3 插件

最近 Alfred 3 测试版放出，想学一下开发 Workflow 的过程，正好使用 MWeb 时遇到了些问题，在作者没有正式改进前先使用 Alfred 辅助书写。

该工具具备处理本地静态网站的相关功能。

[下载链接](https://github.com/DarryO/alfred3-mweb-workflow/raw/master/Mweb-Blog.alfredworkflow)

功能：

1. 本地预览静态博客。
>我的 MWeb 生成的文件都有@扩展属性标记，无法直接打开Chrome预览。使用该功能能够删除扩展属性，并在本地预览博客。

2. 推送至 Git 仓库。
>如果已经将静态网站生成目录设置为 Git 仓库，并配置了 ssh 免密码登录，可以使用该 Wrokflow 直接推送到远程仓库。

3. 搜索站内文章并生成跳转链接。搜索已经生成的文章(拼音搜索感谢[lxneng提供的拼音处理模块](https://github.com/lxneng/xpinyin.git))，并生成站内跳转链接。

前两个功能就不多说了。关于生成站内链接，下面补充一下3的作用：

![](http://i.imgur.com/S4ZXYAC.gif)

Alfred 通过读取 静态网站生成目录下的 archives.html，列出所有文章的名称，类别，创建时间，并通过用户输入的拼音进行搜索。

我用了Alfred 3 提供的环境变量的功能，用户在使用前需要配置一下自己的静态网站路径。

![](http://i.imgur.com/mwBmo56.png)
![](http://i.imgur.com/J0zb5Dp.png)



