# 雷士达项目管理系统


## 界面

### 登录（平台独立使用账号密码登录）

### 管理员/老板主界面

### 我的

### 老板查看所有项目页面

### 老板查看所有业务员页面

### 老板查看某个项目详细页面（低下可以留言）

### 单个项目的某个汇报页面

### 添加人员页面

### 销售员主界面

### 创建项目页面

### 创建项目




## 功能点设计

### 老板端
- 权限介绍：查看所有项目，删除项目，添加项目，添加业务员，删除业务员，添加项目负责人，
- 查看业务员
- 查看所有项目
- 添加业务员
- 删除业务员
- 查看业务员负责的项目（跳看项目页面按业务员搜）
- 搜索项目
- 添加项目
- 删除项目
- 查看单个项目进展
- 留言
- 查看单个汇报详情

### 销售员端
- 权限介绍：只能看自己，只能提交，不能更改，
- 创建项目
  - 提交项目
- 查看我的项目列表
  - 查看单个项目进度
  - 添加汇报
- 查看老板留言消息


## 数据库设计
### user 用户表

字段 |名称| 类型 | 备注
---|---|---|---
id|用户id | int |主键、自增
name|姓名 | varchar|
password|密码|char(20)|采用字符串+md5加密
authority|权限|char(20)|root或salesman

### project 项目表

字段 |名称| 类型 | 备注
---|---|---|---
id|项目id|int|主键、自增
name|名称|char(20)|
source|来源|char(30)|
contacts|对方联系人|char(20)|
telephone|联系电话|char(20)|
introduction|简介|char(256)|
time|创建时间|Date|自动生成
effective|是否有效|int|0有效，1失效

### report 汇报表

字段 |名称| 类型 | 备注
---|---|---|---
id|汇报表id|int|主键、自增
proid|项目id|int|外键关联项目表
reporter|汇报人|char(20)|
capital|资金明细|char(256)|
workable|落实情况|char(1024)|
invoice|开票|char(256)|
progress|进展|char(1024)|
time|汇报时间|Date|自动生成
other|其他|char(1024)|
effective|是否有效|int|0有效，1失效

### Message 留言表

字段 |名称| 类型 | 备注
---|---|---|---
id|留言id|int|主键、自增
report_id|汇报id|int|外键关联汇报表
read|是否已读|int|0未读，1已读
effective|是否有效|int|0有效，1失效
time|留言时间|Date|自动生成

### user-project用户项目表

字段 |名称| 类型 | 备注
---|---|---|---
id|用户项目id|int|主键、自增|
user_id|用户id|int|外键关联用户id
pro_id|项目id|int|外键关联项目id

### user-str 用户密文表
字段 |名称| 类型 | 备注
---|---|---|---
id|用户密文表id|int|主键自增
user_id|用户id|int|外键关联用户表
str|加密字符串|char(10)|随机生成


## 接口文档
### 登录
- url：http://LSD/login
- 请求方法：POST
- 请求参数：
  - 姓名：name(唯一)
  - 密码：password
- 返回值：
  - 成功与否：true/false
  - 身份信息：boss/salesman
- 逻辑说明：后端根据name判断属于老板或者业务员，进行相应跳转

### BOSS
### 查看业务员列表
- url: http://LSD/all-salesman/
- 请求方式：GET
- 请求参数：无
- 返回值：所有业务员的名字列表

### 查看单个业务员项目个数
- Url：/get-project-count/
- 方式：Get
- 参数：name
- 返回值：count

### 查看项目列表
- url：http://LSD/all-project/ 
- 请求方式：GET
- 请求参数：无
- 返回值：[{项目id，项目名称，项目时间，负责人[]},{……}]

### 添加业务员
- url：/add-salesman
- put
- 参数：
  - 姓名
  - 密码
- 返回值:成功与否

### 删除业务员
- url:/del-salesman
- delete
- 参数：姓名
- 返回值：成功与否

### 业务员的负责项目查询
- url: http://LSD/search-with-salesman
- 请求方式：GET
- 请求参数：
	身份标识：name
- 返回值：[{项目id，项目名称，项目时间，负责人[]},{}]


### 项目搜素
- url: http://LSD/search-projects
- 请求方式：POST
- 请求参数：
  - 关键字key
- 返回值：项目列表[]

### 添加项目
- url:/add-project
- put
- 参数：
  - 名称
  - 所属单位
  - 简介
  - 对方负责人姓名
  - 对方负责人电话
- 返回值
  - 成功与否

### 删除项目
- url：/del-project
- delete
- 参数：
  - 项目id
- 返回值：
  - 成功与否



### 查看单个项目详细信息
- url： http://LSD/single-project-detail
- 请求方式：GET
- 请求参数：
	- Project_id
- 返回值：
  - 名称
  - 所属单位
  - 简介
  - 对方负责人姓名
  - 对方负责人电话

### 查看单个项目汇报记录
- url： http://LSD/single-project-report
- 请求方式：GET
- 请求参数：
	- Project_id
- 返回值：汇报记录列表[{汇报id，名称，负责人，时间，}, {}]

### 查看单个项目老板留言
- url： http://LSD/single-project-record
- 请求方式：GET
- 请求参数：
	- Project_id
- 返回值：老板留言列表[{'留言1', 留言时间1}, '留言2', 留言时间2, ...]

### 留言
- url： http://LSD/record
- 请求方式：put
- 请求参数：
 - 项目_id
 - 留言内容
- 返回值：成功与否

### 查看单个汇报
- url：/get-report
- get
- 参数：
  - 汇报id
- 返回值
  - 项目id
  - 汇报id
  - 项目进展
  - 落实情况
  - 供货情况
  - 项目资金
  - 开票情况
  - 其它

### 添加汇报
- url：http://LSD/add-report
- 请求方式：put
- 请求参数：
  - 项目id
  - 汇报id
  - 项目进展
  - 落实情况
  - 供货情况
  - 项目资金
  -	开票情况
  -	其它
- 返回值：成功与否

### 查看老板给业务员的消息
- url:/get-ones-record
- get
- 请求参数
  - 业务员名字name
- 返回值
  - [{消息1，消息1对应的项目id},{消息2，消息2对应项目id}...]

### 更改人员权限
- url：/change-authority
- update
- 请求参数
  - 人员name
  - 权限id
- 返回值
  - 成功与否
- 说明
  - 把人的全新啊改成id