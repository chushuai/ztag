from ztag.transform import *
from ztag import protocols, errors

class MYSQLTransform(ZGrabTransform):

    name="mysql/status"
    port = 3306
    protocol = protocols.MYSQL
    subprotocol = protocols.MYSQL.BANNER

    def _transform_object(self, obj):
        zout = ZMapTransformOutput()
        wrapped = Transformable(obj)
        banenr = wrapped['data']['banner']
        if not banenr:
            raise errors.IgnoreObject()
        out = {
            "data": banenr.resolve()
        }
        zout.transformed = out
        return zout

