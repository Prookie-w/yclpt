# yclpt
## 问题描述
因为出现了很多发布后缺陷都是因为新修改导致之前的老功能，所以想要通过页面自动化来避免这样的问题再出现
## 实现方式
选用python3+selenium+unittest来实现
## 目录介绍
base:基础的浏览器操作
tools:工具文件，如各个浏览器的driver.jar
config:配置文件
logs:日志文件
report:测试报告
page:以页面为单位维护页面元素的获取方法
service:各种业务操作
test_case:用例维护


