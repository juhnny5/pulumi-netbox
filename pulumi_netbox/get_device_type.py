# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetDeviceTypeResult',
    'AwaitableGetDeviceTypeResult',
    'get_device_type',
    'get_device_type_output',
]

@pulumi.output_type
class GetDeviceTypeResult:
    """
    A collection of values returned by getDeviceType.
    """
    def __init__(__self__, id=None, is_full_depth=None, manufacturer=None, manufacturer_id=None, model=None, part_number=None, slug=None, u_height=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_full_depth and not isinstance(is_full_depth, bool):
            raise TypeError("Expected argument 'is_full_depth' to be a bool")
        pulumi.set(__self__, "is_full_depth", is_full_depth)
        if manufacturer and not isinstance(manufacturer, str):
            raise TypeError("Expected argument 'manufacturer' to be a str")
        pulumi.set(__self__, "manufacturer", manufacturer)
        if manufacturer_id and not isinstance(manufacturer_id, int):
            raise TypeError("Expected argument 'manufacturer_id' to be a int")
        pulumi.set(__self__, "manufacturer_id", manufacturer_id)
        if model and not isinstance(model, str):
            raise TypeError("Expected argument 'model' to be a str")
        pulumi.set(__self__, "model", model)
        if part_number and not isinstance(part_number, str):
            raise TypeError("Expected argument 'part_number' to be a str")
        pulumi.set(__self__, "part_number", part_number)
        if slug and not isinstance(slug, str):
            raise TypeError("Expected argument 'slug' to be a str")
        pulumi.set(__self__, "slug", slug)
        if u_height and not isinstance(u_height, int):
            raise TypeError("Expected argument 'u_height' to be a int")
        pulumi.set(__self__, "u_height", u_height)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isFullDepth")
    def is_full_depth(self) -> bool:
        return pulumi.get(self, "is_full_depth")

    @property
    @pulumi.getter
    def manufacturer(self) -> Optional[str]:
        return pulumi.get(self, "manufacturer")

    @property
    @pulumi.getter(name="manufacturerId")
    def manufacturer_id(self) -> int:
        return pulumi.get(self, "manufacturer_id")

    @property
    @pulumi.getter
    def model(self) -> Optional[str]:
        return pulumi.get(self, "model")

    @property
    @pulumi.getter(name="partNumber")
    def part_number(self) -> Optional[str]:
        return pulumi.get(self, "part_number")

    @property
    @pulumi.getter
    def slug(self) -> Optional[str]:
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter(name="uHeight")
    def u_height(self) -> int:
        return pulumi.get(self, "u_height")


class AwaitableGetDeviceTypeResult(GetDeviceTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeviceTypeResult(
            id=self.id,
            is_full_depth=self.is_full_depth,
            manufacturer=self.manufacturer,
            manufacturer_id=self.manufacturer_id,
            model=self.model,
            part_number=self.part_number,
            slug=self.slug,
            u_height=self.u_height)


def get_device_type(manufacturer: Optional[str] = None,
                    model: Optional[str] = None,
                    part_number: Optional[str] = None,
                    slug: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeviceTypeResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_netbox as netbox

    ex1 = netbox.get_device_type(model="7210 SAS-Sx 10/100GE")
    ex2 = netbox.get_device_type(slug="7210-sas-sx-10-100GE")
    ex3 = netbox.get_device_type(manufacturer="Nokia",
        part_number="3HE11597AARB01")
    ```
    """
    __args__ = dict()
    __args__['manufacturer'] = manufacturer
    __args__['model'] = model
    __args__['partNumber'] = part_number
    __args__['slug'] = slug
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('netbox:index/getDeviceType:getDeviceType', __args__, opts=opts, typ=GetDeviceTypeResult).value

    return AwaitableGetDeviceTypeResult(
        id=__ret__.id,
        is_full_depth=__ret__.is_full_depth,
        manufacturer=__ret__.manufacturer,
        manufacturer_id=__ret__.manufacturer_id,
        model=__ret__.model,
        part_number=__ret__.part_number,
        slug=__ret__.slug,
        u_height=__ret__.u_height)


@_utilities.lift_output_func(get_device_type)
def get_device_type_output(manufacturer: Optional[pulumi.Input[Optional[str]]] = None,
                           model: Optional[pulumi.Input[Optional[str]]] = None,
                           part_number: Optional[pulumi.Input[Optional[str]]] = None,
                           slug: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeviceTypeResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_netbox as netbox

    ex1 = netbox.get_device_type(model="7210 SAS-Sx 10/100GE")
    ex2 = netbox.get_device_type(slug="7210-sas-sx-10-100GE")
    ex3 = netbox.get_device_type(manufacturer="Nokia",
        part_number="3HE11597AARB01")
    ```
    """
    ...
