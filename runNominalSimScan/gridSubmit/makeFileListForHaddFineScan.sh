pnfsOutDir=/pnfs/GM2/scratch/users/sgrant/LowDCAsScans/Fine
echo "Checking output files for in $pnfsOutDir"

output="fileListForHaddFineScan.txt"

rm -rf $output && touch $output

for line in `cat MainFileList.txt`; do

  # Get run and sub-run  
  id=${line%_*}
  id=${id##*_}


  if [ -f ${pnfsOutDir}/*/simScanFine_${id}.root ]; then
    echo $line >> $output #| tee $output
  fi

done