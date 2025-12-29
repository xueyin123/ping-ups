from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from config import settings


class PingTask:
    
    def __init__(self, interval, host_list):
        self.ping_interval = interval
        self.host_list = host_list
        self.host_status = {}

    def run(self):
        while True:
           
            time.sleep(self.ping_interval)
    
    def get_host_status(self, host):
       ping_ret = os.system(f"ping -c 1 {host}")
       return "up" if ping_ret == 0 else "down"


# 创建FastAPI应用实例
app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version
)

# 配置CORS中间件（可选）
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 基础路由
@app.get("/")
def read_root():
    return {"Hello": "World", "message": "欢迎使用FastAPI项目模板"}


@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "服务运行正常"}


# 如果直接运行此文件，则启动服务器
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "127.0.0.1")

    

    uvicorn.run(app, host=host, port=port, reload=True)