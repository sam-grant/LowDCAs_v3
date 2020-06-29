# plot the number of tracks per filter condition

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import LoadPlotFunc, DefineScat, DrawScat
from ROOT import gROOT

LoadPlotFunc()

fitMode = ["tracksMainFit"] #, "tracksFullSeqFit"]

# Left this as a list, in case you need to make more configs
config = ["vacuum_2um_allTimes_noMaterial_noBinning"]

# filters = ["endHitsAllDCAs", "endHitsLowDCAs", "endHitsHighDCAs","nonEndHitsAllDCAs", "nonEndHitsLowDCAs", "nonEndHitsHighDCAs"]
filters = ["oneHitInViewAllDCAs", "oneHitInViewHighDCAs", "oneHitInViewLowDCAs", "twoHitsInViewAllDCAs", "twoHitsInViewHighDCAs", "twoHitsInViewLowDCAs"]
#filters = ["notFirstOrLastModuleAllDCAs", "notFirstOrLastModuleHighDCAs", "notFirstOrLastModuleLowDCAs",
#				"firstOrLastModuleAllDCAs", "firstOrLastModuleHighDCAs", "firstOrLastModuleLowDCAs",
# 				"twoHitsInViewAllDCAs", "twoHitsInViewHighDCAs", "twoHitsInViewLowDCAs", 
# 				"oneHitInViewAllDCAs", "oneHitInViewHighDCAs", "oneHitInViewLowDCAs"]


for i in range(len(fitMode)):

	for j in range(len(config)):

		# List for tracks
		tracks = []

		for k in range(len(filters)):

			# Make plots for non filtered tracks
		
			# Get regular file
			file = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filteredPlots_"+filters[k]+".root")
			print(file)

			# Grab all hits file
			h1 = file.Get("oneWrong/Run");
			print(h1)

			tracks.append(h1.GetEntries())

		# Now plot them against the string corresponding describing their filter condition

		print(len(tracks))

		for i_filter in range(len(tracks)):

			tgr = DefineScat([1,2,3,4,5,6], tracks)

			# if(i_filter==0): # only need to do this once
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(0 + 1.),"One")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(1 + 1.),"One, low DCA")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(2 + 1.),"One, high DCA")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(3 + 1.),"Two")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(4 + 1.),"Two, low DCA")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(5 + 1.),"Two, high DCA")
			tgr.GetXaxis().LabelsOption("h")
				# tgr.GetHistogram().SetMinimum(0)
				# tgr.GetHistogram().SetMaximum(2500)
			# tgr_.append(tgr)


		DrawScat(tgr,";Filter condition, wrong hits / view;Tracks", "../images/"+fitMode[i]+"/"+config[j]+"/tracksPerFilter")