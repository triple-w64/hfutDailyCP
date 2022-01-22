<div align="center">
<h1 align="center">HFUT今日校园自动签到</h1>
<img src="https://img.shields.io/github/issues/choya-lee/hfutDailyCP?color=green">
<img src="https://img.shields.io/github/stars/choya-lee/hfutDailyCP?color=yellow">
<img src="https://img.shields.io/github/forks/choya-lee/hfutDailyCP?color=orange">
<img src="https://img.shields.io/github/license/choya-lee/hfutDailyCP?color=ff69b4">

<blockquote data-tool="科技兽" style="border-top: none;border-right: none;border-bottom: none;font-size: 0.9em;background: url(https://figurebed-iseex.oss-cn-hangzhou.aliyuncs.com/img/20210519013028.png) 10px 10px / 40px no-repeat rgb(31,79,107);overflow: auto;color: inherit;border-left: 0px;padding: 1.2em 2em;margin-bottom: 2em;margin-top: 2em;text-align: center;border-radius: 10px;"><p style="font-family: Optima-Regular, Optima, PingFangSC-light, PingFangTC-light, &quot;PingFang SC&quot;, Cambria, Cochin, Georgia, Times, &quot;Times New Roman&quot;, serif;text-align: justify;line-height: 26px;margin-top: 1em;margin-bottom: 0.3em;font-size: 14px;color: rgb(255, 255, 38);"><strong style="color: #fc8705;">使用必读：</strong><br>1.本项目仅适用于合肥工业大学的今日校园打卡<br>2.以下账号、密码即新信息门户的账号(学号)和密码<br><strong style="color: #fc8705;">声明：</strong><br>1.此脚本仅供学习交流，禁止盈利和商用<br>2.脚本使用过程中，若存在瞒报误报所造成的损失由使用者个人承担<br></p></blockquote>

---

### 使用说明

- 右上角fork本仓库


<p align="center">
    <img alt="Git" src="img/fork.png" >
</p>
- 
  点击导航栏Action，启用workflow


![action](E:\Code_files\GitPro\hfutDailyCP\img\action.png)

​	[下图采用其他仓库做演示]

![workflow](img\workflow.png)



- 点击setting -> secret -> 新建一个secret

![secret](img\secret.png)

- 在`name`栏中填`INFO`，`value`中填入`账号`和`密码`，用空格隔开<img src="E:\Code_files\GitPro\hfutDailyCP\img\info.png"/>


---

### 补充

1. 支持多人打卡，只要以空格隔开，格式形如"账号1 密码1 账号2 密码2 ...账号n 密码n"
2. 脚本在每天14：30左右自动签到，也可以自行更改签到时间
3. 若脚本无法运行，请检查action中workflow是否启用
4. 如有其他问题，请反馈至[邮箱](lzyfrwk@163.com)

