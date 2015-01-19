# Copyright 2013 OpenStack, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from neutronclient.common import extension


class MacAddressRangeList(extension.ClientExtensionList):
    """(Admin-only) List all MAC Address Ranges."""
    resource = "mac_address_range"
    resource_plural = "%ses" % (resource)
    resource_path = "/%s" % resource_plural
    list_columns = ["id", "cidr"]
    log = extension.NeutronClientExtension.get_logger('ListMacAddressRanges')


class RoutesList(extension.ClientExtensionList):
    """List routes all routes for a tenant."""
    resource = "routes"
    resource_path = "/%s" % resource
    list_columns = ["id", "subnet_id", "cidr", "gateway"]
    log = extension.NeutronClientExtension.get_logger('ListRoutes')


class RoutesCreate(extension.ClientExtensionCreate):
    """Create a new route for a given subnet."""
    resource = "route"
    resource_plural = "%ss" % (resource)
    resource_path = "/%s" % resource_plural
    log = extension.NeutronClientExtension.get_logger('CreateRoute')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'subnet_id', metavar='SUBNET_ID',
            help='Subnet ID to associate the route with')
        parser.add_argument(
            'cidr', metavar='CIDR',
            help='CIDR mask for the route')
        parser.add_argument(
            'gateway', metavar='GATEWAY',
            help='Destination gateway for the route')

    def args2body(self, parsed_args):
        body = {self.resource: {
            'cidr': parsed_args.cidr,
            'subnet_id': parsed_args.subnet_id,
            'gateway': parsed_args.gateway}, }
        return body


class RoutesDelete(extension.ClientExtensionDelete):
    """Deletes a route by id."""
    resource = "route"
    resource_plural = "%ss" % (resource)
    resource_path = "/%s" % resource_plural
    log = extension.NeutronClientExtension.get_logger('DeleteRoute')


class IpPolicyList(extension.ClientExtensionList):
    resource = "ip_policy"
    resource_plural = "ip_policies"
    resource_path = "/%s" % resource_plural
    list_columns = ["id", "tenant_id", "name", "subnet_ids", "network_ids",
                    "exclude"]
    log = extension.NeutronClientExtension.get_logger('ListRoutes')


class IpPolicyCreate(extension.ClientExtensionList):
    resource = "ip_policy"
    resource_plural = "ip_policies"
    resource_path = "/%s" % resource_plural
    log = extension.NeutronClientExtension.get_logger('ListRoutes')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'subnet_id', metavar='SUBNET_ID',
            help='Subnet ID to associate the route with')
        parser.add_argument(
            'cidr', metavar='CIDR',
            help='CIDR mask for the route')
        parser.add_argument(
            'gateway', metavar='GATEWAY',
            help='Destination gateway for the route')

    def args2body(self, parsed_args):
        body = {self.resource: {
            'cidr': parsed_args.cidr,
            'subnet_id': parsed_args.subnet_id,
            'gateway': parsed_args.gateway}, }
        return body


class IpPolicyDelete(extension.ClientExtensionDelete):
    """Deletes a route by id."""
    resource = "ip_policy"
    resource_plural = "ip_policies"
    resource_path = "/%s" % resource_plural
    log = extension.NeutronClientExtension.get_logger('DeleteIpPolicy')


COMMANDS = {
    "mac-range-list": MacAddressRangeList,
    "route-list": RoutesList,
    "ip-policy-list": IpPolicyList,
    "ip-policy-create": IpPolicyCreate,
    "ip-policy-delete": IpPolicyDelete,
    "route-create": RoutesCreate,
    "route-delete": RoutesDelete,
}
