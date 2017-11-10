from ztag.transform import *
from ztag import protocols, errors

class PGSQLTransform(ZGrabTransform):

    name="pgsql/status"
    port = 5432
    protocol = protocols.PGSQL
    subprotocol = protocols.PGSQL.BANNER

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


