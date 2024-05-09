```
            _____            _____                                  
          /\    \          /\    \                 ______          
         /::\____\        /::\    \               |::|   |         
        /:::/    /        \:::\    \              |::|   |         
       /:::/    /          \:::\    \             |::|   |         
      /:::/    /            \:::\    \            |::|   |         
     /:::/    /              \:::\    \           |::|   |         
    /:::/    /                \:::\    \          |::|   |         
   /:::/    /                  \:::\    \         |::|   |         
  /:::/    /                    \:::\    \  ______|::|___|___ ____ 
 /:::/____/       _______________\:::\____\|:::::::::::::::::|    |
 \:::\    \       \::::::::::::::::::/    /|:::::::::::::::::|____|
 \:::\    \       \::::::::::::::::/____/  ~~~~~~|::|~~~|~~~      
  \:::\    \       \:::\~~~~\~~~~~~              |::|   |         
   \:::\    \       \:::\    \                   |::|   |         
    \:::\    \       \:::\    \                  |::|   |         
     \:::\    \       \:::\    \                 |::|   |         
      \:::\    \       \:::\    \                |::|   |         
       \:::\____\       \:::\____\               |::|   |         
        \::/    /        \::/    /               |::|___|         
         \/____/          \/____/                 ~~        
```
---
### 依赖库
* [![python][python_img_url]](http://python.org/)
* [![django][django_img_url]](http://djangoproject.com)
* [![layui][layui_img_url]](http://layui.dev)
* [![layuiadmin][layuiadmin_img_url]](https://dev.layuion.com/themes/layuiadmin/)

## 开始

这是一份在本地构建项目的指导的例子。
要获取本地副本并且配置运行，你可以按照下面的示例步骤操作。

### 依赖

你可以用pip一键安装依赖
* pip
  ```shell
  pip -r requirements.txt
  ```

### 安装

_下面是一个指导你的受众如何安装和配置你的应用的例子。这个模板不需要任何外部依赖或服务。_

1. 克隆本仓库
   ```shell
   git https://github.com/lzx9002/djangoProject.git
   ```
2. 安装 pip 包
   ```shell
   python -m pip install --upgrade pip
   ```
3. 在 `djangoProject/settings.py` 中的`ALLOWED_HOSTS`填写你的域名或ip
   ```python
   ALLOWED_HOSTS = ['127.0.0.1']
   ```

<!-- 贡献 -->
## 贡献

贡献让开源社区成为了一个非常适合学习、启发和创新的地方。你所做出的任何贡献都是**受人尊敬**的。

如果你有好的建议，请复刻（fork）本仓库并且创建一个拉取请求（pull request）。你也可以简单地创建一个议题（issue），并且添加标签「enhancement」。不要忘记给项目点一个 star！再次感谢！

1. 复刻（Fork）本项目
2. 创建你的 Feature 分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的变更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到该分支 (`git push origin feature/AmazingFeature`)
5. 创建一个拉取请求（Pull Request）

[python_img_url]:https://img.shields.io/badge/python-3.12.3-blue?logo=python
[django_img_url]:https://img.shields.io/badge/django-5.0.3-brightgreen?logo=django
[layui_img_url]:https://img.shields.io/badge/layui-2.8.5-cyan?logo=data%3Aimage%2Fx-icon%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAAAXNSR0IArs4c6QAAAxhJREFUaEPtml9IU1Ecx7%2Fn7k8uomyRbmjRiylBKAQGxcjc1B4ia2y%2B9NR7LyFkzz0K0VPvBT3U%2FAMWCF4nGVJgRBijGcR0Zn90ITgfAtvcjTPdGHP37pyzO%2B9W3sft%2FP58vr%2Ffzvnde0egctVPBKYVgktq3%2B%2F150TB2GpP3%2FX8uCT3gzo5sAVA2uvkuOMpJB7r8ddSuyxAnRxQuB0ZbBDr7iNpgGpMfke7jWoHALGPjzSazVvLBneDcHhSxe2Tht4HEK69TobcFThmsSLc0ZsOXz85pFMa4m64AWio1S5%2FNqLREEIA0c4bsJnMaYhH0U%2B4%2FyUsLmGJlkIAByWCRbevIqogBJDfRsnUFhqmRkvUUsxcFwAjf9C6AdBJ0GHArqQbgFFVEAb46fFB2h5ms1dSSaEhOMLdzO1HjuJluwcpADNrK%2Bj7MMPsQxhg2e2FVTLtCsR7LkQ7vbCZxP3oDtAffoen35eYFKyRTFhyewuu3Uhsomn6RVE%2FwgCFWigTjbUKd080ob%2BlTTVJFj%2FCALnjRH4GLIGpzb2Tp3GnubXyAJzBIaQY77DVhIj8juPCG7l8LaRVgfXkHzS%2FGisanC6Yc12Fs8YmvBmUpYV4zwS6Hf%2Fw%2BNKPSAbm3%2BPxt0UmeLqoIgCYsy2w8P8EaD1cC%2Fl8l6ZwN%2BdeI%2FgrVoq4TLZCFZjvuAa75YBmgLXEJs4wHEQZJ5lNgXULztgJAWjtQBnHKShwTg4zqUgXid6mlg2AdyfKBRiPfcWtj7NM8BUJwAPPDbDi8SNvii5pFKDG9CCjB1ru5ZmVEdqIF60CNwBL%2F%2FMOdZHLvThktgqdxlwANsmEqMr4W0gq1h1FTRQWey4AHvV5%2BljN72AkhAcLnzXbiBnAtDOvFG3KnAUsCo6ec%2BGi3SH8O2IG4FWfZvRwIQRLkTdut0%2Bd1dSkmAhMAFeOO%2FCkzcUjvm5rdQEQUV8vgsapYSQ07o6YKqBXMuXwsw9QDlV5fFb%2Fa1ZKW81vKrcrMPE8CUJ2P9%2FjqaUBawnw9t%2F4r0R2epSfzSuQWgwQkzMkGYh1%2Bwep0V%2Fbl05MPtpzbgAAAABJRU5ErkJggg%3D%3D
[layuiadmin_img_url]:https://img.shields.io/badge/layuiadmin-1.4.0-cyan?logo=data%3Aimage%2Fx-icon%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAAAXNSR0IArs4c6QAAAyRJREFUaEPtmktoE0EYx%2F%2BTmIcvWiH25N0e4kWEWpumLQh52IcHFT1IxYOoCBYpqBREPQjm0qJYipUqQZRCTRpbEw00SY1NSxHESwU9iRe92QcKmu7KpibEmN2dmWxe2j3uzvy%2F7%2Ff%2FvpkdsiGQuRqbXTEALXLPS35fEAOzM88P5sYl2Tcabc5VEKIreXLsARdn46FaaVoGoLHZJbLrlHfGbDxEUgDVmPxv65aqHQCkocG1Q2fEp%2FI2A390UsXtk6JeB%2BAvvjYzmStQs60GocDjVPR9drc2WRSgwgwgxUq8DGZClhuCCyAS9sNsNqUgvD4%2FhgaGC%2FCwsKlcAMaaTYhNjFVEFbgActsoKazC3tpRmJWcszUBKOeC1gxAOgk2lWFX0gygXFXgBng1%2FQy6tcNs5koKAuyt7czdbN29C3cHbkIA8PrNW%2FScv0ytwQ0QiwRg3GD4KxDreyEyFYDZwK%2BjOcCN%2FtuY9IeoHDSZTYiG%2FXnHLn%2F%2FBofjkKoON0C%2BFkpHo63C8UvncMYtfxyh0eEGyD5O5NpEE1iac6L3LE51yq8ZGp2iANja2iGsSktS%2FZIz4uOXzzh2%2BKSqQFEAlldW4HAfUQ0uDRj3eVFnsXBvBkUBYH0n6HQ6xGOTqZ9IPHeGMD76lApeGlQRANTZ5hn4fwLUW3diZLBf0bgLV65jLjZXiLlUc7kqEAyNonbzVsUAXxeX4O44SpWENCi9G9FsndmiXABK74C0uCCKsLUcYAZg3QCKBsCaSLYp0fl59PVepYKvSAAWeGaAmekgck7Rsk7R9vP2OgsCY94%2FdLpP9%2BDDwnvVKjAD0PQ%2F66EuPOXDFoOZ623MBGDaaEb0hU%2FVFVYAOVNoKsgEwOI%2BSx%2FL6Q4%2FeIj7I48UDaMG0Ov1iEcnqN2nBbg16MEeq5V7HVEDsLovZXTviQ8Gg14RuruzS%2FG5WhtRAdjamuC51sfkvlaDNQHgcV8rAPv%2BLiR%2F%2FJSVo6qAVskUQ2cdoBiusmhW%2F2dWibaav1SuVcDmTIIQ5Q2bpa4lGiuKYuLf%2BK9E2rC9Nuc7Qkh9iQzkDkOAi4l4yCMJ%2FAIkdDDfLJgOyQAAAABJRU5ErkJggg%3D%3D
