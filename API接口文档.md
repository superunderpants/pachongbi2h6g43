# API 接口文档

> 项目: pachongbi2h6g43 | 后端: Django 2.0 + Python 3.7 | 数据库: MySQL 5.7
>
> Base URL: `http://localhost:8080/pachongbi2h6g43`

---

## 认证说明

- 后台管理员账号: `admin / admin`
- 前台用户自行注册（`/yonghu/register`），默认密码 `123456`
- **所有 POST 请求**（除 login/register/upload）需要在 HTTP Header 中携带 `token: <token值>`
- 登录接口返回的 JSON 中包含 `token` 字段，后续请求放入 Header 即可
- GET 请求部分接口免认证（如 `list`、`config/list`、`news/list` 等）

---

## 1. 通用 CRUD 接口

以下 11 张表均自动生成这些接口（将 `{table}` 替换为表名）：

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/{table}/page` | 分页列表（后台） | 是 |
| GET | `/{table}/list` | 列表 | 否 |
| GET | `/{table}/lists` | 列表（变体） | 否 |
| POST | `/{table}/query` | 单条查询 | 否 |
| POST | `/{table}/save` | 新增（后台） | 是 |
| POST | `/{table}/add` | 新增（前台） | 视表而定 |
| GET | `/{table}/info/<id>` | 详情（后台） | 是 |
| GET | `/{table}/detail/<id>` | 详情（前台） | 否 |
| POST | `/{table}/update` | 更新 | 是 |
| POST | `/{table}/delete` | 批量删除 | 是 |
| GET | `/{table}/default` | 默认项 | 否 |
| POST | `/{table}/autoSort` | 智能排序 | 否 |
| POST | `/{table}/autoSort2` | 智能排序2 | 否 |
| POST | `/{table}/importExcel` | Excel导入 | 是 |
| GET/POST | `/{table}/thumbsup/<id>` | 点赞/踩 | 否 |
| GET/POST | `/{table}/vote/<id>` | 投票 | 否 |

11 张表:

| 表名 | 中文名 | 说明 |
|------|--------|------|
| `autohome` | 新能源资讯 | 爬虫数据 |
| `xingyezixun` | 行业资讯 | 行业资讯 |
| `zixunfenlei` | 资讯分类 | 资讯分类 |
| `zixunjiedu` | 资讯解读 | 资讯解读 |
| `news` | 系统公告 | 系统公告 |
| `chat` | AI问答 | 用户提问/AI回复 |
| `storeup` | 收藏表 | 用户收藏 |
| `yonghu` | 用户 | 前台用户 |
| `users` | 管理员 | 后台管理员 |
| `discussautohome` | 新能源资讯评论 | autohome评论 |
| `discussxingyezixun` | 行业资讯评论 | xingyezixun评论 |

---

## 2. Config 配置表

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/config/page` | 分页列表 | 是 |
| GET | `/config/list` | 列表 | 否 |
| POST | `/config/save` | 新增 | 是 |
| POST | `/config/add` | 新增（前台） | 否 |
| GET | `/config/info/<id>` | 详情 | 是 |
| GET | `/config/info` | 详情（无参） | 是 |
| GET | `/config/detail/<id>` | 详情（前台） | 否 |
| POST | `/config/update` | 更新 | 是 |
| POST | `/config/delete` | 删除 | 是 |

---

## 3. 用户认证接口

### 3.1 管理员 (users)

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/users/login` | 登录（返回token） | 否 |
| POST | `/users/register` | 注册 | 否 |
| GET/POST | `/users/logout` | 登出 | 否 |
| POST | `/users/resetPass` | 重置密码（需传username） | 是 |
| GET | `/users/session` | 获取当前用户信息 | 是 |
| POST | `/users/security` | 密保查询 | 否 |

### 3.2 前台用户 (yonghu)

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/yonghu/login` | 登录（返回token） | 否 |
| POST | `/yonghu/register` | 注册 | 否 |
| GET/POST | `/yonghu/logout` | 登出 | 否 |
| POST | `/yonghu/resetPass` | 重置密码 | 是 |
| GET | `/yonghu/session` | 获取当前用户信息 | 是 |

---

## 4. 扩展接口（按表）

### 4.1 autohome（新能源资讯）

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | `/autohome/count` | 计数 | 否 |
| GET | `/autohome/group/<columnName>` | 按列分组统计 | 否 |
| GET | `/autohome/value/<xCol>/<yCol>` | 按列值统计 | 否 |
| GET | `/autohome/value/<xCol>/<yCol>/<timeStatType>` | 按时间统计（日/月/年） | 否 |
| GET | `/autohome/valueMul/<xCol>` | 多值统计 | 否 |
| GET | `/autohome/valueMul/<xCol>/<timeStatType>` | 多值时间统计 | 否 |
| GET | `/autohome/cleanse` | 数据清洗 | 否 |

### 4.2 xingyezixun（行业资讯）

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | `/xingyezixun/count` | 计数 | 否 |
| GET | `/xingyezixun/group/<columnName>` | 按列分组统计 | 否 |
| GET | `/xingyezixun/value/<xCol>/<yCol>` | 按列值统计 | 否 |
| GET | `/xingyezixun/value/<xCol>/<yCol>/<timeStatType>` | 按时间统计 | 否 |
| GET | `/xingyezixun/valueMul/<xCol>` | 多值统计 | 否 |
| GET | `/xingyezixun/valueMul/<xCol>/<timeStatType>` | 多值时间统计 | 否 |

