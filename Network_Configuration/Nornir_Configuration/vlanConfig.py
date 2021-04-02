from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure

path = "./values/vlan_trunk_interfaces"

def configure_vlan(task):
    vlan_config = task.run(task=template_file,
                    template="vlan_config", path="./template_file/")
    task.host["template_config"] = vlan_config.result
    r = task.run(task=napalm_configure, configuration=task.host["template_config"])
    return r

def configure_vlan_access (task):
    data = task.run(
                     task=load_yaml,
              file=f'{path}.yaml'
       )
    int_config = task.run(task=template_file,
                    template="trunk_interface", path="./template_file/", interface= data.result["interface"]["access"])
    task.host["template_config"] = int_config.result
    task.run(task=napalm_configure, configuration=task.host["template_config"])

def configure_vlan_distribution (task):
    data = task.run(
                     task=load_yaml,
              file=f'{path}.yaml'
       )
    int_config = task.run(task=template_file,
                    template="trunk_interface", path="./template_file/", interface= data.result["interface"]["distribution"])
    task.host["template_config"] = int_config.result
    task.run(task=napalm_configure, configuration=task.host["template_config"])

def configure_vlan_core (task):
    data = task.run(
                     task=load_yaml,
              file=f'{path}.yaml'
       )
    int_config = task.run(task=template_file,
                    template="trunk_interface", path="./template_file/", interface= data.result["interface"]["core"])
    task.host["template_config"] = int_config.result
    task.run(task=napalm_configure, configuration=task.host["template_config"])