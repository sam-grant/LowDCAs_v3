# wrongHitPos.py

# Make plots of wrong hit position, normalised through track

# measuredDCAPlotter.py

# Make plots of the fraction of wrong hits for tracks with one wrong hit per track

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

		# No planes hit condition
		# No DCA condition
		for i_plane in range(9,15):
			name = "oneWrong/WrongHits/WrongHitPos"+str(i_plane)
			h1 = file.Get(name)
			print(h1)
			h1.SetStats(0)
			FancyDraw1D(h1, ";Wrong hit position;Wrong LR hits","../images/"+fitMode[i]+"/"+config[j]+"/wrongHitPos"+str(i_plane))
		# High DCAs
		for i_plane in range(9,15):
			name = "oneWrong/WrongHitsDCA2000/WrongHitPos"+str(i_plane)
			h2 = file.Get(name)
			print(h2)
			h2.SetStats(0)
			FancyDraw1D(h2, ";Wrong hit position;Wrong LR hits","../images/"+fitMode[i]+"/"+config[j]+"/wrongHitPosHighDCA"+str(i_plane))
		# Low DCAs
		for i_plane in range(9,15):
			name = "oneWrong/WrongHitsDCA500/WrongHitPos"+str(i_plane)
			h3 = file.Get(name)
			print(h3)
			h3.SetStats(0)
			FancyDraw1D(h3, ";Wrong hit position;Wrong LR hits","../images/"+fitMode[i]+"/"+config[j]+"/wrongHitPosLowDCA"+str(i_plane))

		# Make plots for filtered tracks

		for k in range(len(filters)):

			# Make plots for non filtered tracks
		
			file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filteredPlots_"+filters[k]+".root")
			print(file)

			for j_plane in range(9,15):
				name = "oneWrong/WrongHits/WrongHitPos"+str(j_plane)
				h4 = file.Get(name)
				print(h4)
				h4.SetStats(0)
				FancyDraw1D(h4, ";Wrong hit position;Wrong LR hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/wrongHitPos"+str(j_plane))
