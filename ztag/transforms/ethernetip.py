from ztag.transform import *
from ztag import protocols, errors

class EthernetipTransform(ZGrabTransform):

    name="ethernetip/status"
    port = 44818
    protocol = protocols.ETHERNETIP
    subprotocol = protocols.ETHERNETIP.BANNER

    def _transform_object(self, obj):
        zout = ZMapTransformOutput()
        wrapped = Transformable(obj)
        banner = wrapped['data']['ethernetip']
        if not banner.resolve():
            raise errors.IgnoreObject()
        out = {
            "data": banner.resolve()
        }
        zout.transformed = out
        return zout


