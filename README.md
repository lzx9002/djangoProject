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
* [python](http://python.org/)
* [django](http://djangoproject.com)
* [layui](http://layui.dev)
* [layuiadmin](https://dev.layuion.com/themes/layuiadmin/)

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
