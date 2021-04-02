import os
import sys
import pprint
from nornir_jinja2.plugins.tasks import template_file
from genie import testbed
from pyats import topology
from genie.conf import Genie
from pyats.topology import loader

testbedfile = os.path.join('../testbed.yml')
testbed = Genie.init(testbedfile)

def verify_vlan(task):
    device = testbed.devices[f'{task.host}']
    device.connect(log_stdout=False)
    output = device.parse('show vlan')
    available_vlans = output['vlans'].keys()
    configured_vlans = [10,22,35,40,44]
    result_dict ={ }
    for vlan_id in configured_vlans:
        if vlan_id in available_vlans:
            result_dict.update({f"Vlan {vlan_id} present": True})
        else:
            result_dict.update({f"Vlan {vlan_id} present": False})
    if False in result_dict.values():
        raise Exception(["Vlans not properly configured",result_dict])
    else:
        return result_dict
    