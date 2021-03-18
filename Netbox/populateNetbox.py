import os
from genie import testbed
from pyats import topology
from pyats.topology import loader
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result 
from nornir.core.filter import F

testbedfile = (os.getcwd()+'/testbed.yaml')
testbed = topology.loader.load(testbedfile)
nr = InitNornir("config.yaml")


def run_parsers(task):
    device = testbed.devices[f'{task.host}']
    connect = device.connect()
    output = connect.parse('show interfaces')

def main():
    nr.run(task=run_parsers)