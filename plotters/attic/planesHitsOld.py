# pulls.py

# Make plots of the hit pulls for AllHits, WrongHits, and RightHits

from ROOT import TFile, TH1
from plotFunc import LoadPlotFunc, FancyDraw1D

LoadPlotFunc()

fitMode = ["tracksMainFit"] #, "tracksFullSeqFit"]

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

		# Grab plain DCA histograms (denominator)
		h1 = file.Get("oneWrong/PlanesHit");
		# h1 = file.Get("oneWrong/WrongHit/PlanesHit");
		print(h1)

		h1.SetStats(0)

		# Draw denominator
		FancyDraw1D(h1, ";Planes hit;Tracks","../images/"+fitMode[i]+"/"+config[j]+"/planesHit")

		# Make plots for filtered tracks

		for k in range(len(filters)):

			# Make plots for non filtered tracks
		
			# Get regular file
			file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filteredPlots_"+filters[k]+".root")
			print(file)

			# Grab plain DCA histograms (denominator)
			h2 = file.Get("oneWrong/PlanesHit");
			print(h2)

			h2.SetStats(0)

			# Draw denominator
			FancyDraw1D(h2, ";Planes hit;Tracks","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/planesHit")
