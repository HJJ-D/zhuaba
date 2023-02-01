# this is the config file for wms-backend

import os

from app.libs.logger import LogLevel

# logger
log_level = LogLevel.INFO  # log级别, 超过此级别会被记录
log_file = 'log/wms.log'

# 上传文件的存放路径
uploaded_file_save_dir = os.path.join(os.getcwd(), 'file')

# 最大请求大小
MAX_CONTENT_LENGTH = 128 * 1024 * 1024  # 128M
