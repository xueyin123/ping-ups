"""
FastAPI项目配置文件
"""
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 应用配置
    app_title: str = "FastAPI 项目模板"
    app_description: str = "一个基础的FastAPI项目模板"
    app_version: str = "1.0.0"
    
    # 服务器配置
    host: str = os.getenv("HOST", "127.0.0.1")
    port: int = int(os.getenv("PORT", 8000))
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # CORS配置
    allow_origins: list = ["*"]  # 在生产环境中应更具体地指定允许的源
    
    class Config:
        env_file = ".env"


# 创建全局配置实例
settings = Settings()