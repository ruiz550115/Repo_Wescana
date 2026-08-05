import pyads
import numpy as np


# PLC Connection 
PLC_NETID = "127.0.0.1.1.1"
PLC_PORT = 851
plc = pyads.Connection(PLC_NETID, PLC_PORT)
plc.open()
print(plc.read_by_name("Main.nCycleCounter", pyads.PLCTYPE_INT))


# Read initial joint angles from PLC and set robot state
CurrentPosition = plc.read_by_name("Main.lrActPos", pyads.PLCTYPE_ARR_REAL(36))
print(CurrentPosition)


# Cyclicly read joint commands from PLC and update robot state in pybullet
while True:
    CurrentPosition = plc.read_by_name("Main.lrActPos", pyads.PLCTYPE_ARR_REAL(36))
        
# Read actual joint angles from pybullet and write back to PLC
#actual_deg = [0.0] * 36 
    PosCmd = []

    for i in range(36):

        PosCmd.append(200.0)

   # print(PosCmd)
    
    plc.write_by_name("GVL_PY.aPythonPositions", PosCmd, pyads.PLCTYPE_ARR_REAL(36))
