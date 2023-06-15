import json
import traceback

from redis.client import Redis
from redis.connection import ConnectionPool

from settings import REDIS_CONFIG


class RedisClient:
    """redis客户端连接"""

    @classmethod
    def get_redis_conn(cls, retry_times=3, config=REDIS_CONFIG):
        """获取redis连接"""
        for _ in range(retry_times):
            try:
                pool = ConnectionPool(**config)
                redis = Redis(connection_pool=pool)
                redis.ping()
            except TimeoutError:
                if _ < retry_times - 1:
                    continue
                raise Exception(traceback.format_exc())
            else:
                return redis

    @classmethod
    def get_queue(cls, channel: str):
        return cls.get_redis_conn().rpop(channel)

    @classmethod
    def push_queue(cls, channel: str, data: dict):
        return cls.get_redis_conn().lpush(channel, json.dumps(data))

    @classmethod
    def set_string(cls, key: str, data: dict):
        return cls.get_redis_conn().set(key, json.dumps(data))

    @classmethod
    def get_string(cls, key: str, name: str):
        return cls.get_redis_conn().get(name + str(key))

    @classmethod
    def del_string(cls, key):
        return cls.get_redis_conn().delete(str(key))

    @classmethod
    def get_keys(cls, key):
        return cls.get_redis_conn().keys(str(key))
