#!bin/echo # Please source instead

#Setup all the stuff we need here

# Standard stuff
source /grid/fermiapp/products/common/etc/setups.sh
setup jobsub_client
setup fife_utils

# source /cvmfs/gm2.opensciencegrid.org/prod/g-2/setup
# setup gm2 v9_45_00 -q prof
# source /gm2/app/users/sgrant/g2Soft/gm2Dev_v9_45_00/localProducts_gm2_v9_45_00_prof/setup
# source mrb setEnv # Seg fault without this



#Make sure file list exists
if [ $# -ne 0 ]; then
  echo "No arguments are allowed. $# was/were supplied."
  return
fi

#Make sure file list exists
if [ ! -f MainFileList.txt ] || [ `cat MainFileList.txt | wc -l` -eq 0 ]; then
  echo "Input file list \"MainFileList.txt\" is required.  This was not found or has 0 entries"
  return
fi

# Split into list with 5 each
echo "Splitting file list" 
rm -f SplitFileList*
rm -f xrootdFileList*

split MainFileList.txt -l 5 -a 3 -d SplitFileList
for file in `ls SplitFileList*`; do 
  mv $file ${file}.txt
done

# Make output directory
pnfsOutDir=/pnfs/GM2/scratch/users/${USER}/LowDCAsScans2/Coarse

echo "Output files will appear in $pnfsOutDir"

if [ ! -d $pnfsOutDir ]; then
  mkdir -p $pnfsOutDir
  chmod -R g+w $pnfsOutDir
fi

# Add xrootd business to the start of file names
for file in `ls SplitFileList*`; do 

  fileNum=${file##SplitFileList}
  fileNum=${fileNum%.txt}

  # Split output files into directories
  # mkdir -p ${pnfsOutDir}/${fileNum}
  # chmod -R g+w ${pnfsOutDir}/${fileNum}

  rm -f xrootFileList${fileNum}.txt && touch xrootdFileList${fileNum}.txt
  rm -f ${pnfsOutDir}/xrootdFileList*.txt

  for line in `cat $file`; do
    # Strip /pnfs/ from file name and write into new file

    id=${line%_*}
    id=${id##*_}
    # Skip files already written
    if [ -f ${pnfsOutDir}/simScanCoarse_${id}.root ]; then
      echo "${pnfsOutDir}/simScanCoarse_${id}.root already exists, skipping..."
      continue
    fi

    longFileName=${line#/pnfs/*}
    echo root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/${longFileName} >> xrootdFileList${fileNum}.txt
  done

  # Skip if file list is empty
  if [[ ! -s xrootdFileList${fileNum}.txt ]]; then
    echo "File list is empty, no job submitted"
    continue
  fi


  if [[ ! -s xrootdFileList${fileNum}.txt ]]; then
    echo "File list empty, no grid job submitted"
    continue
  fi

  echo "xrootdFileList${fileNum}.txt"
  ls ${pnfsOutDir}/*.root | wc -l
  cat xrootdFileList${fileNum}.txt

  # break
  # Copy fcl & .so file to pnfs so we can get it from grid jobs
  if [ -f ${pnfsOutDir}/xrootdFileList${fileNum}.txt ]; then
    rm -f ${pnfsOutDir}/xrootdFileList${fileNum}.txt 
  fi

  if [ -f ${pnfsOutDir}/RunSimAndPlotNominalScanCoarse.fcl ]; then
    rm -f ${pnfsOutDir}/RunSimAndPlotNominalScanCoarse.fcl  
  fi
  if [ -f ${pnfsOutDir}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so ]; then
    rm -f ${pnfsOutDir}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so
  fi

  sleep 5

  ifdh cp RunSimAndPlotNominalScanCoarse.fcl ${pnfsOutDir}/RunSimAndPlotNominalScanCoarse.fcl
  ifdh cp libgm2tracker_analyses_LowDCAsTruthPlots_module.so ${pnfsOutDir}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so
  ifdh cp xrootdFileList${fileNum}.txt ${pnfsOutDir}/xrootdFileList${fileNum}.txt

  echo "Copied RunSimAndPlotNominalScanCoarse.fcl, libgm2tracker_analyses_LowDCAsTruthPlots_module.so, and xrootdFileList${fileNum}.txt to ${pnfsOutDir}"


# Make script that we'll want to run on the grid
cat <<EOF > runCoarseScanJob${fileNum}.sh
# Setup stuff to copy files back and forth
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups
source /cvmfs/fermilab.opensciencegrid.org/products/larsoft/setup
setup ifdhc

# Copy xrootdFileList${fileNum} here
if [ ! -z "\`ifdh ls ${pnfsOutDir}/xrootdFileList${fileNum}.txt\`" ]; then
  ifdh cp ${pnfsOutDir}/xrootdFileList${fileNum}.txt xrootdFileList${fileNum}.txt
else 
  echo "${pnfsOutDir}/xrootdFileList${fileNum}.txt does not exist"
fi

#Copy fcl and .so files
if [ ! -z "\`ifdh ls ${pnfsOutDir}/RunSimAndPlotNominalScanCoarse.fcl\`" ]; then
  ifdh cp ${pnfsOutDir}/RunSimAndPlotNominalScanCoarse.fcl ./RunSimAndPlotNominalScanCoarse.fcl
else 
  echo "${pnfsOutDir}/RunSimAndPlotNominalScanCoarse.fcl does not exist"
fi
if [ ! -z "\`ifdh ls ${pnfsOutDir}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so\`" ]; then
  ifdh cp ${pnfsOutDir}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so ./libgm2tracker_analyses_LowDCAsTruthPlots_module.so
else 
  echo "${pnfsOutDir}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so does not exist"
fi

#Setup gm2
source /cvmfs/gm2.opensciencegrid.org/prod/g-2/setup
setup gm2 v9_45_00 -q prof

#Add current directory to LD_LIBRARY_PATH for so file we copied
export LD_LIBRARY_PATH=\`pwd\`:\$LD_LIBRARY_PATH

# Some nodes have newer kernels
case `uname -r` in
  3.*) export UPS_OVERRIDE="-H Linux64bit+2.6-2.12";;
  4.*) export UPS_OVERRIDE="-H Linux64bit+2.6-2.12";;
esac

#Run jobs
for file in \`cat xrootdFileList${fileNum}.txt\`; do
  echo "Processing \$file"

  id=\${file%_*}
  id=\${id##*_}

  gm2 -c RunSimAndPlotNominalScanCoarse.fcl -s \$file -T simScanCoarse_\${id}.root

  # Only copy back if job completed successfully (output from last command was 0)
  if [ \$? -eq 0 ]; then
    if [ -f simScanCoarse_\${id}.root ]; then
      ifdh mv simScanCoarse_\${id}.root ${pnfsOutDir}/simScanCoarse_\${id}.root
    else 
      echo "simScanCoarse_\${id}.root does not exist.  ls reads:"
      ls
    fi
  fi
done
EOF

  if [ -f ${pnfsOutDir}/runCoarseScanJob${fileNum}.sh ]; then
    rm -f ${pnfsOutDir}/runCoarseScanJob${fileNum}.sh
  fi
    ifdh cp runCoarseScanJob${fileNum}.sh ${pnfsOutDir}/runCoarseScanJob${fileNum}.sh
  while [ ! -f ${pnfsOutDir}/runCoarseScanJob${fileNum}.sh ]; do
    echo "${pnfsOutDir}/runCoarseScanJob${fileNum}.sh not found after ifdh cp.  Sleeping 5..."
    sleep 5
  done

  #Submit grid job
  jobsub_submit -N 1 -G gm2 --OS=SL6 --resource-provides=usage_model=DEDICATED,OPPORTUNISTIC --expected-lifetime=6h --memory=3GB --role=Analysis file://${pnfsOutDir}/runCoarseScanJob${fileNum}.sh
  rm -f runCoarseScanJob${fileNum}.sh
  rm -f xrootdFileList${fileNum}.txt
  rm -f SplitFileList${fileNum}.txt

 # 
  
done





