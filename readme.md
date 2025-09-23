

![logo_gslv.png](figures%2Flogo_gslv.png)



GSLV (Grid SoLVer) is a C++ library for advanced power systems simulation
that has been exposed to python closely following the VeraGrid API design.

## Supported OS and platforms

GSLV is available for Linux (based on the kernel of Ubuntu 20.04), 
OSX with *M* architectures, and Microsoft's Windows 10 or newer.

For the time being, only the python module is made available. 
Upon special request a static or dynamic library could be provided. 

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


Upon loading, the license will be validated online automatically and you will
be able to use GSLV.
A characteristic of the license is that once validated online, it allows 24h of 
off-line access until requiring an on-line verification. This allows for working on 
planes or other temporary off-line situations.
Special, completely off-line licenses are possible as well.

## [VeraGrid Usage](veragrid_usage.md)

GSLV is best used as a plugin engine of [VeraGrid](https://veragrid.readthedocs.org/).
The usage with GSLV is really simple and provides alternative results 
to the veragrid python engine but much much faster.
Click [here](veragrid_usage.md) to know more.

## [Satndalone usage](standalone_usage.md)

This is a brief guide to get you started using GSLV.
You may want to use gslv directly. 
Its API is amost identical to the VeraGrid one, so it should be straigh forward to get started.
Click [here](standalone_usage.md) to know more.


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