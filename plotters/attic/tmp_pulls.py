# planesHit.py

# Make plots of the number of planes hit per track

from ROOT import TFile, TH1
from plotFunc import LoadPlotFunc, FancyDraw1D

LoadPlotFunc()

fitMode = ["tracksMainFit", "tracksFullSeqFit"]

# Left this as a list, in case you need to make more configs
config = ["vacuum_2um_allTimes_noMaterial_noBinning"]

filters = ["endHitsAllDCAs", "endHitsLowDCAs", "endHitsHighDCAs","nonEndHitsAllDCAs", "nonEndHitsLowDCAs", "nonEndHitsHighDCAs"]

for i in range(len(fitMode)):

	for j in range(len(config)):
		
		# Make plots for non filtered tracks
		
		# Get regular file
		file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/simPlots_"+config[j]+".root")
		print(file)

		# Grab all hits file
		h1 = file.Get("Pull");
		h2 = file.Get("WrongHits/Pull")
		h3 = file.Get("RightHits/Pull")
		print(h1)
		print(h2)
		print(h3)

		# Draw
		FancyDraw1D(h1, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/pullAllHits")
		FancyDraw1D(h2, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/pullWrongHits")
		FancyDraw1D(h3, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/pullRightHits")

		# Make plots for filtered tracks

		for k in range(len(filters)):

			# Make plots for non filtered tracks
		
			# Get regular file
			file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filteredPlots_"+filters[k]+".root")
			print(file)

			# Grab all hits file
			h4 = file.Get("Pull");
			h5 = file.Get("WrongHits/Pull")
			h6 = file.Get("RightHits/Pull")
			print(h4)
			print(h5)
			print(h6)

			# Draw
			FancyDraw1D(h1, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/pullAllHits")
			FancyDraw1D(h2, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/pullWrongHits")
			FancyDraw1D(h3, ";Hit pull;Hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/pullRightHits")