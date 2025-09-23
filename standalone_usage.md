# Standalone usage

This section will provide the necessary examples to run GSLV in standalone (library) mode.

## License and activation in library mode

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

## Creating a grid (The MultiCircuit)

The appropriate representation of a modern power system model
does not really attend to a fully relational, non-relational or graph philosophy.
Instead, the nature of it is mixed; There are things that must be modelled 
using strict relationships like the lines with its connection points, and others that
work better as a composite like the tap changer object inside a transformer object.

The experience has demonstrated the vast superiority of this approach versus
the simplistic table approaches or the unjustified waste of graph approaches. 
Here, you will learn about a selectively mixed structure that allows for complex 
device modelling, embedded time variations, and time series with minimal memory footprint. 
Enter, the MultiCircuit.

```python
import pygslv as pg

grid = pg.MultiCircuit(nt=12, name="My grid", Sbase=100, fBase=50)
```

We have just created an *empty* database formatted for 12 time steps.
GSLV is made such as the time component is a first class design element.
Unlike VeraGrid with the snapshot + time series, GSLV has time series always.

## Reading a VeraGrid file

GSLV reads `.veragrid` files as the primary source of information. 
This is because it is the best way to fill and later use the internal 
structures easily:

```python

import pygslv as pg

pg.activate(r"my_license.gslv", verbose=True)
print("GSLV", pg.get_version())

logger = pg.Logger()
verbose = 0
mc: pg.MultiCircuit = pg.read_file("IEEE39_1W.VeraGrid", logger, verbose)
```

For a VeraGrid file with only Snapshot information, the equivalent 
GSLV MultiCircuit will have 1 time step. For VeraGrid files with 
snapshot and time series, only the time series information will 
be translated to GSLV.

## Power flow

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

print(res.voltage)  # per-unit voltage matrix
```

### Methods and Controls

Depending on the method, certain controls may be available or not. In practice this is a quick way
to find control positons without resorting to a complete optimization.
The controls supported are as follows:

|   | Newton Raphson  |Powell Dog-leg|Levenberg-Marquardt|Iwamoto|Fast-decoupled|Gauss-seidel|Holomorphic embedding|Linear without voltage modules|Linear with voltage modules|
|---|---|---|---|---|---|---|---|---|---|
|Local voltage control using a Generator.|  ✅ | ✅  | ✅  |  ✅ | ✅  | ✅  |  ✅ |  ✅  |  ✅ |
|Remote voltage control using a Generator.| ✅  |  ✅ |  ✅ |  ✅ |  ✅ |   |   |   |   |
|Generator reactive power limits.| ✅  |  ✅ |  ✅ |  ✅ | ✅  |  ✅ |   |   |   |
|Local and remote voltage control using a transformer's tap changer.| ✅  |  ✅ |  ✅ |   |   |   |   |   |   |
|Local active power control using a transformer's tap changer.|  ✅ | ✅  |  ✅ |   |   |   |   |   |   |
|Local reactive power control using a transformer's tap changer.| ✅  | ✅  | ✅  |   |   |   |   |   |   |
|Local and remote AC and DC voltage control using a converter.| ✅  | ✅  | ✅  |   |   |   |   |   |   |
|Local AC and DC active power control using converter.|✅   | ✅  |  ✅ |   |   |   |   |   |   |
|Local AC reactive power control using a converter.| ✅  | ✅  |  ✅ |   |   |   |   |   |   |


## Contingency analysis

GSLV incorporates a time series contingency analysis.

### Complete, without approximations

This option runs a non-linear (Newton-Raphson) 
power flow and evaluated the contingencies with the same method.
This will perform N power flows times the number of time steps.

```python
import pygslv as pg

print("GSLV", pg.get_version())
# pg.activate(r"~\.GridCal\license.gslv", verbose=True)  # alternative
pg.search_license_and_activate(r"", verbose=True)

logger = pg.Logger()
verbose = 0
mc: pg.MultiCircuit = pg.read_file("IEEE39_1W.gridcal", logger, verbose)

pf_options = pg.PowerFlowOptions(solver_type=pg.SolverType.NR)
con_options = pg.ContingencyAnalysisOptions(
    pf_options=pf_options,
    contingency_method=pg.ContingencyMethod.PowerFlow
)
nt = len(mc.time_array)
res = pg.run_contingencies(grid=mc, options=con_options, time_indices=list(range(nt)))

print(res.max_values.Sf)  # apparent power from
print(res.max_values.loading)  # branches loading
```

### Linear contingencies

We could choose to run non-linear power flows, but have the contingency evaluation be linear:

```python
import pygslv as pg

print("GSLV", pg.get_version())
# pg.activate(r"~\.GridCal\license.gslv", verbose=True)
pg.search_license_and_activate(r"", verbose=True)

logger = pg.Logger()
verbose = 0
mc: pg.MultiCircuit = pg.read_file("IEEE39_1W.gridcal", logger, verbose)

pf_options = pg.PowerFlowOptions(solver_type=pg.SolverType.NR)
con_options = pg.ContingencyAnalysisOptions(
    pf_options=pf_options,
    contingency_method=pg.ContingencyMethod.PTDF
)
nt = len(mc.time_array)
res = pg.run_contingencies(grid=mc, options=con_options, time_indices=list(range(nt)))

print(res.max_values.Sf)
print(res.max_values.loading)
```

These scripts will output some arrays.