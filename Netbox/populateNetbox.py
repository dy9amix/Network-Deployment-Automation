from genie import testbed

testbed = testbed.load(testbed.yaml)
device = testbed.devices
connect = device.connect()
output = connect.parse('show interfaces')

print(output)