# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['InterfaceArgs', 'Interface']

@pulumi.input_type
class InterfaceArgs:
    def __init__(__self__, *,
                 virtual_machine_id: pulumi.Input[int],
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tagged_vlans: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 untagged_vlan: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Interface resource.
        """
        pulumi.set(__self__, "virtual_machine_id", virtual_machine_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if mac_address is not None:
            pulumi.set(__self__, "mac_address", mac_address)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tagged_vlans is not None:
            pulumi.set(__self__, "tagged_vlans", tagged_vlans)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            warnings.warn("""This attribute is not supported by netbox any longer. It will be removed in future versions of this provider.""", DeprecationWarning)
            pulumi.log.warn("""type is deprecated: This attribute is not supported by netbox any longer. It will be removed in future versions of this provider.""")
        if type is not None:
            pulumi.set(__self__, "type", type)
        if untagged_vlan is not None:
            pulumi.set(__self__, "untagged_vlan", untagged_vlan)

    @property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "virtual_machine_id")

    @virtual_machine_id.setter
    def virtual_machine_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "virtual_machine_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mac_address")

    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac_address", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="taggedVlans")
    def tagged_vlans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "tagged_vlans")

    @tagged_vlans.setter
    def tagged_vlans(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "tagged_vlans", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="untaggedVlan")
    def untagged_vlan(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "untagged_vlan")

    @untagged_vlan.setter
    def untagged_vlan(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "untagged_vlan", value)


@pulumi.input_type
class _InterfaceState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tagged_vlans: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 untagged_vlan: Optional[pulumi.Input[int]] = None,
                 virtual_machine_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Interface resources.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if mac_address is not None:
            pulumi.set(__self__, "mac_address", mac_address)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tagged_vlans is not None:
            pulumi.set(__self__, "tagged_vlans", tagged_vlans)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            warnings.warn("""This attribute is not supported by netbox any longer. It will be removed in future versions of this provider.""", DeprecationWarning)
            pulumi.log.warn("""type is deprecated: This attribute is not supported by netbox any longer. It will be removed in future versions of this provider.""")
        if type is not None:
            pulumi.set(__self__, "type", type)
        if untagged_vlan is not None:
            pulumi.set(__self__, "untagged_vlan", untagged_vlan)
        if virtual_machine_id is not None:
            pulumi.set(__self__, "virtual_machine_id", virtual_machine_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mac_address")

    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac_address", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="taggedVlans")
    def tagged_vlans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "tagged_vlans")

    @tagged_vlans.setter
    def tagged_vlans(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "tagged_vlans", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="untaggedVlan")
    def untagged_vlan(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "untagged_vlan")

    @untagged_vlan.setter
    def untagged_vlan(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "untagged_vlan", value)

    @property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "virtual_machine_id")

    @virtual_machine_id.setter
    def virtual_machine_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "virtual_machine_id", value)


class Interface(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tagged_vlans: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 untagged_vlan: Optional[pulumi.Input[int]] = None,
                 virtual_machine_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a Interface resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InterfaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Interface resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param InterfaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InterfaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tagged_vlans: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 untagged_vlan: Optional[pulumi.Input[int]] = None,
                 virtual_machine_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InterfaceArgs.__new__(InterfaceArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["mac_address"] = mac_address
            __props__.__dict__["mode"] = mode
            __props__.__dict__["mtu"] = mtu
            __props__.__dict__["name"] = name
            __props__.__dict__["tagged_vlans"] = tagged_vlans
            __props__.__dict__["tags"] = tags
            if type is not None and not opts.urn:
                warnings.warn("""This attribute is not supported by netbox any longer. It will be removed in future versions of this provider.""", DeprecationWarning)
                pulumi.log.warn("""type is deprecated: This attribute is not supported by netbox any longer. It will be removed in future versions of this provider.""")
            __props__.__dict__["type"] = type
            __props__.__dict__["untagged_vlan"] = untagged_vlan
            if virtual_machine_id is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machine_id'")
            __props__.__dict__["virtual_machine_id"] = virtual_machine_id
        super(Interface, __self__).__init__(
            'netbox:index/interface:Interface',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            mac_address: Optional[pulumi.Input[str]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            mtu: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tagged_vlans: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            untagged_vlan: Optional[pulumi.Input[int]] = None,
            virtual_machine_id: Optional[pulumi.Input[int]] = None) -> 'Interface':
        """
        Get an existing Interface resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InterfaceState.__new__(_InterfaceState)

        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["mac_address"] = mac_address
        __props__.__dict__["mode"] = mode
        __props__.__dict__["mtu"] = mtu
        __props__.__dict__["name"] = name
        __props__.__dict__["tagged_vlans"] = tagged_vlans
        __props__.__dict__["tags"] = tags
        __props__.__dict__["type"] = type
        __props__.__dict__["untagged_vlan"] = untagged_vlan
        __props__.__dict__["virtual_machine_id"] = virtual_machine_id
        return Interface(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="taggedVlans")
    def tagged_vlans(self) -> pulumi.Output[Optional[Sequence[int]]]:
        return pulumi.get(self, "tagged_vlans")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="untaggedVlan")
    def untagged_vlan(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "untagged_vlan")

    @property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "virtual_machine_id")
