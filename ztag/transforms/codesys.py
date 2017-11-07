from ztag.transform import *
from ztag import protocols, errors

class CodesysTransform(ZGrabTransform):

    name="codesys/status"
    port = 2455
    protocol = protocols.CODESYS
    subprotocol = protocols.CODESYS.BANNER

    def _transform_object(self, obj):
        zout = ZMapTransformOutput()
        wrapped = Transformable(obj)
        banner = wrapped['data']["codesys"]
        if not banner.resolve():
            raise errors.IgnoreObject()
        out = {
            "data": banner.resolve()
        }
        zout.transformed = out
        return zout

