# FastAPI 项目模板

这是一个基础的 FastAPI 项目模板，包含基本的配置和运行设置。

## 项目结构

```
.
├── main.py              # 主应用文件
├── run.py               # 运行脚本
├── config.py            # 配置文件
├── requirements.txt     # 项目依赖
├── .env.example         # 环境变量配置示例
└── README.md            # 项目说明
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
python main.py
```

或者使用 uvicorn:

```bash
uvicorn main:app --reload
```

### 3. 访问应用

启动后，您可以通过以下地址访问应用：

- 主页: http://127.0.0.1:8000
- 健康检查: http://127.0.0.1:8000/health
- Ping接口: http://127.0.0.1:8000/api/v1/ping
- API文档: http://127.0.0.1:8000/docs
- API红文档: http://127.0.0.1:8000/redoc

## 环境变量

- `PORT`: 指定应用运行端口，默认为 8000
- `HOST`: 指定应用运行主机，默认为 127.0.0.1

## 特性

- 基于 FastAPI 框架
- 自动API文档 (Swagger UI 和 ReDoc)
- CORS 中间件配置
- 基础健康检查接口
- 热重载开发模式