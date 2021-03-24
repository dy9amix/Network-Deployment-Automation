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

InventoryPluginRegister.register("user_password",adapt_user_password)

testbedfile = os.path.join('../testbed.yml')
testbed = Genie.init(testbedfile)
config_files = os.path.join('../config.yaml')
nr = InitNornir(config_files)


def run_parsers(task):
    device = testbed.devices[f'{task.host}']
    device.connect(log_stdout=False)
    output = device.parse('show interface')
    print(output)

#Text edit
def main():
    parser_task = nr.run(task=run_parsers)
    print_result(parser_task)

if __name__ == "__main__":
    main()

