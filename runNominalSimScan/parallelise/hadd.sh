# Number of wrong hits
declare -a numWrong=("nonePlusWrong" "noneWrong" "oneWrong" "twoWrong" "threeWrong" "fourWrong" "fiveWrong" "fivePlusWrong")

for i in "${numWrong[@]}"; do

    cd $i

    hadd -f simPlots_fine.root file*/simPlots_fine.root
    hadd -f simPlots_coarse.root file*/simPlots_coarse.root
    
    cd ../

done