# Label piped input file
inFile=$1

# Number of wrong hits
declare -a numWrong=("nonePlusWrong" "noneWrong" "oneWrong" "twoWrong" "threeWrong" "fourWrong" "fiveWrong" "fivePlusWrong")

# Define output path

for i in "${numWrong[@]}"; do

	mkdir $i
	cd $i

	pwd
	# Copy and append fcl file with wrong hits
	cp ../RunSimAndPlotNominal.fcl .

	echo "physics.analyzers.trackPlotsFlipLR.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.trackPlotsMainFit.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.trackPlotsTruthLR.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.trackPlotsFullSeqFit.${i} : true" >> RunSimAndPlotNominal.fcl 
	
	# Now run sim

	mkdir $inFile

	cd $inFile
	cp ../../files/$inFile .

	pwd

	# Get the list of root files
	filesToRun=""
	for line in `cat $inFile`; do
  		filesToRun=$filesToRun" "$line
	done

	echo $filesToRun

	gm2 -c ../RunSimAndPlotNominal.fcl -s $filesToRun

	wait

	cd ../../

done
