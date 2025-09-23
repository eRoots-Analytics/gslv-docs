# Power flow

The power flow simulation is the calculation to find the voltages of the nodes,
given the grid definition and it's power injections.

As such, the power flow simulation can be though of as an optimization problem
with only equality constraints, where we try to equalize the power flowing through the branches 
(which is a function of the voltage) with the specified nodal injections (loads and generation)

## Positive sequence power flow

The positive sequence power flow is the single-phase approximation of a
pre-supposed balanced three-phase system. This approximation has been used since the
inception of power systems calculations in the 1920's and has been
the de-facto industry standard for many decades.

### Controls

Depending on the method, certain controls may be available or not. In practice this is a quick way
to find control positons without resorting to a complete optimization.

Controls supported:

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

see \ref gslv::PowerFlowOptions


### Results


## Three-phase power flow


### Results