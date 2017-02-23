import math
'''
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

'''



def torque_constant(V_nom, w_0, dec=1):
    '''Calculate the torque constant, k_t
    
    args:
    V_nom = nominal voltage     [units: V]
    w_0 = angular velocity      [units: rad/s]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    k_t                         [units: N*m/A]
    '''
    
    return round(V_nom/float(w_0), dec)
    
    
def electrical_constant(V_nom, w_0, dec=1):
    '''Calculate the electrical constant, k_e
    
    args:
    V_nom = nominal voltage     [units: V]
    w_0 = angular velocity      [units: rad/s]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    k_e                         [units: V*s/rad]
    '''
    
    return V_nom/float(w_0)
    
    
def speed_constant(V_nom, w_0, dec=1):
    '''Calculate the speed constant, k_s
    
    args:
    V_nom = nominal voltage     [units: V]
    w_0 = angular velocity      [units: rad/s]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    k_s                         [units: rad/V*s]
    '''
    
    return w_0/float(V_nom)
    
    
def motor_constant(V_nom, w_0, R, dec=1):
    '''Calculate the motor constant, k_m
    
    args:
    R = terminal resistance     [units: Ohm]
    V_nom = nominal voltage     [units: V]
    w_0 = angular velocity      [units: rad/s]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    k_m                         [units: N*m/sqrt(W)]
    '''
    
    return round(V_nom/(float(w_0)*math.sqrt(R)), dec)
    
    
def max_continuous_current(P, R, dec=1):
    '''Calculate the maximum continuous current, I_cont
    
    args:
    P = Power                   [units: Watts]
    R = Terminal resistance     [units: Ohm]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    I_cont                      [units: A]
    '''
    
    return math.sqrt((P/float(R)))
    
    
def max_continuous_torque(P, R, V_nom, dec=1):
    '''Calculate the maximum continuous torque, tau_cont
    
    args:
    P = Power                   [units: Watts]
    R = Terminal resistance     [units: Ohm]
    V_nom = nominal voltage     [units: V]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    tau_cont                    [units: N*m]
    '''
    
    return V_nom*(math.sqrt((P/R))/float(w_0))
    
    
def short_circuit_damping(V_nom, w_0, R, dec=1):
    '''Calculate the short-circuit damping constant, B
    
    args:
    V_nom = nominal voltage     [units: V]
    w_0 = angular velocity      [units: rad/s]
    R = terminal resistance     [units: Ohm]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    B                           [units: N*m*s/rad]
    '''
    
    return round((V_nom**2)/float(((w_0**2)*R)), dec)
    
    
def electrical_time_constant(L, R, dec=1):
    '''Calculate the electrical time constant, T_e
    
    args:
    L = terminal inductance     [units: H]
    R = terminal resistance     [units: Ohm]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    T_e                         [units: s]
    '''
    
    return round((L/float(R)), dec)
    
    
def mechanical_time_constant(J, R, V_nom, w_0, dec=1):
    '''Calculate the electrical time constant, T_m
    
    args:
    J = Rotor inertia           [units: kg*m^2]
    R = terminal resistance     [units: Ohm]
    V_nom = nominal voltage     [units: V]
    w_0 = angular velocity      [units: rad/s]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    T_m [                       units: s]
    '''
    
    return round((J*R*(w_0**2))/float((V_nom**2)), dec)
    
    
def stall_current(R, V_nom, dec=1):
    '''Calculate the stall current, I_stall
    
    args:
    R = terminal resistance     [units: Ohm]
    V_nom = nominal voltage     [units: V]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    I_stall                     [units: A]
    '''
    
    return round((V_nom/float(R)), dec)
    
    
def stall_torque(R, V_nom, w_0, dec=1):
    '''Calculate the stall torque, tau_stall
    
    args:
    R = terminal resistance     [units: Ohm]
    V_nom = nominal voltage     [units: V]
    w_0 = angular velocity      [units: rad/s]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    tau_stall                   [units: N*m]
    '''
    
    return round(((V_nom**2)/float(R*w_0)), dec)
    
    
def max_mechanical_power(R, V_nom, dec=1):
    '''Calculate the maximum mechanical power, P_max
    
    args:
    R = terminal resistance     [units: Ohm]
    V_nom = nominal voltage     [units: V]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    P_max                       [units: W]
    '''
    
    return round(((V_nom**2)/float((4*R))), dec)
    
    
def max_efficiency(I_0, R, V_nom, dec=1):
    '''Calculate the maximum efficiency, n_max
    
    args:
    I_0 = No-load current       [units: A]
    R = terminal resistance     [units: Ohm]
    V_nom = nominal voltage     [units: V]
    
    kwargs:
    dec = specify the number of decimal places to round the result to (default is 1)
    
    returns:
    n_max                       [units: ...it's a percentage (%)]
    '''
    
    return round(((1-math.sqrt((I_0*R))/float(V_nom))**2), dec)