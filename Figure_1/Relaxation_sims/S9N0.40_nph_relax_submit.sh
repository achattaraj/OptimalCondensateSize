#!/bin/bash
#SBATCH --job-name=S9N0.40
#SBATCH -n  12
#SBATCH -t 3-00:00:00 # DD-HH:MM:SS
#SBATCH -p shared
#SBATCH --mem-per-cpu=400
#SBATCH -o %x_%j.out
#SBATCH -e %x_%j.err
#SBATCH --mail-type=END
#SBATCH --mail-user=achattaraj@fas.harvard.edu

module load gcc/12.2.0-fasrc01 openmpi/4.1.4-fasrc01

srun -n $SLURM_NTASKS --mpi=pmix /n/home07/achattaraj/lammps-5Jun19/src/lmp_mpi -in S9N0.40_nph_relax_input.in 
