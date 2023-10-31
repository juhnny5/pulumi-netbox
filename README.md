# pulumi_netbox

A Pulumi package for creating and managing Netbox resources.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed and configured:

```bash
pulumi new python
pulumi stack init dev
```

Install `pulumi-netbox` Python 3 package:

```bash
pip install git+https://github.com/juhnny5/pulumi-netbox.git@3b60cf3136e158c640fa1510841df78ddfffddd5
```

Store Netbox login infos:

```bash
pulumi config set netbox:serverUrl <NETBOX_URL> --secret
pulumi config set netbox:apiToken <NETBOX_API_TOKEN> --secret
```

## Examples

### Create a new user

```python
import pulumi
import pulumi_netbox as netbox

pulumi_user = netbox.User(
    "pulumi",
    username="pulumi",
    password="pulumi",
    active=True,
    staff=True
)

pulumi.export("pulumi_user", pulumi_user.id)
```

Launch Pulumi commands:

```bash
pulumi preview
pulumi up
pulumi destroy
```

## Contributing

Contributions to this project are welcome! If you find any issues or have improvements to suggest, please open an issue or submit a pull request.

## Acknowledgments

- Pulumi Documentation
- Netbox Documentation

## Go further

### Publish this project

```bash
python3 setup.py sdist bdist_wheel
twine upload --repository pypi dist/*
```
