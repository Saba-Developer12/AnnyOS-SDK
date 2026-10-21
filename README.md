# AnnyOS SDK

The AnnyOS SDK provides the public headers, AP v1 packer, format documentation,
and sample applications for developing programs for AnnyOS.

## Build an AP application

With Python 3 installed, run from this repository root:

```sh
python3 tools/ap_pack.py apps/HELLO.apasm HELLO.AP
```

See `docs/SDK.md` for the SDK overview and `docs/AP_FORMAT.md` for the binary
format and supported API services.
