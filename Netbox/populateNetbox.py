from genie import testbed
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result 
from nornir.core.filter import F

testbed = testbed.load(testbed)
nr = InitNornir("config.yaml")


def run_parsers(task):
    device = testbed.devices[f'{task.host}']
    connect = device.connect()
    output = connect.parse('show interfaces')

def main():
    nr.run(task=run_parsers)