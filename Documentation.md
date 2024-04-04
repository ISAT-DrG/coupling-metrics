### 3/28/2024

- I started working under Linux environment installing conda under ubuntu with a minimal `scipy` environment

- Added forked coupling metrics to ISAT-DrG Drought project and created python branch

- Created folder `minimal` and moved ctp_hi_low static over there to thest 

- I have been successful wrapping the `Conv_Trig_Pot_Mod` using `f2py` following directions from here
  https://www.numfys.net/howto/F2PY/

- ```
   f2py -c ctp_hilow_min.f90  -m ctp_hilow_min
   python -m numpy.f2py -c ctp_hilow_min.f90  -m ctp_hilow_min
  ```

- Testing the module was not successful. There seem to be array shape issues, which I do not understand 

  ````
  conv_trig_pot_mod.ctp_hi_low(10, arr, arr, arr, 1,1, 1)
  ValueError: ctp_hilow_min.ctp_hilow_min.conv_trig_pot_mod.ctp_hi_low: failed to create array from the 2nd argument `qlev_in` -- 0-th dimension must be fixed to 1 but got 10
  ````

- Posted a question on stack overflow, because I cannot figure this out. 

- Next steps, 

  - wait for stackoverflow. 
  - Pull subroutine out of module? 