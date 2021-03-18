from genie import testbed
from pyats import topology
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result 
from nornir.core.filter import F

testbed = testbed.load('testbed.yaml')
nr = InitNornir("config.yaml")


def run_parsers(task):
    device = testbed.devices[f'{task.host}']
    connect = device.connect()
    output = connect.parse('show interfaces')

def main():
    nr.run(task=run_parsers)