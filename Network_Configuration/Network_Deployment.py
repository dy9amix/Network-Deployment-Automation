import pprint
import os
import sys
import pprint
from nornir.core.plugins.inventory import InventoryPluginRegister
sys.path.insert(1, '../')
from inventory_script.helpers import adapt_user_password
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result 
from nornir.core.filter import F
from netbox import NetBox