# planesHit.py

# Make plots of pulls 

from ROOT import TFile, TH1
from plotFunc import LoadPlotFunc, FancyDraw1D

LoadPlotFunc()

fitMode = ["tracksMainFit", "tracksTruthLR"]

# Left this as a list, in case you need to make more configs
config = ["vacuum_2um_allTimes_noMaterial_noBinning"]

# filters = ["endHitsAllDCAs", "endHitsLowDCAs", "endHitsHighDCAs","nonEndHitsAllDCAs", "nonEndHitsLowDCAs", "nonEndHitsHighDCAs"]
# filters = ["twoHitsInViewAllDCAs", "twoHitsInViewHighDCAs", "twoHitsInViewLowDCAs", "oneHitInViewAllDCAs", "oneHitInViewHighDCAs", "oneHitInViewLowDCAs"]
filters = ["notFirstOrLastModuleAllDCAs", "notFirstOrLastModuleHighDCAs", "notFirstOrLastModuleLowDCAs",
				"firstOrLastModuleAllDCAs", "firstOrLastModuleHighDCAs", "firstOrLastModuleLowDCAs",
 				"twoHitsInViewAllDCAs", "twoHitsInViewHighDCAs", "twoHitsInViewLowDCAs", 
 				"oneHitInViewAllDCAs", "oneHitInViewHighDCAs", "oneHitInViewLowDCAs", "oneHitOnly"]


for i in range(len(fitMode)):

	for j in range(len(config)):
		
		# Make plots for non filtered tracks
		
		# Get regular file
		file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/simPlots_"+config[j]+".root")
		print(file)

		# Grab all hits file
		h1 = file.Get("oneWrong/Pull"); # fine
		h2 = file.Get("oneWrong/WrongHits/Pull") # fine
		h3 = file.Get("oneWrong/RightHits/Pull") # fine
		# 12 planes hit cut
		h4 = file.Get("oneWrongPlanesHitCut/Pull"); # fine
		h5 = file.Get("oneWrongPlanesHitCut/WrongHits/Pull") # fine
		h6 = file.Get("oneWrongPlanesHitCut/RightHits/Pull") # fine
		print(h1)
		print(h2)
		print(h3)
		print(h4)
		print(h5)
		print(h6)

		# Draw
		FancyDraw1D(h1, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/pullAllHits")
		FancyDraw1D(h2, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/pullWrongHits")
		FancyDraw1D(h3, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/pullRightHits")
		# Draw
		FancyDraw1D(h4, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/pullAllHits12PlanesHitCut")
		FancyDraw1D(h5, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/pullWrongHits12PlanesHitCut")
		FancyDraw1D(h6, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/pullRightHits12PlanesHitCut")
		# Make plots for filtered tracks

		for k in range(len(filters)):

			# Make plots for non filtered tracks
		
			# Get regular file
			file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filteredPlots_"+filters[k]+".root")
			print(file)

			# Grab all hits file
			h7 = file.Get("oneWrong/Pull");
			h8 = file.Get("oneWrong/WrongHits/Pull")
			h9 = file.Get("oneWrong/RightHits/Pull")
			# 12 planes hit cut
			h10 = file.Get("oneWrongPlanesHitCut/Pull"); # fine
			h11 = file.Get("oneWrongPlanesHitCut/WrongHits/Pull") # fine
			h12 = file.Get("oneWrongPlanesHitCut/RightHits/Pull") # fine
			# TODO: ADD PLANES HIT CUT PLOTS
			print(h7)
			print(h8)
			print(h9)
			print(h10)
			print(h11)
			print(h12)

			# Draw
			FancyDraw1D(h7, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/pullAllHits")
			FancyDraw1D(h8, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/pullWrongHits")
			FancyDraw1D(h9, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/pullRightHits")
			# Draw
			FancyDraw1D(h10, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/pullAllHits12PlanesHitCut")
			FancyDraw1D(h11, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/pullWrongHits12PlanesHitCut")
			FancyDraw1D(h12, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/pullRightHits12PlanesHitCut")
