Author: Michael Vincent
Date:   2/21/2017
Description:
    This library contains a series of functions for characterizing motors. 
    In total, the equations only use 7 different inputs: 
        - Nominal voltage (V_nom)   [units: V]
        - Power rating (P)          [units: W]
        - Terminal resistance (R)   [units: Ohm]
        - Terminal inductance (L)   [units: H]
        - No load current (I_0)     [unit: A]
        - No load speed (w_0)       [units: rad/s]
        - Rotor inertia (J)         [units: kg*m^2]

References:
    Lynch, K., Marchuk, N., and Elwin, M. (2016). Embedded computing and mechatronics with the PIC32 microcontroller.