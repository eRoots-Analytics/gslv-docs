# Introduction and basics

GSLV (Grid SoLVer) is a C++ library for advanced power systems simulation
that has been exposed to python closely following the VeraGrid API design.

This is a brief guide to get you started using GSLV.

## Supported OS

GSLV is available for Linux (based on the kernel of Ubuntu 20.04), 
OSX with *M* architectures, and Microsoft's Windows 10 or newer.

## Installing GSLV (Python)

The name of the GSLV package for python is `pygslv`

Installing is as simple as typing the following on your system command line:

```bash
pip install pygslv
```

And you will be able to install it in the system python distribution.

If you with to install `pygslv` into a specific python distribution do:

```bash
"the path to the python executable" -m pip install pygslv
```

## License and activation

If you have purchased a license with eRoots Analytics S.L. you have
received a license file (i.e. `license.gslv`). This license file has 
to be stored in a folder with **read and write access**, this is because 
GSLV will read that file to determine whether you have a valid license or not.

A simple way to provide the file is to explicitly tell its location 
right after importing gslv:
```python
import pygslv as pg

print("GSLV", pg.get_version())
pg.activate(r"my_license.gslv", verbose=True)
```

Alternatively, you could just search for a valid license:
```python
import pygslv as pg

print("GSLV", pg.get_version())
pg.search_license_and_activate()
```

This will search for the license first at the execution folder, 
and then in the `.VeraGrid` folder at your user folder location.

Upon loading, the license will be validated online automatically and you will
be able to use GSLV.
A characteristic of the license is that once validated online, it allows 24h of 
off-line access until requiring an on-line verification. This allows for working on 
planes or other temporary off-line situations.
Special, completely off-line licenses are possible as well.

## Python module usage

### Reading a VeraGrid file

GSLV read .VeraGrid files as the primary source of information. 
This is because it is the best way to fill and later use the internal 
structures easily:

```python

import pygslv as pg

pg.activate(r"my_license.gslv", verbose=True)
print("GSLV", pg.get_version())

logger = pg.Logger()
verbose = 0
mc: pg.MultiCircuit = pg.read_file("IEEE39_1W.VeraGrid", logger, verbose)

options = pg.PowerFlowOptions(solver_type=pg.SolverType.NR)
nt = len(mc.time_array)
res = pg.multi_island_pf(grid=mc, options=options, time_indices=list(range(nt)))

print(res.voltage)

```

## Notes on performance

For the best performance, use a desktop Linux distribution or OSX distribution.

### Cores and performance

The more cores, the more parallel performance...but not linearly.
If the runtime of a process in an 8-core processor takes 10 minutes, the same
process in a 16-core computer will not take 5 minutes. This is because, adding more cores
also adds process-synchronization overhead. 
In general, the gain obtained with more cores is asymptotic.

### Threading

GSLV's multi-threading is designed to make use of all the available logic
processors available if not instructed an specific number at runtime. 

However, under Microsoft's Windows, you may experience that not all cores operate at a 100%.
This is because of good reason and a bad reason; The good reason is that, due to the nature of electrical calculations 
(unlike AI operations for instance) it is not possible to allocate all memory in advance. 
This is no big issue for unix-like threading systems but it is for Microsoft Threading systems, which leads to the bad reason;
Despite using a specific memory allocation for multi-threading under windows, 
the MS Windows threading, cannot make use of all the processing power available unless all the memory is pre-allocated. 
This is unfortunate but true and has been experienced with all the major threading libraries for C++.

Hence, for any serious numerical task, please use the far superior Linux or OSX systems.


### Processor throttling (overheating protection)

For some (poorly refrigerated) systems you may observe that the processor usage decreases
after some time at a 100% usage. This is specially true for laptops, but may also occur for
desktop system with insufficient ventilation or that cannot handle sustained high usage.

To avoid this, use well refrigerated workstations or server-grade computers.


