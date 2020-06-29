# Make plots of the number of planes hit for tracks of high DCA

from ROOT import TFile, TH1
from plotFunc import LoadPlotFunc, FancyDraw1D

LoadPlotFunc()

fitMode = ["mainFit"] #, "tracksFullSeqFit"]

# Left this as a list, in case you need to make more configs
config = ["optimal"] #"vacuum_2um_allTimes_noMaterial_noBinning"]

# filters = ["endHitsAllDCAs", "endHitsLowDCAs", "endHitsHighDCAs","nonEndHitsAllDCAs", "nonEndHitsLowDCAs", "nonEndHitsHighDCAs"]
# filters = ["twoHitsInViewAllDCAs", "twoHitsInViewHighDCAs", "twoHitsInViewLowDCAs", "oneHitInViewAllDCAs", "oneHitInViewHighDCAs", "oneHitInViewLowDCAs"]
filters = ["oneWrongAnyViewFirstLastModAllDCAs", "oneWrongAnyViewFirstLastModHighDCAs"] 

 				
for i in range(len(fitMode)):

	for j in range(len(config)):
		
		# Make plots for non filtered tracks
		
		# Get regular file
		file = TFile.Open("../plots/"+config[i]+"/"+fitMode[j]+"/0/simPlots.root")
		print(file)

		# Grab plain DCA histograms (denominator)
		h1 = file.Get("noFlip/PlanesHit");
		# h1 = file.Get("oneWrong/WrongHit/PlanesHit");
		print(h1)

		h1.SetStats(0)

		# Draw denominator
		FancyDraw1D(h1, ";Planes hit;Tracks","../images/"+config[i]+"/"+fitMode[j]+"/planesHit")

		# Make plots for filtered tracks

		for k in range(len(filters)):

			# Make plots for non filtered tracks
		
			# Get regular file
			file = TFile.Open("../plots/"+config[i]+"/"+fitMode[j]+"/0/filterPlots_"+filters[k]+".root")
			print(file)

			# Grab plain DCA histograms (denominator)
			h2 = file.Get("oneWrong/PlanesHit");
			print(h2)

			h2.SetStats(0)

			# Draw denominator
			FancyDraw1D(h2, ";Planes hit;Tracks","../images/"+config[i]+"/"+fitMode[j]+"/"+filters[k]+"/planesHit")
