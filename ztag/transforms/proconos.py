from ztag.transform import *
from ztag import protocols, errors

class PROCONOSTransform(ZGrabTransform):

    name="proconos/status"
    port = 20547
    protocol = protocols.PROCONOS
    subprotocol = protocols.PROCONOS.BANNER

    def _transform_object(self, obj):
        zout = ZMapTransformOutput()
        wrapped = Transformable(obj)
        banner = wrapped['data']['proconos']
        if not banner.resolve():
            raise errors.IgnoreObject()
        out = {
            "data": banner.resolve()
        }
        zout.transformed = out
        return zout


