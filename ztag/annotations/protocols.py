import sys

from ztag.annotation import Annotation

from ztag import protocols

def __process(self, obj, meta):
    meta.tags.add(self.protocol.pretty_name)
    return meta

PROTOCOLS = [
    (protocols.HTTP, protocols.HTTP.GET, {"device_with_http":{"tags":["http",]}}),
    (protocols.FTP, protocols.FTP.BANNER, {"device_with_ftp":{"tags":["ftp",]}}),
    (protocols.HTTPS, protocols.HTTPS.TLS, {"device_with_https":{"tags":["https",]}}),
    (protocols.DNS, protocols.DNS.OPEN_RESOLVER, {"device_with_dns":{"tags":["dns",]}}),
    (protocols.UPNP, protocols.UPNP.DISCOVERY, {"device_with_upnp":{"tags":["upnp",]}}),
    (protocols.SSH, protocols.SSH.V2, {"device_with_ssh":{"tags":["ssh",]}}),
    (protocols.TELNET, protocols.TELNET.BANNER, {"device_with_telnet":{"tags":["telnet",]}}),
    #(protocols.NTP, protocols.NTP.TIME, {"device_with_ntp":{"tags":["ntp",]}}),
    (protocols.IMAP, protocols.IMAP.STARTTLS, {"device_with_imap":{"tags":["imap",]}}),
    (protocols.IMAPS, protocols.IMAPS.TLS, {"device_with_imaps":{"tags":["imaps",]}}),
    (protocols.POP3, protocols.POP3.STARTTLS, {"device_with_pop3":{"tags":["pop3",]}}),
    (protocols.POP3S, protocols.POP3S.TLS, {"device_with_pop3s":{"tags":["pop3s",]}}),
    (protocols.SMTP, protocols.SMTP.STARTTLS, {"device_with_smtp":{"tags":["smtp",]}}),
    (protocols.MODBUS, protocols.MODBUS.DEVICE_ID, {"schneider_nf3000":{"tags":["modbus",]}}),
    (protocols.BACNET, protocols.BACNET.DEVICE_ID, {"device_with_bacnet":{"tags":["bacnet",]}}),
    (protocols.FOX, protocols.FOX.DEVICE_ID, {"device_with_fox":{"tags":["fox",]}}),
    (protocols.DNP3, protocols.DNP3.STATUS, {"device_with_dnp3": {"tags":["dnp3",]}}),
    (protocols.S7, protocols.S7.SZL, {"device_with_s7": {"tags":["s7",]}}),
    (protocols.CWMP, protocols.CWMP.GET, {"device_with_cwmp": {"tags":["cwmp",]}}),
    (protocols.SMB, protocols.SMB.BANNER, {"device_with_smb": {"tags":["smb",]}}),
    #add by cy
    (protocols.MYSQL, protocols.MYSQL.BANNER, {"device_with_mysql": {"tags":["mysql",]}}),
    (protocols.REDIS, protocols.REDIS.BANNER, {"device_with_redis": {"tags":["redis",]}}),
    (protocols.MEMCACHE, protocols.MEMCACHE.BANNER, {"device_with_memcache": {"tags":["memcache",]}}),
    (protocols.MONGODB, protocols.MONGODB.BANNER, {"device_with_mongodb": {"tags":["mongodb",]}}),
    (protocols.CODESYS, protocols.CODESYS.BANNER, {"device_with_codesys": {"tags":["codesys",]}}),
    (protocols.RDP, protocols.RDP.BANNER, {"device_with_rdp": {"tags":["rdp",]}}),
    (protocols.AMQP, protocols.AMQP.BANNER, {"device_with_amqp": {"tags":["amqp",]}}),
    (protocols.RIAK, protocols.RIAK.BANNER, {"device_with_riak": {"tags":["riak",]}}),
    (protocols.IKE, protocols.IKE.BANNER, {"device_with_ike": {"tags":["ike",]}}),
    (protocols.PCWORX, protocols.PCWORX.BANNER, {"device_with_pcworx": {"tags":["pcworx",]}}),
    (protocols.OMRON, protocols.OMRON.BANNER, {"device_with_omron": {"tags":["omron",]}}),
    (protocols.ETHERNETIP, protocols.ETHERNETIP.BANNER, {"device_with_ethernetip": {"tags":["ethernetip",]}}),
    (protocols.PGSQL, protocols.PGSQL.BANNER, {"device_with_pgsql": {"tags":["pgsql",]}}),
    (protocols.MELSECQ, protocols.MELSECQ.BANNER, {"device_with_melsecq": {"tags":["melsecq",]}}),
    (protocols.PROCONOS, protocols.PROCONOS.BANNER, {"device_with_proconos": {"tags":["proconos",]}}),
] 

for proto, subproto, tests in PROTOCOLS:
    name = "%sAnnotation" % proto.pretty_name.upper()
    c = type(name, (Annotation,), {"process":__process})
    c.protocol = proto
    c.subprotocol = subproto
    c.tests = tests
    setattr(sys.modules[__name__], name, c)
