# craft-sdk pydantic wheel build-snap demo

This repository contains:

- a provider snap (`craft-sdk`) that publishes wheels (including pydantic and pydantic-core)
- a consumer snap in `test/` that uses `craft-sdk/latest/edge` as a `build-snap`

## Prerequisites

- Snapcraft installed
- Access to `craft-sdk/latest/edge` on the Snap Store

## Build the consumer snap

```bash
cd test
snapcraft pack
```

## Install and run the consumer snap

```bash
sudo snap install ./test-python-app_0.1_amd64.snap --dangerous
snap run test-python-app.my-app
```

## Expected behavior

The app should run pydantic validation successfully, confirming that pydantic is resolved from wheels provided by `craft-sdk` during build.
