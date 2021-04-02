import pprint
import os
import sys
import pprint
from nornir.core.plugins.inventory import InventoryPluginRegister
sys.path.insert(1, '../')
from inventory_script.helpers import adapt_user_password
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from Nornir_Configuration.vlanConfig import configure_vlan
from Nornir_Configuration.Backup_configuration import backup_configuration
from nornir.core.filter import F

InventoryPluginRegister.register("user_password",adapt_user_password)
config_files = os.path.join('../config.yaml')
nr = InitNornir(config_files)


def main():
    client_access_devices = nr.filter(F(device_role__name="Access"))
    client_distribution_devices = nr.filter(F(device_role__name="Distribution"))
    client_core_devices = nr.filter(F(device_role__name="Core"))
    access_task = client_access_devices.run(task=backup_configuration)
    distribution_task=client_distribution_devices.run(task=backup_configuration)
    core_task=client_core_devices.run(task=backup_configuration)

    access_task = client_access_devices.run(task=configure_vlan)
    print_result(access_task)
    distribution_task=client_distribution_devices.run(task=configure_vlan)
    print_result(distribution_task)
    core_task=client_core_devices.run(task=configure_vlan)
    print_result(core_task)

if __name__ == "__main__":
    main()
