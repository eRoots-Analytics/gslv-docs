import pygslv as pg

grid = pg.MultiCircuit(nt=12, name="My grid", Sbase=100, fBase=50)

bus1 = pg.Bus(nt=12, name="Bus1", Vnom=132)
grid.add_bus(bus1)

load1 = pg.Load(nt=12, bus=bus1, name="Load1")
grid.add_load(load1)

print(grid)
