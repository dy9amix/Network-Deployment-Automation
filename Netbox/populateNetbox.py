import os
import pprint
from genie import testbed
from pyats import topology
from genie.conf import Genie
from pyats.topology import loader
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result 
from nornir.core.filter import F

testbedfile = os.path.join('../testbed.yml')
testbed = Genie.init(testbedfile)
config_files = os.path.join('../config.yaml')
nr = InitNornir(config_files)


def run_parsers(task):
    device = testbed.devices[f'{task.host}']
    device.connect()
    output = device.parse('show interfaces')
    pprint(output)

def main():
    nr.run(task=run_parsers)
