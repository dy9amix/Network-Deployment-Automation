from netbox import NetBox

token = '0123456789abcdef0123456789abcdef01234567'
host = '34.74.171.83'
port = 8000

netbox = NetBox(host=host, port=port, auth_token=token,use_ssl=False)
def create_device():
    for i in range(6 , 11):
        netbox.dcim.create_device(name=f'SW-{i}',device_role='Access',site_name='Client-2',device_type='ios',platform=1)

def create_interface():
    for i in range(3, 11):
        netbox.dcim.create_interface(name='Management',interface_type= '1000base-t',device_id=i) 

def create_management_IP():
    for i in range(4,11):
        netbox.ipam.create_ip_address(address=f'172.16.16.{i}/16',device=i ,assigned_object_type='dcim.interface' ,assigned_object_id=i, assigned_object=i)

print(netbox.dcim.get_devices(name='SW-3')[0]['id'])