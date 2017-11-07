from ztag.transform import *
from ztag import protocols, errors

class RDPTransform(ZGrabTransform):

    name="rdp/status"
    port = 3389
    protocol = protocols.RDP
    subprotocol = protocols.RDP.BANNER

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


