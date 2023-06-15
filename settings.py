import os

"""mysql 配置"""
MYSQL_CONFIG = {
    "maxconnections": 6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    "mincached": 2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    "maxcached": 5,  # 链接池中最多闲置的链接，0和None不限制
    "maxshared": 1,  # 链接池中最多共享的链接数量，0和None表示全部共享
    "blocking": True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    "maxusage": None,  # 一个链接最多被重复使用的次数，None表示无限制
    "ping": 1,
    "host": "example.mysql.rds.aliyuncs.com",  # 数据库域名
    "port": 3306,  # 数据库端口，默认3306
    "user": "username",  # 数据库用户名
    "password": "password",  # 数据库密码
    "database": "database",  # 数据库名称
    "charset": "utf8mb4",
}


"""redis 配置"""
REDIS_CONFIG = {
    "host": "example.redis.rds.aliyuncs.com",  # redis域名
    "port": "6379",  # redis端口，默认6379
    "password": "vYqH2Vyn8lqRmVBG",  # redis密码
    "db": 90,  # 使用的db
    "decode_responses": True,
    "health_check_interval": 30,
    "socket_connect_timeout": 5,
}
TASK_CHANNEL = "task_channel"  # 任务队列


"""日志配置"""
LOG_LEVEL = "debug"
LOG_PATH = os.path.split(os.path.realpath(__file__))[0] + "/logs/"  # 日志存储位置


"""钉钉端口异常机器人"""
ROBOT_TOKEN = "钉钉机器人token"
ROBOT_SECRET = "钉钉机器人secret"
