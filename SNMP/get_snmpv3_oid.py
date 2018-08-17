import sys
sys.path.append('/path/to/snmp_helper.py')
import snmp_helper


if True:
    ip_arista = '10.1.255.110'
    ip_cisco = '10.1.255.109'
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)
    rtr_arista = (ip_arista, 161)
    rtr_cisco = (ip_cisco, 161)

snmp_oids = (
    ('sysName', '1.3.6.1.2.1.1.1.0', None),
    ('sysUptime', '1.3.6.1.2.1.1.3.0', None),
    ('ifDescr.2', '1.3.6.1.2.1.2.2.1.2.2', None),
    ('ifInOctets.2', '1.3.6.1.2.1.2.2.1.10.2', True),
    ('ifUcastPkts.2', '1.3.6.1.2.1.2.2.1.11.2', True),
    ('ifOutOctets.2', '1.3.6.1.2.1.2.2.1.16.2', True),
    ('ifOutUcastPkts.2', '1.3.6.1.2.1.2.2.1.17.2', True)
)

for desc, oid, is_count in snmp_oids:
    snmp_data = snmp_helper.snmp_get_oid_v3(
        rtr_arista, snmp_user, oid=oid)
    output = snmp_helper.snmp_extract(snmp_data)
    print("{}: {}".format(desc, output))
