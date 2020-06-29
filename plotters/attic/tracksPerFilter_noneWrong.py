# plot the number of tracks per filter condition

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import *
from ROOT import gROOT

LoadPlotFunc()

fitMode = ["tracksMainFit"] #, "tracksFullSeqFit"]

# Left this as a list, in case you need to make more configs
# config = ["vacuum_2um_allTimes_noMaterial_noBinning"]
config = ["nominal", "nominal_lock500"]

filters0 = ["nonePlusWrongOneHitInView", "nonePlusWrongTwoHitsInView"]
filters1 = ["noneWrongOneHitInView", "noneWrongTwoHitsInView"]
filters2 = ["oneWrongSingleViewFirstLastModAllDCAs", "oneWrongNotSingleViewFirstLastModAllDCAs"]

for i in range(len(fitMode)):

	for j in range(len(config)):

		plotMode = ["nonePlusWrong", "nonePlusWrongPlanesHitCut" ,"nonePlusWrongPlanesHitCutPValueCut"]

		for h in range(len(plotMode)):

			print(plotMode[h])
			# List for tracks
			tracks0 = []
			tracks1 = []
			tracks2 = []

			tracks0.append(0)
			tracks1.append(0)
			tracks2.append(0)

			for k in range(len(filters1)):
			
				# Get file
				file0 = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filterPlots_"+filters0[k]+".root")
				file1 = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filterPlots_"+filters1[k]+".root")
				file2 = TFile.Open("../runSimPlots_v2/"+fitMode[i]+"/"+config[j]+"/filterPlots_"+filters2[k]+".root")
				print(file0)
				print(file1)
				print(file2)
	
				# Grab all hits file
				h0 = file0.Get(plotMode[h]+"/Run");
				h1 = file1.Get(plotMode[h]+"/Run");
				h2 = file2.Get(plotMode[h]+"/Run");
				print(h0)
				print(h1)
				print(h2)
	
				print("nonePlusWrong",h0.GetEntries())
				print("noneWrong ",h1.GetEntries())
				print("oneWrong ",h2.GetEntries())
	
				# print(h2.GetEntries())
				# print("Fraction",100*round(1- (h2.GetEntries()/h1.GetEntries())))
				# print("Percentage ",round(100*(1-(h2.GetEntries()/h1.GetEntries()))))
				tracks0.append(h0.GetEntries())
				tracks1.append(h1.GetEntries())
				tracks2.append(h2.GetEntries())
	
			print(len(tracks1))
	
			tracks0.append(0)
			tracks1.append(0)
			tracks2.append(0)
	
			for i_filter in range(len(tracks1)):
	
				tgr0 = DefineScat([1,2,3,4], tracks0)
				tgr1 = DefineScat([1,2,3,4], tracks1)
				tgr2 = DefineScat([1,2,3,4], tracks2)
	
				tgr0.GetXaxis().SetBinLabel(tgr1.GetXaxis().FindBin(1 + 1.),"View with single hit")
				tgr0.GetXaxis().SetBinLabel(tgr1.GetXaxis().FindBin(2 + 1.),"No view with single hit")			
				tgr1.GetXaxis().SetBinLabel(tgr1.GetXaxis().FindBin(1 + 1.),"View with single hit")
				tgr1.GetXaxis().SetBinLabel(tgr1.GetXaxis().FindBin(2 + 1.),"No view with single hit")
				tgr2.GetXaxis().SetBinLabel(tgr2.GetXaxis().FindBin(1 + 1.),"View with single hit")
				tgr2.GetXaxis().SetBinLabel(tgr2.GetXaxis().FindBin(2 + 1.),"No view with single hit")
	
				tgr0.GetXaxis().LabelsOption("h")
				tgr1.GetXaxis().LabelsOption("h")
				tgr2.GetXaxis().LabelsOption("h")
	
			#tracks0.append(0)
			#tracks1.append(0)
			#tracks2.append(0)
	
			tgr0.SetMinimum(0)
			tgr0.GetXaxis().SetRangeUser(1.5,3.5)
			tgr0.GetXaxis().SetTickLength(0)
			DrawScatOverlay3(tgr0,tgr1,tgr2,"Any or no wrong hits in track","No wrong hits in track","One wrong hit",";Filter condition on hits in the first/last modules;Tracks", "../images/"+fitMode[i]+"/"+config[j]+"/tracksPerFilter_"+plotMode[h]+"_main")

