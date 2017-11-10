from ztag.transform import *
from ztag import protocols, errors

class MELSECQTransform(ZGrabTransform):

    name="melsecq/status"
    protocol = protocols.MELSECQ
    subprotocol = protocols.MELSECQ.BANNER

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


