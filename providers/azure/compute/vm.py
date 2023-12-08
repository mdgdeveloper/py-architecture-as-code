# VM Diagram provider 

from __future__ import print_function
import os
import sys

# Import GraphViz and related libraries
from graphviz import Digraph
from graphviz import Source

# Import Azure libraries
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.common.credentials import ServicePrincipalCredentials


# Define the diagram class

class VM_Diagram(object):
    def __init__(self, resource_group_name, location):
        self.resource_group_name = resource_group_name
        self.location = location

    # Create the diagram
