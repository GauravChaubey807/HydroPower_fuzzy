from values import *
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

water_level = ctrl.Antecedent(np.arange(0,21,1), 'Water Level')
flow_rate = ctrl.Antecedent(np.arange(0,100001,1), 'Flow Rate')
drain_valve = ctrl.Consequent(np.arange(0,101,1), 'Drain Valve')
release_valve = ctrl.Consequent(np.arange(0,101,1), 'Release Valve')

for i,j in wl.items():
	water_level[i] = fuzz.trimf(water_level.universe, j)
for i,j in fr.items():
	flow_rate[i] = fuzz.trimf(flow_rate.universe, j)

for i,j in mfov.items():
	drain_valve[i] = fuzz.trimf(drain_valve.universe, j)
	release_valve[i] = fuzz.trimf(release_valve.universe, j)
