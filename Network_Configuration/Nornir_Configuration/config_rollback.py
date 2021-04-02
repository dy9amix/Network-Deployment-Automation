from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure

def rollback_configuration(task):
    task.run(task=napalm_configure, configuration=f'/Backups/{task.host}.conf',replace=True)


