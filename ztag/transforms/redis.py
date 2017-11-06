from ztag.transform import *
from ztag import protocols, errors

class RedisTransform(ZGrabTransform):

    name="redis/status"
    port = 6379
    protocol = protocols.REDIS
    subprotocol = protocols.REDIS.BANNER

    def _transform_object(self, obj):
        zout = ZMapTransformOutput()
        wrapped = Transformable(obj)
        banner = wrapped['data']['banner']
        if not banner.resolve():
            raise errors.IgnoreObject()
        out = {
            "data": banner.resolve()
        }
        zout.transformed = out
        return zout
