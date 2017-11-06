from ztag.transform import *
from ztag import protocols, errors

class MongodbTransform(ZGrabTransform):

    name="mongodb/status"
    port = 27017
    protocol = protocols.MONGODB
    subprotocol = protocols.MONGODB.BANNER

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

