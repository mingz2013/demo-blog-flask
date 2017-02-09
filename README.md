# demo.blog

用flask + sqlalchemy 开发一个简单的博客，设计要求如下

### model
- Article: id,title,content,image,create_at
- Comment: id,name,comment,create_at,article_id


### url
- /  首页，按时间显示10片
- ／1， 文章列表第2页
- ／aticle／1 ， 文章详情页, 包括文章（标题，内容，时间），评论列表
- /article/post?(id=1) 发表文章,或者编辑文章，有图片上传功能，图片要处理为宽度不超过1024px（长宽比不变）

### 前端
- 选择一个前端框架 或者用 bootstrap