# measuredDCAPlotter.py

# Make plots of the fraction of wrong hits for tracks with one wrong hit per track

from ROOT import TFile, TH1
from plotFunc import LoadPlotFunc, FancyDraw1D
from utils import LoadUtils, Ratio

LoadPlotFunc()
LoadUtils()

fitMode = ["tracksMainFit", "tracksFullSeqFit"]

# Left this as a list, in case you need to make more configs
config = ["vacuum_2um_allTimes_noMaterial_noBinning"]

# filters = ["endHitsAllDCAs", "endHitsLowDCAs", "endHitsHighDCAs","nonEndHitsAllDCAs", "nonEndHitsLowDCAs", "nonEndHitsHighDCAs"]
filters = ["twoHitsInViewAllDCAs", "twoHitsInViewHighDCAs", "twoHitsInViewLowDCAs", "oneHitInViewAllDCAs", "oneHitInViewHighDCAs", "oneHitInViewLowDCAs", "oneHitOnly"]

for i in range(len(fitMode)):

	for j in range(len(config)):
		
		# Make plots for non filtered tracks
		
		# Get regular file
		file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/simPlots_"+config[j]+".root")
		print(file)

		# Grab plain DCA histograms (denominator)
		h1 = file.Get("oneWrong/DCA");
		print(h1)

		# Sort out axis
		h1.GetXaxis().SetRangeUser(0,2500)

		# Draw denominator
		FancyDraw1D(h1, ";Measured DCA [#mum];Hits","../images/"+fitMode[i]+"/"+config[j]+"/measDCAOneWrong")

		# Get wrong hits histograms (numerator)
		h2 = file.Get("oneWrong/WrongHits/DCA")

		# Make ratio hist
		ratio = Ratio(h2, h1)
		print(ratio)

		# Remove stat box for this one
		ratio.SetStats(0)

		# Sort out axis
		ratio.GetXaxis().SetRangeUser(0,2500)

		# Draw ratio
		FancyDraw1D(ratio, ";Measured DCA [#mum];Fraction of wrong LR hits","../images/"+fitMode[i]+"/"+config[j]+"/fracWrongMeasDCAsOneWrong")

		# Make plots for filtered tracks

		for k in range(len(filters)):

			# Make plots for non filtered tracks
		
			# Get regular file
			file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filteredPlots_"+filters[k]+".root")
			print(file)

			# Grab plain DCA histograms (denominator)
			h1 = file.Get("oneWrong/DCA");
			print(h1)

			# Sort out axis
			h1.GetXaxis().SetRangeUser(0,2500)

			# Draw denominator
			FancyDraw1D(h1, ";Measured DCA [#mum];Hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/measDCAOneWrong")

			# Get wrong hits histograms (numerator)
			h2 = file.Get("oneWrong/WrongHits/DCA")

			# Make ratio hist
			ratio = Ratio(h2, h1)
			print(ratio)

			# Remove stat box for this one
			ratio.SetStats(0)

			# Sort out axis
			ratio.GetXaxis().SetRangeUser(0,2500)

			# Draw ratio
			FancyDraw1D(ratio, ";Measured DCA [#mum];Fraction of wrong LR hits","../images/"+fitMode[i]+"/"+config[j]+"/"+filters[k]+"/fracWrongMeasDCAsOneWrong")
