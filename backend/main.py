from fastapi import FastAPI
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware
# 配置日志记录器，定义日志格式 时间文件行号 日志级别 日志内容
logger.add(
    "app.log",  # 日志文件路径
    format="{time:YYYY-MM-DD HH:mm:ss} {file}:{line} {level} {message}",  # 日志格式
    level="INFO",  # 日志级别 
)

# 创建 FastAPI 应用实例
app = FastAPI()

# 凡是前后端不在同一个端口或域名的，需添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义一个根路径的 GET 请求处理函数
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 定义一个带有路径参数的 GET 请求处理函数
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 定义一个 POST 请求处理函数，接收 JSON 数据
# 修改返回值，使其直接返回接收到的 text 字段
# 修改后函数，返回接收到的 text 字段
@app.post("/items/")
def create_item(item: dict):
    logger.info(f"Received item: {item}")
    return item



def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10001)

if __name__ == "__main__":
    main()