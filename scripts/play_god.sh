#!/bin/bash

#SBATCH -o /u/eschoe/output/%j.out      #output file
#SBATCH -e /u/eschoe/output/%j.err      #error file
#SBATCH -D ./                      #working directory
#SBATCH -J sim_multiverse                 #job name
#SBATCH -N 1                       #minimum number of nodes
#SBATCH --ntasks-per-node=1        #Python multiprocessing starts more tasks internally
#SBATCH --cpus-per-task=40         #request all cores to task to make room for Python's mp
#SBATCH --time=23:00:00            #estimated time
#SBATCH --mail-type=ALL            #receive mail when status changes
#SBATCH --mail-user=elisa.schoesser@uni-heidelberg.de


module load anaconda/3/2021.05
module load gcc/13
module load gsl/2.4
module load mkl/2023.1
source /u/eschoe/virtual_envs/py3.8_shader/bin/activate

srun /cobra/u/eschoe/virtual_envs/py3.8_shader/bin/python play_god_parallel.py