# Setup stuff to copy files back and forth
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups
source /cvmfs/fermilab.opensciencegrid.org/products/larsoft/setup
setup ifdhc

#Setup gm2
source /cvmfs/gm2.opensciencegrid.org/prod/g-2/setup
setup gm2 v9_45_00 -q prof

#Add current directory to LD_LIBRARY_PATH for so file we copied
export LD_LIBRARY_PATH=`pwd`:$LD_LIBRARY_PATH

# Some nodes have newer kernels
case 2.6.32-754.30.2.el6.x86_64 in
  3.*) export UPS_OVERRIDE="-H Linux64bit+2.6-2.12";;
  4.*) export UPS_OVERRIDE="-H Linux64bit+2.6-2.12";;
esac

#Run jobs
for file in `cat xrootdFileList000.txt`; do

  echo "Processing $file"
  echo $file

  id=${file##*15921}
  id=${id%*.root}
  echo "Output "recoCoarseScanPlots${id}.root

  gm2 -c RunRecoAndPlotVeryCoarseScan.fcl -s $file -T recoCoarseScanPlots${id}.root -n 15

done
