import sys
import os
import re
from nornir import InitNornir
from genie import testbed
from pyats import topology
from genie.conf import Genie
from pyats.topology import loader
from nornir_napalm.plugins.tasks import napalm_get
from pyats.vlan_stp_verify import verify_vlan
from nornir.core.plugins.inventory import InventoryPluginRegister
sys.path.insert(1, '../')
from inventory_script.helpers import adapt_user_password
from nornir_utils.plugins.functions import print_result 
from nornir.core.filter import F
from Nornir_Configuration.config_rollback import rollback_configuration

InventoryPluginRegister.register("user_password",adapt_user_password)

testbedfile = os.path.join('../testbed.yml')
testbed = Genie.init(testbedfile)
config_files = os.path.join('../config.yaml')
nr = InitNornir(config_files)
path = os.getcwd()

def main():
    client_core = nr.filter(F(name="sbx-n9kv-ao"))
    parser_task = client_core.run(task=verify_vlan)
    print_result(parser_task)
    config_save = client_core.run(task)
    # config_rollback = client_core.run(task=config_rollback, on_failed=True, on_good=False)


if __name__ == "__main__":
    main()
