from ztag.transform import *
from ztag import protocols, errors

class MemcacheTransform(ZGrabTransform):

    name="memcache/status"
    port = 11211
    protocol = protocols.MEMCACHE
    subprotocol = protocols.MEMCACHE.BANNER

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
