# Label piped input file
inFile="/pnfs/GM2/mc/run1_gasgun_1062/runs_1567190000/1567190852/gm2ringsim_muon_gasgun_truth_22551240_1567190852.1.root"
 # $1

# Number of wrong hits
cd test

# Define output path
pwd
# Copy and append fcl file with wrong hits
cp ../RunSimAndPlotNominalScanCoarse.fcl .

#mkdir $inFile

#cd $inFile
#cp ../files/$inFile .

pwd

# Get the list of root files
#filesToRun=""
#for line in `cat $inFile`; do
#    filesToRun=$filesToRun" "$line
#done

#echo $filesToRun

gm2 -c ../RunSimAndPlotNominalScanCoarse.fcl -s $inFile #filesToRun

wait

cd ../


