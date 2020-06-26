# Number of wrong hits
declare -a numWrong=("nonePlusWrong" "noneWrong" "oneWrong" "twoWrong" "threeWrong" "fourWrong" "fiveWrong" "fivePlusWrong")

for i in "${numWrong[@]}"; do

    cd $i

    hadd -f simPlots.root file*/simPlots.root
    
    cd ../

done