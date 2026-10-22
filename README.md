# AnnyOS SDK

Current version: **0.3.0**

The AnnyOS SDK contains the public `.AP` v1 format and API headers, the AADL
compiler, core AADL libraries, and sample applications. AADL supports classes,
inheritance, statically resolved objects and methods, and recursive imports.
Compiled applications are bounded AP v1 bytecode interpreted by AnnyOS.

## Build sample applications

Requirements: Python 3.

```sh
make build
```

The compiler writes sample `.AP` files to the ignored `build/` directory. To
compile one application directly:

```sh
python3 tools/aadlc.py apps/HELLO.aadl build/HELLO.AP
```

See [AADL](docs/AADL.md), the [AP format](docs/AP_FORMAT.md), and the
[SDK guide](docs/SDK.md) for language, bytecode, and API details.
