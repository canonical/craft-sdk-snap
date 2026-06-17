# craft-sdk snap

The craft-sdk snap contains pre-built wheels needed by Craft apps, such as Snapcraft
and Rockcraft.

## Background

The Craft apps build Python dependencies from source instead of relying on
pre-built wheels from an external source such as PyPI. Building from source
is resource-intensive and requires additional tooling for certain libraries.
For example, [cryptography](https://github.com/pyca/cryptography) and
[pydantic](https://github.com/pydantic/pydantic) require compatible versions of Cargo
to build.

This snap provides pre-built wheels for these libraries, allowing Craft apps to avoid
rebuilding them independently.

For an example, see the snap in the `test/` directory, which consumes craft-sdk as
a build-snap.

## Testing

### Prerequisites

- Snapcraft installed
- Access to [`craft-sd`](https://snapcraft.io/craft-sdk) on the Snap Store

### Build the craft-sdk snap

```bash
snapcraft pack
# The test will install a local copy of the snap from its directory.
cp craft-sdk*.snap test/craft-sdk-snap
```

### Build the consumer snap

```bash
cd test
snapcraft pack
```

### Install and run the consumer snap

```bash
sudo snap install ./test-python-app_0.1_amd64.snap --dangerous
test-python-app
```

### Expected behavior

The app should run pydantic validation successfully, confirming that pydantic is
resolved from wheels provided by `craft-sdk` during build.
