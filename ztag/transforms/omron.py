from ztag.transform import *
from ztag import protocols, errors

class OmronTransform(ZGrabTransform):

    name="omron/status"
    port = 9600
    protocol = protocols.OMRON
    subprotocol = protocols.OMRON.BANNER

    def _transform_object(self, obj):
        zout = ZMapTransformOutput()
        wrapped = Transformable(obj)
        banner = wrapped['data']['omron']
        if not banner.resolve():
            raise errors.IgnoreObject()
        out = {
            "data": banner.resolve()
        }
        zout.transformed = out
        return zout


