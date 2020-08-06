
# Setup stuff to copy files back and forth
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups
source /cvmfs/fermilab.opensciencegrid.org/products/larsoft/setup
setup ifdhc

#Setup gm2
source /cvmfs/gm2.opensciencegrid.org/prod/g-2/setup
setup gm2 v9_49_00 -q prof

#Add current directory to LD_LIBRARY_PATH for so file we copied
export LD_LIBRARY_PATH=`pwd`:$LD_LIBRARY_PATH

# Some nodes have newer kernels
case 2.6.32-754.30.2.el6.x86_64 in
  3.*) export UPS_OVERRIDE="-H Linux64bit+2.6-2.12";;
  4.*) export UPS_OVERRIDE="-H Linux64bit+2.6-2.12";;
esac

gm2 -c 0.0000.fcl -s root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/GM2/daq/run1/offline/gm2_5037A/runs_15000/15921/gm2offline_full_27633716_15921.00313.root -T recoPlots0.0000.root -n 3

# Only copy back if job completed successfully (output from last command was 0)
if [ $? -eq 0 ]; then
	if [ -f recoPlots0.0000.root ]; then
    	ifdh mv recoPlots0.0000.root /pnfs/GM2/scratch/users/sgrant/pValueWindowScan/recoPlots0.0000.root
    else 
    	echo "recoPlots0.0000.root does not exist.  ls reads:"
    	ls
    fi
fi