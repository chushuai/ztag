from ztag.transform import *
from ztag import protocols, errors

class IkeTransform(ZGrabTransform):

    name="ike/status"
    port = 500
    protocol = protocols.IKE
    subprotocol = protocols.IKE.BANNER

    def _transform_object(self, obj):
        zout = ZMapTransformOutput()
        wrapped = Transformable(obj)
        banner = wrapped['data']['ike']
        if not banner.resolve():
            raise errors.IgnoreObject()
        out = {
            "data": banner.resolve()
        }
        zout.transformed = out
        return zout


