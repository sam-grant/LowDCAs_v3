pnfsOutDir=/pnfs/GM2/scratch/users/sgrant/LowDCAsReco_15921/NoQ
echo "Checking output files for in $pnfsOutDir"

for line in `cat MainFileList.txt`; do

  # Get run and sub-run  
  id=${line%_*}
  id=${id##*_}


  if [ ! -f ${pnfsOutDir}/recoPlots_${id}.root ]; then
    echo ${pnfsOutDir}/recoPlots_${id}.root
  fi

done