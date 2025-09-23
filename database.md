# DataBase (The MultiCircuit)

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
GSLV is made such as the time component is a first class design element