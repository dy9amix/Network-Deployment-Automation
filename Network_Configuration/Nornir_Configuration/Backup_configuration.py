import sys
import os
import re
from nornir import InitNornir
from nornir.core.plugins.inventory import InventoryPluginRegister

def backup_configuration(task):
    r = task.run(task=napalm_get, getters=["config"],retrieve='running')
    run_conf = r.result['config']['running']
  	#erase lines with "Building configuration", "Current Configuration" and "end"
    run_config = re.sub(r'Building configuration.*|Current configuration.*|end','',run_conf)
    file = open(f"/Backups/{task.host}.conf",'w')
    file.write(run_config)
    file.close()
