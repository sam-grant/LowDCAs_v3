pnfsOutDir=/pnfs/GM2/scratch/users/sgrant/LowDCAsScans/FineNoneWrong
echo "Checking output files for in $pnfsOutDir"

output="fileListForHaddFineScanNoneWrong.txt"

rm -rf $output && touch $output

for line in `cat MainFileList.txt`; do

  # Get run and sub-run  
  id=${line%_*}
  id=${id##*_}


  if [ -f ${pnfsOutDir}/*/simScanFineNoneWrong_${id}.root ]; then
    echo $line >> $output
  fi

done