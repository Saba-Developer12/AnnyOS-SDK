# AnnyOS SDK

The AnnyOS SDK provides the public headers, AP v1 packer, format documentation,
and sample applications for developing programs for AnnyOS. AP applications can
print text and command-line arguments or call documented system services,
including date/time, memory information, reboot, sleep, and PC speaker tone.

## Build an AP application

With Python 3 installed, build all sample applications from this repository root:

```sh
make build
```

The generated `.AP` files are written to the ignored `build/` directory. To pack
one application manually:

```sh
python3 tools/ap_pack.py apps/HELLO.apasm HELLO.AP
```

See `docs/SDK.md` for the SDK overview and `docs/AP_FORMAT.md` for the binary
format and supported API services.
