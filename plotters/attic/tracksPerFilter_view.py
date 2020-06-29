# plot the number of tracks per filter condition

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import *
from ROOT import gROOT

LoadPlotFunc()

fitMode = ["tracksMainFit"] #, "tracksFullSeqFit"]

# Left this as a list, in case you need to make more configs
# config = ["vacuum_2um_allTimes_noMaterial_noBinning"]
config = ["nominal", "nominal_lock500"]

filters1 = ["oneWrongSingleViewFirstLastModAllDCAs", "oneWrongSingleViewFirstLastModLowDCAs", "oneWrongSingleViewFirstLastModHighDCAs"]
filters2 = ["oneWrongNotSingleViewFirstLastModAllDCAs", "oneWrongNotSingleViewFirstLastModLowDCAs", "oneWrongNotSingleViewFirstLastModHighDCAs"]

for i in range(len(fitMode)):

	for j in range(len(config)):

		plotMode = ["oneWrong", "oneWrongPlanesHitCut","oneWrongPlanesHitCutPValueCut"]

		for h in range(len(plotMode)):

			print(plotMode[h])

			# List for tracks
			tracks1 = []
			tracks2 = []			
	
			for k in range(len(filters1)):
			
				# Get regular file
				file1 = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filterPlots_"+filters1[k]+".root")
				file2 = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filterPlots_"+filters2[k]+".root")
				print(file1)
				print(file2)
	
				# Grab all hits file
				h1 = file1.Get(plotMode[h]+"/Run");
				h2 = file2.Get(plotMode[h]+"/Run");
				print(h1)
				print(h2)
	
				print("Entries (one hit) ",h1.GetEntries())
				print("Entries (two hit) ",h2.GetEntries())
	
				print(h2.GetEntries())
				# print("Fraction",100*round(1- (h2.GetEntries()/h1.GetEntries())))
				# print("Percentage ",round(100*(1-(h2.GetEntries()/h1.GetEntries()))))
				tracks1.append(h1.GetEntries())
				tracks2.append(h2.GetEntries())
				
	
	
			# Now plot them against the string corresponding describing their filter condition
	
			print(len(tracks1))
	
			for i_filter in range(len(tracks1)):
	
				tgr1 = DefineScat([1,2,3], tracks1)
				tgr2 = DefineScat([1,2,3], tracks2)
				
				tgr1.GetXaxis().SetBinLabel(tgr1.GetXaxis().FindBin(0 + 1.),"All DCAS")
				tgr1.GetXaxis().SetBinLabel(tgr1.GetXaxis().FindBin(1 + 1.),"DCAs < 500 #mum")
				tgr1.GetXaxis().SetBinLabel(tgr1.GetXaxis().FindBin(2 + 1.),"DCAs > 2000 #mum")
				tgr2.GetXaxis().SetBinLabel(tgr2.GetXaxis().FindBin(0 + 1.),"All DCAS")
				tgr2.GetXaxis().SetBinLabel(tgr2.GetXaxis().FindBin(1 + 1.),"DCAs < 500 #mum")
				tgr2.GetXaxis().SetBinLabel(tgr2.GetXaxis().FindBin(2 + 1.),"DCAs > 2000 #mum")
				
				tgr1.GetXaxis().LabelsOption("h")
				tgr2.GetXaxis().LabelsOption("h")
	
			tgr1.SetMinimum(0)
			DrawScatOverlay(tgr1,tgr2,"Wrong hit alone in view","Wrong hit not alone in view",";Filter condition on wrong hits in the first/last modules;Tracks with one wrong hit", "../images/"+fitMode[i]+"/"+config[j]+"/tracksPerFilter_"+plotMode[h]+"_view")

