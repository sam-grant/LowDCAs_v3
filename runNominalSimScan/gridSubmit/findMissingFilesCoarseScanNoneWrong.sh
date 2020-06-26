pnfsOutDir=/pnfs/GM2/scratch/users/sgrant/LowDCAsScans/CoarseNoneWrong
echo "Checking output files for in $pnfsOutDir"

for line in `cat MainFileList.txt`; do

  # Get run and sub-run  
  id=${line%_*}
  id=${id##*_}


  if [ ! -f ${pnfsOutDir}/*/simScanCoarse_${id}.root ]; then
    echo $line
  fi

done