# Contingency analysis

GSLV incorporates 

## Full

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
    contingency_method=pg.ContingencyMethod.PowerFlow
)
nt = len(mc.time_array)
res = pg.run_contingencies(grid=mc, options=con_options, time_indices=list(range(nt)))

print(res.max_values.Sf)
print(res.max_values.loading)
```

## Linear contingencies

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
