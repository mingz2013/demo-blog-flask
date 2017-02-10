# demo.blog

### clone项目
`git clone https://github.com/mingz2013/demo.blog`

`cd demo.blog`

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

