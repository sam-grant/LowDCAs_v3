# Label piped input file
inFile=$1

# Number of wrong hits
declare -a numWrong=("noneWrong" "oneWrong" "twoWrong" "threeWrong" "fourWrong" "fiveWrong" "fivePlusWrong")

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
	echo "physics.analyzers.zero.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.one.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.two.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.three.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.four.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.five.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.six.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.seven.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.eight.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.nine.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.ten.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.eleven.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twelve.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.thirteen.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.fourteen.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.fifteen.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.sixteen.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.seventeen.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.eighteen.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.nineteen.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twenty.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twentyOne.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twentyTwo.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twentyThree.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twentyFour.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twentyFive.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twentySix.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twentySeven.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twentyEight.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.twentyNine.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.thirty.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.thirtyOne.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.thirtyTwo.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.thirtyThree.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.thirtyFour.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.thirtyFive.${i} : true" >> RunSimAndPlotNominal.fcl 
	echo "physics.analyzers.thirtySix.${i} : true" >> RunSimAndPlotNominal.fcl 

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
