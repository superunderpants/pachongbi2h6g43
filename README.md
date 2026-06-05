# 新能源资讯平台

基于 Django + Vue 的全栈数据采集与可视化分析平台，支持多数据源爬取、数据管理、前端展示和图表分析。

## 技术栈

**后端**
- Python 3.11+ / Django 2.0
- MySQL 5.7+
- Scrapy 爬虫框架
- Pandas 数据分析

**前端**
- Vue 2.7 + Element UI
- ECharts 数据可视化

## 功能模块

| 模块 | 说明 |
|------|------|
| 汽车信息 | 30款热门新能源车型核心参数（事故率、价格、销量、续航等） |
| 行业资讯 | 60条行业新闻资讯（车型/政策/行业/市场/国际） |
| 资讯解读 | 40篇深度分析解读 |
| 资讯分类 | 资讯分类管理 |
| 汽车之家 | 汽车之家资讯数据采集展示 |
| 系统公告 | 20条平台公告 |
| 用户管理 | 用户注册、登录、权限管理 |
| 收藏管理 | 用户收藏功能 |
| AI问答 | DeepSeek AI 智能问答 |
| 聊天模块 | WebSocket 实时聊天 |

## 快速开始

数据库已部署在远程服务器上，本地只需配置连接即可运行。

### 1. 安装环境

- 安装 [Python](https://www.python.org/downloads/)（推荐 3.11+）

### 2. 克隆项目

```bash
git clone https://github.com/superunderpants/pachongbi2h6g43.git
cd pachongbi2h6g43
```

### 3. 创建虚拟环境并安装依赖

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# 国内用户建议使用镜像加速
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 海外用户直接安装
pip install -r requirements.txt
```

### 4. 配置数据库连接

```bash
# Windows
copy config.ini.example config.ini

# Linux / Mac
cp config.ini.example config.ini
```

编辑 `config.ini`，将 `your_password_here` 替换为远程服务器的 MySQL 密码，并根据实际情况修改 `host` 和 `port`：

```ini
[sql]
type = mysql
host = <服务器IP>
port = 3306
user = root
passwd = <密码>
db = pachongbi2h6g43
charset = utf8
hasHadoop=no
```

### 5. 初始化数据库

```bash
python manage.py migrate --fake-initial
```

### 6. 启动服务

```bash
python manage.py runserver 0.0.0.0:8000
```

### 7. 访问网站

启动后会自动打开浏览器。如果没有自动打开，手动访问：

| 地址 | 说明 |
|------|------|
| http://127.0.0.1:8000/ | 前台首页 |
| http://127.0.0.1:8000/admin/ | 后台管理 |

### 8. 配置环境变量（可选）

以下配置影响邮件、支付等功能。不配置不影响基本运行。

| 变量名 | 说明 | 必填 |
|--------|------|------|
| `DJANGO_SECRET_KEY` | Django 密钥（不设置则使用默认值） | 否 |
| `EMAIL_HOST_USER` | QQ邮箱发件地址 | 否 |
| `EMAIL_HOST_PASSWORD` | QQ邮箱SMTP授权码 | 否 |
| `ALIPAY_APP_ID` | 支付宝App ID | 否 |

Windows 示例：
```cmd
set DJANGO_SECRET_KEY=your-secret-key
set EMAIL_HOST_USER=your-email@qq.com
set EMAIL_HOST_PASSWORD=your-smtp-password
```

### 登录账号

- 后台：`abo` / `abo`（如果没有，运行 `python manage.py shell -c "from django.contrib.auth.models import User;User.objects.create_superuser('abo','abo@example.com','abo')"`）
- 前台：`001` ~ `008` / `123456`

## 项目结构

```
├── dj2/                       # Django 配置
│   ├── settings.py            # 项目设置（从 config.ini 读取数据库配置）
│   ├── urls.py                # URL 路由
│   └── views.py               # 静态文件视图
├── main/                      # 主应用
│   ├── models.py              # 数据模型（20+业务模型）
│   ├── *_v.py                 # API 视图（CRUD + 统计接口）
│   ├── config_model.py        # 模型配置
│   └── migrations/            # 数据库迁移文件
├── templates/front/           # Vue 前端项目
│   ├── src/                   # 源码
│   │   ├── pages/             # 前台页面组件
│   │   ├── config/            # 配置文件
│   │   └── router/            # 路由配置
│   ├── admin/                 # 后台管理前端
│   └── dist/                  # 前端构建产物
├── spider/                    # 爬虫与数据生成
│   ├── generate_*.py          # 数据生成脚本
│   ├── crawler_standalone.py  # 独立爬虫
│   ├── batchgen.py            # 批量数据生成
│   └── Spider/                # Scrapy 爬虫（读取根目录 config.ini）
│       └── spiders/           # 爬虫定义
├── util/                      # 工具模块
├── xmiddleware/               # 中间件（认证/参数处理）
├── db/                        # 数据库备份
├── config.ini.example         # 数据库配置模板
├── requirements.txt           # Python 依赖
└── manage.py                  # Django 管理入口
```

## API 接口

详见 [API接口文档.md](API接口文档.md)

## 前端开发（可选）

修改前端代码后需要重新构建：

```bash
cd templates/front
npm install
npm run serve    # 开发模式（端口 8082）
npm run build    # 生产构建（输出到 dist/）
```

构建后將 `dist/` 目录下的 JS/CSS 文件复制到 `templates/front/js/` 和 `templates/front/css/`，并更新 `index.html` 中的资源引用。
