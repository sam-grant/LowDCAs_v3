# Setup stuff to copy files back and forth
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups
source /cvmfs/fermilab.opensciencegrid.org/products/larsoft/setup
setup ifdhc

# Copy xrootdFileList012 here
if [ ! -z "`ifdh ls /pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/xrootdFileList012.txt`" ]; then
  ifdh cp /pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/xrootdFileList012.txt xrootdFileList012.txt
else 
  echo "/pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/xrootdFileList012.txt does not exist"
fi

#Copy fcl and .so files
if [ ! -z "`ifdh ls /pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/RunSimAndPlotNominalNoQ.fcl`" ]; then
  ifdh cp /pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/RunSimAndPlotNominalNoQ.fcl ./RunSimAndPlotNominalNoQ.fcl
else 
  echo "/pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/RunSimAndPlotNominalNoQ.fcl does not exist"
fi
if [ ! -z "`ifdh ls /pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/libgm2tracker_analyses_LowDCAsTruthPlots_module.so`" ]; then
  ifdh cp /pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/libgm2tracker_analyses_LowDCAsTruthPlots_module.so ./libgm2tracker_analyses_LowDCAsTruthPlots_module.so
else 
  echo "/pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/libgm2tracker_analyses_LowDCAsTruthPlots_module.so does not exist"
fi

#Setup gm2
source /cvmfs/gm2.opensciencegrid.org/prod/g-2/setup
setup gm2 v9_45_00 -q prof

#Add current directory to LD_LIBRARY_PATH for so file we copied
export LD_LIBRARY_PATH=`pwd`:$LD_LIBRARY_PATH

# Some nodes have newer kernels
case 2.6.32-754.28.1.el6.x86_64 in
  3.*) export UPS_OVERRIDE="-H Linux64bit+2.6-2.12";;
  4.*) export UPS_OVERRIDE="-H Linux64bit+2.6-2.12";;
esac

#Run jobs
for file in `cat xrootdFileList012.txt`; do
  echo "Processing $file"

  id=${file%_*}
  id=${id##*_}

  # ls /pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/simPlots_${id}.root

  # Skip if the output file already exists
  if [ -f /pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/simPlots_${id}.root ]; then
    echo "/pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/NoQ/012/simPlots_${id}.root exits, skipping..."
    continue
  fi

  gm2 -c RunSimAndPlotNominalNoQ.fcl -s $file -T simPlots_${id}.root


done
