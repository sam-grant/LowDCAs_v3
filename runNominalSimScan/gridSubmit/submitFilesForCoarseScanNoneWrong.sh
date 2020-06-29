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

# Split into list with 15 each
echo "Splitting file list" 
rm -f SplitFileList*
split MainFileList.txt -l 15 -a 3 -d SplitFileList
for file in `ls SplitFileList*`; do 
  mv $file ${file}.txt
done

# Make output directory
pnfsOutDir=/pnfs/GM2/scratch/users/${USER}/LowDCAsScans/CoarseNoneWrong

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
  mkdir -p ${pnfsOutDir}/${fileNum}
  chmod -R g+w ${pnfsOutDir}/${fileNum}

  rm -f xrootFileList${fileNum}.txt && touch xrootdFileList${fileNum}.txt

  for line in `cat $file`; do

    id=${line%_*}
    id=${id##*_}
    # Skip files already written
    if [ -f ${pnfsOutDir}/${fileNum}/simScanCoarseNoneWrong_${id}.root ]; then
      echo "${pnfsOutDir}/${fileNum}/simScanCoarseNoneWrong_${id}.root already exists, skipping..."
      continue
    fi

    # Strip /pnfs/ from file name and write into new file
    longFileName=${line#/pnfs/*}
    echo root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/${longFileName} >> xrootdFileList${fileNum}.txt
  done

  echo "xrootdFileList${fileNum}.txt"
  ls ${pnfsOutDir}/${fileNum}/*.root | wc -l
  cat xrootdFileList${fileNum}.txt

  # Copy fcl & .so file to pnfs so we can get it from grid jobs
  if [ -f ${pnfsOutDir}/${fileNum}/xrootdFileList${fileNum}.txt ]; then
    rm -f ${pnfsOutDir}/${fileNum}/xrootdFileList${fileNum}.txt 
  fi

  if [ -f ${pnfsOutDir}/${fileNum}/RunSimAndPlotNominalScanCoarseNoneWrong.fcl ]; then
    rm -f ${pnfsOutDir}/${fileNum}/RunSimAndPlotNominalScanCoarseNoneWrong.fcl  
  fi
  if [ -f ${pnfsOutDir}/${fileNum}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so ]; then
    rm -f ${pnfsOutDir}/${fileNum}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so
  fi

  sleep 5

  ifdh cp RunSimAndPlotNominalScanCoarseNoneWrong.fcl ${pnfsOutDir}/${fileNum}/RunSimAndPlotNominalScanCoarseNoneWrong.fcl
  ifdh cp libgm2tracker_analyses_LowDCAsTruthPlots_module.so ${pnfsOutDir}/${fileNum}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so
  ifdh cp xrootdFileList${fileNum}.txt ${pnfsOutDir}/${fileNum}/xrootdFileList${fileNum}.txt

  echo "Copied RunSimAndPlotNominalScanCoarseNoneWrong.fcl, libgm2tracker_analyses_LowDCAsTruthPlots_module.so, and xrootdFileList${fileNum} to ${pnfsOutDir}/${fileNum}"


# Make script that we'll want to run on the grid
cat <<EOF > runCoarseScanNoneWrongJob${fileNum}.sh
# Setup stuff to copy files back and forth
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups
source /cvmfs/fermilab.opensciencegrid.org/products/larsoft/setup
setup ifdhc

# Copy xrootdFileList${fileNum} here
if [ ! -z "\`ifdh ls ${pnfsOutDir}/${fileNum}/xrootdFileList${fileNum}.txt\`" ]; then
  ifdh cp ${pnfsOutDir}/${fileNum}/xrootdFileList${fileNum}.txt xrootdFileList${fileNum}.txt
else 
  echo "${pnfsOutDir}/${fileNum}/xrootdFileList${fileNum}.txt does not exist"
fi

#Copy fcl and .so files
if [ ! -z "\`ifdh ls ${pnfsOutDir}/${fileNum}/RunSimAndPlotNominalScanCoarseNoneWrong.fcl\`" ]; then
  ifdh cp ${pnfsOutDir}/${fileNum}/RunSimAndPlotNominalScanCoarseNoneWrong.fcl ./RunSimAndPlotNominalScanCoarseNoneWrong.fcl
else 
  echo "${pnfsOutDir}/${fileNum}/RunSimAndPlotNominalScanCoarseNoneWrong.fcl does not exist"
fi
if [ ! -z "\`ifdh ls ${pnfsOutDir}/${fileNum}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so\`" ]; then
  ifdh cp ${pnfsOutDir}/${fileNum}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so ./libgm2tracker_analyses_LowDCAsTruthPlots_module.so
else 
  echo "${pnfsOutDir}/${fileNum}/libgm2tracker_analyses_LowDCAsTruthPlots_module.so does not exist"
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

  gm2 -c RunSimAndPlotNominalScanCoarseNoneWrong.fcl -s \$file -T simScanCoarseNoneWrong_\${id}.root

  # Only copy back if job completed successfully (output from last command was 0)
  if [ \$? -eq 0 ]; then
    if [ -f simScanCoarseNoneWrong_\${id}.root ]; then
      ifdh mv simScanCoarseNoneWrong_\${id}.root ${pnfsOutDir}/${fileNum}/simScanCoarseNoneWrong_\${id}.root
    else 
      echo "simScanCoarseNoneWrong_\${id}.root does not exist.  ls reads:"
      ls
    fi
  fi
done
EOF

  if [ -f ${pnfsOutDir}/${fileNum}/runCoarseScanNoneWrongJob${fileNum}.sh ]; then
    rm -f ${pnfsOutDir}/${fileNum}/runCoarseScanNoneWrongJob${fileNum}.sh
  fi
    ifdh cp runCoarseScanNoneWrongJob${fileNum}.sh ${pnfsOutDir}/${fileNum}/runCoarseScanNoneWrongJob${fileNum}.sh
  while [ ! -f ${pnfsOutDir}/${fileNum}/runCoarseScanNoneWrongJob${fileNum}.sh ]; do
    echo "${pnfsOutDir}/${fileNum}/runCoarseScanNoneWrongJob${fileNum}.sh not found after ifdh cp.  Sleeping 5..."
    sleep 5
  done

  #Submit grid job
  jobsub_submit -N 1 -G gm2 --OS=SL6 --resource-provides=usage_model=DEDICATED,OPPORTUNISTIC --expected-lifetime=6h --role=Analysis file://${pnfsOutDir}/${fileNum}/runCoarseScanNoneWrongJob${fileNum}.sh
  rm -f runCoarseScanNoneWrongJob${fileNum}.sh
  rm -f xrootdFileList${fileNum}.txt
  rm -f SplitFileList${fileNum}.txt

done





