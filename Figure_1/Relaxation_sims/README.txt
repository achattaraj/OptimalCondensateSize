 - This is an example of how the relaxation simulations are carried out, for a particular set of energy parameters 
 (Es(pY,SH2) = 9kT, Ens = 0.4kT, where 1 kT ~ 0.6 kcal) 
  
  - S9N0.40_nph_relax_input.in is the input file that relaxes the system for 300 million steps, starting from the metadynamics output (neph_clustered_Vol1x.data) 
  - The final_state_S9N.40_relax.restart is then used as an initial condition to sample the .\relaxed_datafiles\*.DATA to save the state (coordinates and bonds) of the system at multiple timepoints. 
  - Those *.DATA files is then processed by python files to obtain final statistics which are saved inside .\relaxed_datafiles\pystate folder. 

  - Same routine is repeated for all other energy parameter combinations  
