# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DeviceRoleArgs', 'DeviceRole']

@pulumi.input_type
class DeviceRoleArgs:
    def __init__(__self__, *,
                 color_hex: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 vm_role: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a DeviceRole resource.
        """
        pulumi.set(__self__, "color_hex", color_hex)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if vm_role is not None:
            pulumi.set(__self__, "vm_role", vm_role)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> pulumi.Input[str]:
        return pulumi.get(self, "color_hex")

    @color_hex.setter
    def color_hex(self, value: pulumi.Input[str]):
        pulumi.set(self, "color_hex", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter(name="vmRole")
    def vm_role(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "vm_role")

    @vm_role.setter
    def vm_role(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "vm_role", value)


@pulumi.input_type
class _DeviceRoleState:
    def __init__(__self__, *,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 vm_role: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering DeviceRole resources.
        """
        if color_hex is not None:
            pulumi.set(__self__, "color_hex", color_hex)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if vm_role is not None:
            pulumi.set(__self__, "vm_role", vm_role)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "color_hex")

    @color_hex.setter
    def color_hex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "color_hex", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter(name="vmRole")
    def vm_role(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "vm_role")

    @vm_role.setter
    def vm_role(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "vm_role", value)


class DeviceRole(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 vm_role: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/core-functionality/devices/#device-roles):

        > Devices can be organized by functional roles, which are fully customizable by the user. For example, you might create roles for core switches, distribution switches, and access switches within your network.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        core_sw = netbox.DeviceRole("coreSw", color_hex="FF00FF")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeviceRoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/core-functionality/devices/#device-roles):

        > Devices can be organized by functional roles, which are fully customizable by the user. For example, you might create roles for core switches, distribution switches, and access switches within your network.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        core_sw = netbox.DeviceRole("coreSw", color_hex="FF00FF")
        ```

        :param str resource_name: The name of the resource.
        :param DeviceRoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeviceRoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 vm_role: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeviceRoleArgs.__new__(DeviceRoleArgs)

            if color_hex is None and not opts.urn:
                raise TypeError("Missing required property 'color_hex'")
            __props__.__dict__["color_hex"] = color_hex
            __props__.__dict__["name"] = name
            __props__.__dict__["slug"] = slug
            __props__.__dict__["vm_role"] = vm_role
        super(DeviceRole, __self__).__init__(
            'netbox:index/deviceRole:DeviceRole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            color_hex: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            slug: Optional[pulumi.Input[str]] = None,
            vm_role: Optional[pulumi.Input[bool]] = None) -> 'DeviceRole':
        """
        Get an existing DeviceRole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeviceRoleState.__new__(_DeviceRoleState)

        __props__.__dict__["color_hex"] = color_hex
        __props__.__dict__["name"] = name
        __props__.__dict__["slug"] = slug
        __props__.__dict__["vm_role"] = vm_role
        return DeviceRole(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> pulumi.Output[str]:
        return pulumi.get(self, "color_hex")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter(name="vmRole")
    def vm_role(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "vm_role")
