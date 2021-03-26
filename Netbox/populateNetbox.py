import pprint
import os
import sys
import pprint
from genie import testbed
from pyats import topology
from genie.conf import Genie
from pyats.topology import loader
from nornir.core.plugins.inventory import InventoryPluginRegister
sys.path.insert(1, '../')
from inventory_script.helpers import adapt_user_password
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result 
from nornir.core.filter import F
from netbox import NetBox

InventoryPluginRegister.register("user_password",adapt_user_password)

testbedfile = os.path.join('../testbed.yml')
testbed = Genie.init(testbedfile)
config_files = os.path.join('../config.yaml')
nr = InitNornir(config_files)
token = '0123456789abcdef0123456789abcdef01234567'
host = '34.74.171.83'
port = 8000
netbox = NetBox(host=host, port=port, auth_token=token,use_ssl=False)


def run_parsers(task):
    device = testbed.devices[f'{task.host}']
    device.connect(log_stdout=False)
    output = device.parse('show interface')
    device_id = netbox.dcim.get_devices(name=f'{task.host}')[0]['id']
    result_arr = []
    for i in output.keys():
        netbox.dcim.create_interface(name=f'{i}',interface_type= '1000base-t',device_id=device_id)
        result_arr.append(f'{i} sucessfully uploaded to NetBox \n')
    return result_arr
     

#Text edit
def main():
    client_core = nr.filter(F(device_role__name="Core"))
    parser_task = client_core.run(task=run_parsers)
    print_result(parser_task)

if __name__ == "__main__":
    main()

