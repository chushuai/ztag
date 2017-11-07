from ztag.transform import *
from ztag import protocols, errors

class AMQPTransform(ZGrabTransform):

    name="amqp/status"
    port = 5672
    protocol = protocols.AMQP
    subprotocol = protocols.AMQP.BANNER

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


