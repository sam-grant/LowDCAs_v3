pnfsOutDir=/pnfs/GM2/scratch/users/sgrant/LowDCAsScans2/CoarseNoneWrong
echo "Checking output files for in $pnfsOutDir"

for line in `cat MainFileList.txt`; do

  # Get run and sub-run  
  id=${line%_*}
  id=${id##*_}


  if [ ! -f ${pnfsOutDir}/simScanCoarseNoneWrong_${id}.root ]; then
    echo ${pnfsOutDir}/simScanCoarseNoneWrong_${id}.root
  fi

done