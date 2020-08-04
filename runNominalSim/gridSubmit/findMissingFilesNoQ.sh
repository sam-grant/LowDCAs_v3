pnfsOutDir=/pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim2/NoQ
echo "Checking output files for in $pnfsOutDir"

for line in `cat MainFileList.txt`; do

  # Get run and sub-run  
  id=${line%_*}
  id=${id##*_}


  if [ ! -f ${pnfsOutDir}/simPlots_${id}.root ]; then
    echo ${pnfsOutDir}/simPlots_${id}.root
  fi

done