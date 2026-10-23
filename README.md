# AnnyOS SDK

Current version: **0.4.0**

The AnnyOS SDK provides the public `.AP` v1 format and API headers, the AADL
compiler, core AADL libraries, and sample applications. The compiler supports
recursive imports, compile-time classes and inheritance, static method
resolution, application arguments, and bounded AP output. ConfigSave services
use AnnyOS API v2. AP applications remain interpreted bytecode; the SDK does
not provide native x86 compilation or process isolation.

## Build sample applications

Requirements: Python 3.

```sh
make build
python3 tools/aadlc.py apps/HELLO.aadl build/HELLO.AP
```

See [AADL](docs/AADL.md), the [AP format](docs/AP_FORMAT.md), and the
[SDK guide](docs/SDK.md) for compiler, bytecode, and API details.
