from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure

def configure_mst (task,root_bridge):
    if root_bridge == True:
        int_config = task.run(task=template_file,
                template="mst_distribution", path="./template_file/")
        task.host["template_config"] = int_config.result
        task.run(task=napalm_configure, configuration=task.host["template_config"])
    else:
        int_config = task.run(task=template_file,
                        template="mst", path="./template_file/")
        task.host["template_config"] = int_config.result
        task.run(task=napalm_configure, configuration=task.host["template_config"])

def configure_rapid_pvst(task):
    int_config = task.run(task=template_file,
                template="rapid_pvst", path="./template_file/")
    task.host["template_config"] = int_config.result
    task.run(task=napalm_configure, configuration=task.host["template_config"])
    