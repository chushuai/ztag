from ztag.transform import *
from ztag import protocols, errors

class PcworxTransform(ZGrabTransform):

    name="pcworx/status"
    port = 1962
    protocol = protocols.PCWORX
    subprotocol = protocols.PCWORX.BANNER

    def _transform_object(self, obj):
        zout = ZMapTransformOutput()
        wrapped = Transformable(obj)
        banner = wrapped['data']['pcworx']
        if not banner.resolve():
            raise errors.IgnoreObject()
        out = {
            "data": banner.resolve()
        }
        zout.transformed = out
        return zout


