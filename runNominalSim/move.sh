declare -a numWrong=("nonePlusWrong" "noneWrong" "oneWrong" "twoWrong" "threeWrong" "fourWrong" "fiveWrong" "fivePlusWrong")

for i in "${numWrong[@]}"; do

    mv $i parellelise

done