from ztag.transform import *
from ztag import protocols, errors

class RiakTransform(ZGrabTransform):

    name="riak/status"
    port = 8087
    protocol = protocols.RIAK
    subprotocol = protocols.RIAK.BANNER

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


