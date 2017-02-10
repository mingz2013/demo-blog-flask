# demo.blog


### 创建所需目录

`mkdir -p /home/apps/`

### clone项目

`cd /home/apps/`

`git clone https://github.com/mingz2013/demo.blog`

`cd demo.blog`

### 创建所需目录
`mkdir logs`

### install nodejs库

`cd app/static/articles/`

`npm install`

`cd ../../..`

### install python库

`pip install flask flask-sqlalchemy redis uwsgi`


### 初始化redis

`sh scripts/init_redis.sh`

### 初始化数据库

`sh scripts/init_db.sh`

### 运行测试环境

`sh scripts/run_test.sh`


### 运行uwsgi

`sh scripts/run_uwsgi.sh`


---

### TODOLIST


优化

- 编辑框加载过慢,压缩前端代码
- css样式优化
- 图片大小处理
- 安全加固
- 标题唯一限制
- ...