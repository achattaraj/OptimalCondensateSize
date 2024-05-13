This repo contains simulation and data analysis methods of the research article titled **"Multi-condensate state as a functional strategy to optimize the cell signaling output"**.
*  __LAMMPS_sims__ contains files related to Langevin Dynamics simulations (Figure 1). Instructions on [how to run lammps](https://docs.lammps.org/Run_head.html)
*  __PDE_VCell__ contains files related to reaction-diffusion simulations (Partial Differential Equation models) using the [Virtual Cell](https://vcell.org/support) software (Figures 2 and 3)
*  __ODE_Solutions__ contains python files related to the Ordinary Differential Equation models (Figures 4 and 5)

__Requirements__:
(Versions of the softwares used in this study are listed here)
* __LAMMPS executable:__ lammps-5Jun19
    * Simulations are run on Harvard FAS RC. As of 05/13/2024, modules: gcc/13.2.0-fasrc01,  openmpi/4.1.5-fasrc03
* __Virtual Cell:__ VCell 7.5.0 (build 62)
* __Python:__
    * conda version: 23.3.1
    * conda-build version : 3.23.3
    * python version : 3.10.9
    * platform : win-64
    * user-agent : conda/23.3.1 requests/2.28.1 CPython/3.10.9 Windows/10 
    * Numpy version: 1.24.3
    * Matplotlib version: 3.7.0
    * Pandas version: 1.5.3
    * Nrrrd module: 1.0.0
