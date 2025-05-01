from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis

def create_limiter(app, redis_host='localhost', redis_port=6379, redis_db=0):
    # Redis client
    redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

    # Create limiter instance
    limiter = Limiter(
        key_func=get_remote_address,
        storage_uri=f"redis://{redis_host}:{redis_port}/{redis_db}"
    )
    limiter.init_app(app)

    return limiter
