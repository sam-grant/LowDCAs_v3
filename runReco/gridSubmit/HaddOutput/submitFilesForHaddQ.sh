# Check that samweb and root are installed
command -v samweb >/dev/null 2>&1 || { echo >&2 "samweb not found. You want:"; echo "source /grid/fermiapp/products/common/etc/setups.sh"; echo "setup fife_utils"; return; }

command -v hadd >/dev/null 2>&1 || { echo >&2 "hadd not found. You want:"; echo "source /cvmfs/gm2.opensciencegrid.org/prod/g-2/setup && setup root v6_12_04 -q e15:prof"; return; }


# Get arguments (sam dataset and number of cores to use)
if [ "$#" -ne 1 ]; then
  echo "Number of cores to use required as arguments"
  return
fi

# dataset=$1
nCores=$1

# Make sub-directory (so we can do more than one)
# if [ -d $dataset ]; then
#   echo "Output directory $dataset already exists."
#   return
# fi
mkdir Q
cd Q
pwd

pnfsInDir=/pnfs/GM2/scratch/users/${USER}/LowDCAsNominalSim/Q

#Make sure file list exists
if [ ! -f ../commonFilesForHadd.txt ] || [ `cat ../commonFilesForHadd.txt | wc -l` -eq 0 ]; then
  echo "Input file list \"commonFilesForHadd.txt\" is required.  This was not found or has 0 entries"
  return
fi

# Really really dumb way of doing this

# Split into list with 15 each
echo "Splitting file list" 
rm -f SplitFileList*
split ../commonFilesForHadd.txt -l 15 -a 3 -d SplitFileList
for file in `ls SplitFileList*`; do 
  mv $file ${file}.txt
done

for file in `ls SplitFileList*`; do 

  fileNum=${file##SplitFileList}
  fileNum=${fileNum%.txt}

  ls ${pnfsInDir}/${fileNum}/*.root >> FileList_${fileNum}.txt

done

rm -f SplitFileList*

# Loop over all the file lists we've made and submit them for hadd
for file in `ls FileList_*.txt`; do run=${file##*FileList_}; run=${run%%.*}; echo $run; done | xargs -i --max-procs=$nCores bash -c ". ../haddFileListQ.sh {}"

echo "Performing final hadd"

hadd -f nominalSimPlotsQ.root */nominalSimPlotsQ_*.root

cd ../