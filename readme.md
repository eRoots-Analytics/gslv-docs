

![logo_gslv.png](figures%2Flogo_gslv.png)



GSLV (Grid SoLVer) is a C++ library for advanced power systems simulation
that has been exposed to python closely following the VeraGrid API design.

## Supported OS and platforms

GSLV is available for Linux (based on the kernel of Ubuntu 20.04 or newer), 
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
"[the path to the python executable]" -m pip install pygslv
```

For instance, to install gslv into VeraGrids's python under a Windows setup:
```bash
"c:\veragrid\python312\python.exe" -m pip install pygslv
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


## [Notes on performance](notes_on_performance.md)

Of course, not all systems are created equal, and GSLV 
will run better on high performance systems running Linux or OSX.
Click [here](notes_on_performance.md) to know more.