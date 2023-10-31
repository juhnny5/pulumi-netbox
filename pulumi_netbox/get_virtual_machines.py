# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetVirtualMachinesResult',
    'AwaitableGetVirtualMachinesResult',
    'get_virtual_machines',
    'get_virtual_machines_output',
]

@pulumi.output_type
class GetVirtualMachinesResult:
    """
    A collection of values returned by getVirtualMachines.
    """
    def __init__(__self__, filters=None, id=None, limit=None, name_regex=None, vms=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if limit and not isinstance(limit, int):
            raise TypeError("Expected argument 'limit' to be a int")
        pulumi.set(__self__, "limit", limit)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if vms and not isinstance(vms, list):
            raise TypeError("Expected argument 'vms' to be a list")
        pulumi.set(__self__, "vms", vms)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetVirtualMachinesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def limit(self) -> Optional[int]:
        return pulumi.get(self, "limit")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def vms(self) -> Sequence['outputs.GetVirtualMachinesVmResult']:
        return pulumi.get(self, "vms")


class AwaitableGetVirtualMachinesResult(GetVirtualMachinesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachinesResult(
            filters=self.filters,
            id=self.id,
            limit=self.limit,
            name_regex=self.name_regex,
            vms=self.vms)


def get_virtual_machines(filters: Optional[Sequence[pulumi.InputType['GetVirtualMachinesFilterArgs']]] = None,
                         limit: Optional[int] = None,
                         name_regex: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachinesResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_netbox as netbox

    vmw_cluster01 = netbox.get_cluster(name="vmw-cluster-01")
    base_vm = netbox.get_virtual_machines(name_regex="myvm-1",
        filters=[netbox.GetVirtualMachinesFilterArgs(
            name="cluster_id",
            value=vmw_cluster01.id,
        )])
    ```
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['limit'] = limit
    __args__['nameRegex'] = name_regex
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('netbox:index/getVirtualMachines:getVirtualMachines', __args__, opts=opts, typ=GetVirtualMachinesResult).value

    return AwaitableGetVirtualMachinesResult(
        filters=__ret__.filters,
        id=__ret__.id,
        limit=__ret__.limit,
        name_regex=__ret__.name_regex,
        vms=__ret__.vms)


@_utilities.lift_output_func(get_virtual_machines)
def get_virtual_machines_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetVirtualMachinesFilterArgs']]]]] = None,
                                limit: Optional[pulumi.Input[Optional[int]]] = None,
                                name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachinesResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_netbox as netbox

    vmw_cluster01 = netbox.get_cluster(name="vmw-cluster-01")
    base_vm = netbox.get_virtual_machines(name_regex="myvm-1",
        filters=[netbox.GetVirtualMachinesFilterArgs(
            name="cluster_id",
            value=vmw_cluster01.id,
        )])
    ```
    """
    ...