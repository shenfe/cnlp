# cnlp

## Commands

### virtualenv

```bash
$ pip install virtualenv
$ virtualenv --no-site-packages venv
$ source venv/Scripts/activate # 进入venv环境
(venv) $ pip install -r requirements.txt # 安装依赖
(venv) $ pip install scipy # 安装一个包
(venv) $ pip freeze > requirements.txt # 保存安装包清单
(venv) $ deactivate # 退出venv环境
```

