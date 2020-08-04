mainDir=/pnfs/GM2/scratch/users/sgrant/LowDCAsNominalSim/Q
for dir in `ls $mainDir`; do
    echo ${mainDir}/${dir}/xrootdFileList${dir}.txt
    cat ${mainDir}/${dir}/xrootdFileList${dir}.txt
done
