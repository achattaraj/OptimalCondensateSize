This repo contains simulation and data analysis methods of the research article titled **"Multi-condensate state as a functional strategy to optimize the cell signaling output"**.
*  __Figure 1__ contains files related to Langevin Dynamics simulations, using the LAMMPS software. Instructions on [how to run lammps](https://docs.lammps.org/Run_head.html)
*  __Figure 2 and Figure 3__ contains files related to reaction-diffusion simulations using the [Virtual Cell](https://vcell.org/support) software
*  __Figure 4__ contains python files related to the analytical solutions of the Ordinary Differential Equation (ODE)
*  __Figure 5__ contains python files to solve ODEs with a distribution of cluster sizes

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
