import sys
import os
import re
from nornir import InitNornir
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir_napalm.plugins.tasks import napalm_get


def backup_configuration(task):
    r = task.run(task=napalm_get, getters=["config"],retrieve='running')
    run_conf = r.result['config']['running']
  	#erase lines with "Building configuration", "Current Configuration" and "end"
    run_config = re.sub(r'Building configuration.*|Current configuration.*|end','',run_conf)
    filepath = f"/Backups/{task.host}.conf"
    pathfile = os.getcwd()+filepath
    f = open(pathfile,"w+")
    f.write(run_config)
    f.close()
    return "Backup successfully taken"
