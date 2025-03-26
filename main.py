from fastapi import FastAPI
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware

# 创建 FastAPI 应用实例
app = FastAPI()

# 添加CORS中间件
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

@app.options("/items/")
def options_items():
    logger.info("Received OPTIONS request")
    return {}