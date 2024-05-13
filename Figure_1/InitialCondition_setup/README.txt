To create the initial configuration (IC_Neph80.data), open a terminal and run
> bash create_InitCoor.sh

To create the colvar file, open a terminal and run
> python3 ColVarFileWriter.py 

- LT_writer.py creates the template files to be used by moltemplate
- memBound_MolArray.py creates the Nephrin array on a 2D surface 
- populate.inp places the user-specified number of molecules (Nck, NWASP and Arp2/3) inside the user-specified defined volume
- mergeXYZ.py combines the initial coordinates of Nephrin, Nck, NWASP and Arp2/3 to create the inital state (Combined.xyz) of the system
- moltemplate.sh creates initial condition of the system (IC_Neph80.data) by parsing the coordinates from the Combined.xyz file.  