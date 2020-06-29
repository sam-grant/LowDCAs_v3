fitmode="tracksTruthLR"

declare -a names=("notFirstOrLastModuleAllDCAs" "notFirstOrLastModuleHighDCAs" "notFirstOrLastModuleLowDCAs"
                                "firstOrLastModuleAllDCAs" "firstOrLastModuleHighDCAs" "firstOrLastModuleLowDCAs"
                                "twoHitsInViewAllDCAs" "twoHitsInViewHighDCAs" "twoHitsInViewLowDCAs"
                                "oneHitInViewAllDCAs" "oneHitInViewHighDCAs" "oneHitInViewLowDCAs")
#declare -a names=("oneHitAllDCAs" "oneHitHighDCAs" "oneHitLowDCAs")
for i in "${names[@]}"; do
    mkdir ../images/${fitMode}/vacuum_2um_allTimes_noMaterial_noBinning/${i}
done
    