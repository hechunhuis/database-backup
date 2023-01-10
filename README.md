<h1 align="center">
  <br>
  <a href="https://github.com/hechunhuis/" alt="logo" ><img src="https://github.com/hechunhuis/database-backup/blob/main/static/images/icon.png" width="150"/></a>
  <br>
  数据库备份系统
  <br>
</h1>

<h4 align="center">基于Python3开发的轻量级数据库全量备份系统</h4>

## ✨ 特性
- 支持 MySQL Oracle SQLServer PostgreSQL SQLite Hive 多种类型数据库备份
- 支持自定义cron备份规则
- 支持正则表达式匹配数据库表备份
- 支持自定义备份文件存储路径
- 支持自定义保存备份文件数量
## ⚙️ 配置
运行前需配置application.yml文件，信息如下：
注意：如果采用Docker方式启动程序，环境变量配置高于application.yml文件配置！
```yaml
database:             # 数据库配置项
  type: MySQL       # 需要备份的数据库类型：MySQL Oracle SQLServer PostgreSQL SQLite Hive
  url: 127.0.0.1    # 数据库的地址
  port: 3306        # 数据库端口
  username: root    # 数据库用户名
  password: root    # 数据库密码
  databaseName:     # 需要备份的数据库名称
  savePath:         # 备份至目标目录 例如：/mnt/dbback\
  backMax: 20       # 备份保留的最大文件数
  regEx:            # 备份符合正则表达式的表名
  cron:             # 备份的时间表达式
```
## 🛠️ 运行&部署
```shell
# 前提需要宿主机安装Python3、virtualenv以及 pip
git clone https://github.com/hechunhuis/database-backup.git
cd ./database-backup
virtualenv --python=python3
source env/bin/activate
pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
python3 main.py
```

## Docker构建
```shell
docker build -f Dockerfile -t databaseback/core:lastest
```
## Docker启动
```shell
docker run \
  --name databaseback \
  -e database.type=MySQL \
  -e database.url=127.0.0.1 \
  -e database.port=3306 \
  -e database.username=root \
  -e database.password=root \
  -e database.databaseName=tableName \
  -e database.savePath=/mnt \
  -e database.backMax=20 \
  -e database.regEx=^\w+$ \
  -e database.cron=* 2 5 4 3 \
  -d databaseback/core:lastest
```
