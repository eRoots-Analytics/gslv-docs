# Notes on performance

For the best performance, use a desktop Linux distribution or OSX distribution.

## Cores and performance

The more cores, the more parallel performance...but not linearly.
If the runtime of a process in an 8-core processor takes 10 minutes, the same
process in a 16-core computer will not take 5 minutes. This is because, adding more cores
also adds process-synchronization overhead. 
In general, the gain obtained with more cores is asymptotic.

## Threading

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


## Processor throttling (overheating protection)

For some (poorly refrigerated) systems you may observe that the processor usage decreases
after some time at a 100% usage. This is specially true for laptops, but may also occur for
desktop system with insufficient ventilation or that cannot handle sustained high usage.

To avoid this, use well refrigerated workstations or server-grade computers.