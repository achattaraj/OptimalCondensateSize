#!/bin/bash
#SBATCH --job-name=const_Mtd
#SBATCH -n  14 #Number of cores
#SBATCH -t 3-00:00:00 # Amount of time needed DD-HH:MM:SS
#SBATCH -p shared # Partition to submit to
#SBATCH --mem-per-cpu=400
#SBATCH -o %x_%j.out  # File to which STDOUT will be written, %j inserts jobid
#SBATCH -e %x_%j.err  # File to which STDERR will be written, %j inserts jobid
#SBATCH --mail-type=END
#SBATCH --mail-user=achattaraj@fas.harvard.edu

module load gcc/12.2.0-fasrc01 openmpi/4.1.4-fasrc01

srun -n $SLURM_NTASKS --mpi=pmix /n/home07/achattaraj/lammps-5Jun19/src/lmp_mpi -in Neph_clustering_Rg.in 
