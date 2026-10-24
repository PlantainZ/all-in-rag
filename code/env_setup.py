"""
环境初始化模块 - 自动定位项目根目录并加载环境变量
必须在所有 HF/LangChain 相关 import 之前调用
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# 1. 定位当前文件(code/env_setup.py) -> code目录 -> all-in-rag根目录
_CODE_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _CODE_DIR.parent  # 这就是 all-in-rag/

# 2. 确保 code/ 目录在 sys.path 中，方便 C1~Cn 直接 import 本模块
if str(_CODE_DIR) not in sys.path:
    sys.path.insert(0, str(_CODE_DIR))

# 3. 加载 all-in-rag/.env
_ENV_FILE = _PROJECT_ROOT / ".env"
load_dotenv(_ENV_FILE, override=False)

# 4. 核心：将路径类变量从“相对路径”转为基于项目根目录的“绝对路径”
for key in ("HF_HOME", "SENTENCE_TRANSFORMERS_HOME"):
    val = os.environ.get(key)
    if val and not os.path.isabs(val):
        # 如果是 ./models，就会变成 E:\XXXX_CodeRepository\all-in-rag\models
        os.environ[key] = str(_PROJECT_ROOT / val)

# 解决镜像站响应慢导致的 ReadTimeoutError
# huggingface_hub 默认超时为 10s，国内镜像建议设为 60-120s
os.environ.setdefault("HF_HUB_DOWNLOAD_TIMEOUT", "120")
os.environ.setdefault("HF_HUB_ETAG_TIMEOUT", "120")

# 5. 自动创建 models 文件夹
model_dir = os.environ.get("HF_HOME")
if model_dir:
    os.makedirs(model_dir, exist_ok=True)