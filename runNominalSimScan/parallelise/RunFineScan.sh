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
	cp ../RunSimAndPlotNominalScanFine.fcl .

	echo "physics.analyzers.zero.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.one.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.two.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.three.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.four.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.five.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.six.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.seven.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.eight.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.nine.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.ten.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.eleven.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.twelve.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.thirteen.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.fourteen.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.fifteen.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.sixteen.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.seventeen.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.eighteen.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.nineteen.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 
	echo "physics.analyzers.twenty.${i} : true" >> RunSimAndPlotNominalScanFine.fcl 

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

	gm2 -c ../RunSimAndPlotNominalScanFine.fcl -s $filesToRun

	wait

	cd ../../

done
