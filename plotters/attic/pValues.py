from ROOT import TFile, TH1
from plotFunc import LoadPlotFunc, FancyDraw1D

LoadPlotFunc()

# First set of plots
#fitMode = ["tracksTruthLR", "tracksMainFit", "tracksFullSeqFit"]
#config = ["vacuum_2um_allTimes_noMaterial_noBinning","vacuum_2um_allTimes_noMaterial_withBinning"]

# New
fitMode = ["tracksMainFit"]
# config = ["vacuum_2um_allTimes_noMaterial_noBinning"]
config = ["nominal"]
filters = ["noneWrongOneHitInView", "oneWrongSingleViewFirstLastModAllDCAs",  ] 


for i in range(len(fitMode)):

	for j in range(len(config)):

		for k in range(len(filters)):

			# If not truthLR, don't use the withBinning config
			#if(i>0 and j>0): continue
	
			# Get file
			file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filterPlots_"+filters[k]+".root")
			# file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/simPlots_"+config[j]+".root")
			print(file)
	
			# Get hist
			hist = file.Get("nonePlusWrongPlanesHitCut/pValues")
			print(hist)
	
			# Make plots
			FancyDraw1D(hist, ";p-values;Tracks", "../images/"+fitMode[i]+"/"+config[j]+"/pValues_"+filters[k])