
import pandas as pd
import numpy as np
from ctp_hilow_min_new import conv_trig_pot_mod

cols =  ['yr1','mn1','hr1','plev1','hlev1','tlev1','qlev1', 
          'yr2','mn2','hr2','plev2','hlev2','tlev2','qlev2', 
          'yr3','mn3','hr3','plev3','hlev3','tlev3','qlev3', 
          'yr4','mn4','hr4','plev4','hlev4','tlev4','qlev4', 
          'yr5','mn5','hr5','plev5','hlev5','tlev5','qlev5', 
          'yr6','mn6','hr6','plev6','hlev6','tlev6','qlev6', 
          'yr7','mn7','hr7','plev7','hlev7','tlev7','qlev7']

df = pd.read_csv('../examples/Sample_obs/Sample_profile.txt', header = None, names = cols)
nlev_in = len(df)

nlev_in=len(df)
tlev_in = df['tlev1'].values
#tlev_in = np.reshape(tlev_in,[1, nlev_in], order = 'F') 

qlev_in = df['qlev1'].values
#qlev_in = np.reshape(qlev_in,[1,nlev_in], order = 'F') 

plev_in = df['qlev1'].values
#plev_in =  np.reshape(plev_in,[1,nlev_in], order = 'F') 

#qlev_in = list(qlev_in)

t0 = tlev_in[0]
q0 = qlev_in[0]
p0 = plev_in[0]

#nlev_in = 5
arr = [[0.00879983, 0.00892215, 0.00955156, 0.00802447, 0.00599362]]
#plev_in = [98100., 97400., 95300., 94100., 92500.]
#tlev_in = [285.6, 289. , 290.4, 290. , 290.4]
#print(tlev_in)
#print( np.reshape(qlev_in,[1,nlev_in], order = 'F') )

arr  = np.ones([10,1], order='F')
arr[:] = np.random.rand(10,1)
#print('Shape of arr:' , arr.shape)

conv_trig_pot_mod.ctp_hi_low(10, arr, arr, arr, 1,1, 1)

print(ctp)

print(hilow)