### 4.3 zixunjiedu（资讯解读）

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/zixunjiedu/shBatch` | 批量审核 | 是 |

### 4.4 chat（AI问答）

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/chat/security` | 密保接口 | 否 |

### 4.5 storeup（收藏）

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/storeup/security` | 密保接口 | 否 |

### 4.6 users（管理员扩展）

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/users/security` | 密保接口 | 否 |

### 4.7 discussautohome / discussxingyezixun

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/discussautohome/security` | 密保接口 | 否 |
| POST | `/discussxingyezixun/security` | 密保接口 | 否 |

---

## 5. 特殊功能接口

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | `/baike/<name>` | 百度百科查询 | 否 |
| GET | `/comment/list` | 用户评论列表 | 是 |
| GET | `/location` | 定位（百度地图） | 否 |
| GET | `/option/<tableName>/<columnName>` | 获取某表某列的去重值 | 否 |
| GET | `/cal/<tableName>/<columnName>` | 计算（sum/max/min/avg） | 否 |
| GET | `/follow/<tableName>/<columnName>` | 根据字段值查单行 | 否 |
| GET | `/follow/<tableName>/<columnName>/<level>/<parent>` | 级联查询 | 否 |
| GET | `/group/<tableName>/<columnName>` | 按列分组统计（通用） | 否 |
| GET | `/value/<tableName>/<xCol>/<yCol>` | 按列值统计（通用） | 否 |
| GET | `/value/<tableName>/<xCol>/<yCol>/<timeStatType>` | 按时间统计（通用） | 否 |
| POST | `/sh/<tableName>` | 审核开关（切换sfsh状态） | 是 |
| POST | `/spider/<tableName>` | 触发爬虫（同步阻塞） | 是 |
| POST | `/deepseek/askai` | DeepSeek AI问答 | 否 |
| POST | `/deepseek/askai/stream` | DeepSeek AI流式问答 | 否 |
| GET | `/ws` | WebSocket连接 | 否 |

---

## 6. 文件接口

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/file/upload` | 文件上传 | 否 |
| GET | `/file/download?fileName=xxx` | 文件下载 | 否 |
| POST | `/file/encrypt` | 文件加密 | 否 |
| POST | `/file/decrypt` | 文件解密 | 否 |
| GET | `/upload/<fileName>` | 直接访问上传文件 | 否 |
| GET | `/upload/<tableName>/<fileName>` | 按表访问上传文件 | 否 |

---

## 7. 其他

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | `/shive/analyze` | Hive分析 | 是 |
| POST | `/matchFace` | 百度人脸识别比对 | 否 |

---

## 8. 前端页面路由

| 路径 | 说明 |
|------|------|
| `/pachongbi2h6g43/admin/` | 后台管理页面 |
| `/pachongbi2h6g43/index.html` | 前台首页 |
| `/pachongbi2h6g43/front/` | 前台页面 |

> **接口总计: ~385个**（11张表 x 16通用接口 ≈ 176个 + 扩展接口 ~60个 + 前端页面路由 + admin静态资源路由）

---

## 9. 测试结果

> 测试时间: 2026-06-03 | 总计: 62个接口 | 通过: 56 | 已知问题: 5 | 跳过: 1

### 通过 (56个)

认证登录（users/yonghu login/logout/session）、Config CRUD、所有11张表的 page/list/info/detail/count/group、百度百科、评论列表、字段选项(option)、计算(cal)、通用统计(group/value/follow)、审核(sh)、点赞(thumbsup)、投票(vote)、评论(discuss分页/列表)、chat/storeup/zixunjiedu 分页列表、文件接口异常处理、DeepSeek异常处理、定位异常处理、后台页面

### 已知问题 (5个)

| 端点 | 现象 | 原因 |
|------|------|------|
| `GET /location` | 返回 `定位失败` | 百度地图 API Key 过期或 API 地址变更，已添加 try/except 兜底 |
| `POST /deepseek/askai` | 返回 `DeepSeek API Key未配置` | config 表中未配置 DeepSeek 的 API Key |
| `POST /deepseek/askai/stream` | 同上 | 同上 |
| `GET /ws` | 500 WebSocket握手失败 | 仅支持 WebSocket 连接，HTTP GET 无法访问 |
| `GET /index.html` | 404 | 前端首页模板 `templates/front/index.html` 不存在 |

### 跳过 (1个)

| 端点 | 原因 |
|------|------|
| `POST /spider/<name>` | 同步阻塞，`os.system()` 调用 Scrapy 爬虫耗时数秒至数十分钟 |

### 本次修复 (4个)

| 端点 | 修复内容 |
|------|----------|
| `POST /users/resetPass` | 添加空参数校验 + username参数验证 + 修复列名匹配逻辑（`username_str` 默认值从值改为 `"username"`） |
| `GET /file/download` | 添加 `fileName` 参数校验 + 文件存在性检查，分别返回 400/404 |
| `GET /location` | 添加 try/except 包裹 geocoding 调用，API异常时返回错误信息而非 500 |
| `POST /deepseek/askai` | 添加 DeepSeek config 存在性检查，未配置时返回 400 而非 500 |
| `POST /deepseek/askai/stream` | 同上 |
