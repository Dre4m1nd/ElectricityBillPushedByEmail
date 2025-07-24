import logging
from logging.handlers import TimedRotatingFileHandler


def get_logger(name="app"):
    """获取全局日志器，确保所有文件使用同一配置"""
    # 避免重复添加处理器
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    # 设置总日志级别
    logger.setLevel(logging.DEBUG)

    # 日志格式（包含时间、级别、模块、内容）
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 1. 文件处理器：按天分割日志，保留7天
    file_handler = TimedRotatingFileHandler(
        "app.log",
        when="midnight",
        interval=1,
        backupCount=7,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)  # 文件日志记录INFO及以上
    file_handler.setFormatter(formatter)

    # 2. 控制台处理器：输出到屏幕
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # 控制台显示DEBUG及以上
    console_handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# 创建全局日志实例（供其他文件直接导入）
logger = get_logger()