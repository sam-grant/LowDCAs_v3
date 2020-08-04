pnfsOutDir=/pnfs/GM2/scratch/users/sgrant/LowDCAsRecoScan_15921/Q

echo "Checking output files for in $pnfsOutDir"

for line in `cat MainFileList.txt`; do

  # Get run and sub-run  
  id=${line##*15921}
  id=${id%*.root}

  if [ ! -f ${pnfsOutDir}/recoCoarseScanPlots${id}.root ]; then
  # if [ -f ${pnfsOutDir}/*/simPlots_${id}.root ]; then
      echo ${pnfsOutDir}/recoCoarseScanPlots${id}.root
#    echo simPlots_${id}.root
#      echo $line
  fi

done