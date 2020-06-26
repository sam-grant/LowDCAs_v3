# Setup stuff to copy files back and forth
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups
source /cvmfs/fermilab.opensciencegrid.org/products/larsoft/setup
setup ifdhc

# Copy xrootdFileList000 here
if [ ! -z "`ifdh ls /pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Coarse/000/xrootdFileList000.txt`" ]; then
  ifdh cp /pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Coarse/000/xrootdFileList000.txt xrootdFileList000.txt
else 
  echo "/pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Coarse/000/xrootdFileList000.txt does not exist"
fi

#Copy fcl and .so files
if [ ! -z "`ifdh ls /pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Coarse/000/RunSimAndPlotNominalScanCoarse.fcl`" ]; then
  ifdh cp /pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Coarse/000/RunSimAndPlotNominalScanCoarse.fcl ./RunSimAndPlotNominalScanCoarse.fcl
else 
  echo "/pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Coarse/000/RunSimAndPlotNominalScanCoarse.fcl does not exist"
fi
if [ ! -z "`ifdh ls /pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Coarse/000/libgm2tracker_analyses_LowDCAsTruthPlots_module.so`" ]; then
  ifdh cp /pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Coarse/000/libgm2tracker_analyses_LowDCAsTruthPlots_module.so ./libgm2tracker_analyses_LowDCAsTruthPlots_module.so
else 
  echo "/pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Coarse/000/libgm2tracker_analyses_LowDCAsTruthPlots_module.so does not exist"
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
for file in `cat xrootdFileList000.txt`; do
  echo "Processing $file"

  id=${file%_*}
  id=${id##*_}

  gm2 -c RunSimAndPlotNominalScanCoarse.fcl -s $file -T simScanCoarse_${id}.root

  # Only copy back if job completed successfully (output from last command was 0)
  if [ $? -eq 0 ]; then
    if [ -f simScanCoarse_${id}.root ]; then
      ifdh mv simScanCoarse_${id}.root /pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Coarse/000/simScanCoarse_${id}.root
    else 
      echo "simScanCoarse_${id}.root does not exist.  ls reads:"
      ls
    fi
  fi
done
