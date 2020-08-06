
# Standard stuff
source /grid/fermiapp/products/common/etc/setups.sh
setup jobsub_client
setup fife_utils

# xrootdFile=root://fndca1.fnal.gov:1094
file=root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/GM2/daq/run1/offline/gm2_5037A/runs_15000/15921/gm2offline_full_17632340_15921.00313.root 

pnfsOutDir=/pnfs/GM2/scratch/users/${USER}/pValueScanMainFitEnhanced2

if [ ! -d $pnfsOutDir ]; then
  mkdir -p $pnfsOutDir
  chmod -R g+w $pnfsOutDir
fi

echo "Output files will appear in $pnfsOutDir"

if [ -f ${pnfsOutDir}/libgm2tracker_analyses_LowDCAsPlots_module.so ]; then
   rm -f ${pnfsOutDir}/libgm2tracker_analyses_LowDCAsPlots_module.so
fi
if [ -f ${pnfsOutDir}/libgm2tracker_reco_GeaneReco_module.so ]; then
   rm -f ${pnfsOutDir}/libgm2tracker_reco_GeaneReco_module.so
fi

sleep 5

ifdh cp libgm2tracker_analyses_LowDCAsPlots_module.so ${pnfsOutDir}/libgm2tracker_analyses_LowDCAsPlots_module.so
ifdh cp libgm2tracker_reco_GeaneReco_module.so ${pnfsOutDir}/libgm2tracker_reco_GeaneReco_module.so

# pValue low cut
declare -a loCut=("0.0000" "0.0001" "0.0002" "0.0003" "0.0004" "0.0005" "0.0006" "0.0007" "0.0008" "0.0009" "0.0010" "0.0020" "0.0030" "0.0040" "0.0050" "0.0060" "0.0070" "0.0080" "0.0090" "0.0100" "0.0110" "0.0120" "0.0130" "0.0140" "0.0150" "0.0160" "0.0170" "0.0180" "0.0190" "0.0200" "0.0250" "0.0300" "0.0400" "0.0450")

for i in "${loCut[@]}"; do

	rm -f fcl/${i}.fcl && cp base.fcl fcl/${i}.fcl

	echo "services.TFileService.fileName : '${i}.root'" >> fcl/${i}.fcl
	echo "physics.producers.tracks.pValueCutLo : '${i}'" >> fcl/${i}.fcl

	echo "Copied files"

	if [ -f ${pnfsOutDir}/${i}.fcl  ]; then
	   rm -f ${pnfsOutDir}/${i}.fcl 
	fi

	ifdh cp fcl/${i}.fcl ${pnfsOutDir}/${i}.fcl 

# Make script that we'll want to run on the grid
cat <<EOF > runJob${i}.sh

# Setup stuff to copy files back and forth
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups
source /cvmfs/fermilab.opensciencegrid.org/products/larsoft/setup
setup ifdhc

#Copy fcl and .so files
if [ ! -z "\`ifdh ls ${pnfsOutDir}/${i}.fcl\`" ]; then
  ifdh cp ${pnfsOutDir}/${i}.fcl ./${i}.fcl
else 
  echo "${pnfsOutDir}/${i}.fcl does not exist"
fi
if [ ! -z "\`ifdh ls ${pnfsOutDir}/libgm2tracker_analyses_LowDCAsPlots_module.so\`" ]; then
  ifdh cp ${pnfsOutDir}/libgm2tracker_analyses_LowDCAsPlots_module.so ./libgm2tracker_analyses_LowDCAsPlots_module.so
else 
  echo "${pnfsOutDir}/libgm2tracker_analyses_LowDCAsPlots_module.so does not exist"
fi
if [ ! -z "\`ifdh ls ${pnfsOutDir}/libgm2tracker_reco_GeaneReco_module.so\`" ]; then
  ifdh cp ${pnfsOutDir}/libgm2tracker_reco_GeaneReco_module.so ./libgm2tracker_reco_GeaneReco_module.so
else 
  echo "${pnfsOutDir}/libgm2tracker_reco_GeaneReco_module.so does not exist"
fi

#Setup gm2
source /cvmfs/gm2.opensciencegrid.org/prod/g-2/setup
setup gm2 v9_49_00 -q prof

#Add current directory to LD_LIBRARY_PATH for so file we copied
export LD_LIBRARY_PATH=\`pwd\`:\$LD_LIBRARY_PATH

# Some nodes have newer kernels
case `uname -r` in
  3.*) export UPS_OVERRIDE="-H Linux64bit+2.6-2.12";;
  4.*) export UPS_OVERRIDE="-H Linux64bit+2.6-2.12";;
esac

gm2 -c ${i}.fcl -s ${file} -T recoPlots${i}.root | tee ${i}.txt

# Only copy back if job completed successfully (output from last command was 0)
if [ \$? -eq 0 ]; then
	if [ -f recoPlots${i}.root ]; then
    	ifdh mv recoPlots${i}.root ${pnfsOutDir}/recoPlots${i}.root
    else 
    	echo "recoPlots${i}.root does not exist.  ls reads:"
    	ls
    fi
    if [ -f ${i}.txt ]; then
    	ifdh mv ${i}.txt ${pnfsOutDir}/${i}.txt
    else 
    	echo "${i}.txt does not exist.  ls reads:"
    	ls
    fi
fi
EOF

  if [ -f ${pnfsOutDir}/runJob${i}.sh ]; then
    rm -f ${pnfsOutDir}/runJob${i}.sh
  fi
    ifdh cp runJob${i}.sh ${pnfsOutDir}/runJob${i}.sh
  while [ ! -f ${pnfsOutDir}/runJob${i}.sh ]; do
    echo "${pnfsOutDir}/runJob${i}.sh not found after ifdh cp.  Sleeping 5..."
    sleep 5
  done

  #Submit grid job
  jobsub_submit -N 1 -G gm2 --OS=SL6 --resource-provides=usage_model=DEDICATED,OPPORTUNISTIC --expected-lifetime=4h --memory=3GB --role=Analysis file://${pnfsOutDir}/runJob${i}.sh
  rm -f runJob${i}.sh

  # break

done