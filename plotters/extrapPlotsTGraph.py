# plot the number of tracks per filter condition

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import *
from ROOT import gROOT

LoadPlotFunc()

 
fnames = [ "nominalSimPlotsQ.root" ] #"magicPlots_noQ.root" , "magicPlots_Q.root"]
fitModes = [ "TruthLR", "MainFit", "FullSeqFit", "FlipLR" ] 
orientation = [ "radialPos", "verticalPos" ] 

for i in range(len(fnames)): # quality on/off files

	# get file
	file = TFile.Open("../plots/nominalSim/"+fnames[i])
	print(file)

	for j in range(len(orientation)): 

		means12 = []
		errors12 = []
		means18 = []
		errors18 = []

		for k in range(len(fitModes)): 

			h12 = file.Get("extrapPlots"+fitModes[k]+"/vertices/station12/h_"+orientation[j]) 
			h18 = file.Get("extrapPlots"+fitModes[k]+"/vertices/station18/h_"+orientation[j])

			means12.append(h12.GetMean())
			errors12.append(h12.GetMeanError())
			means18.append(h18.GetMean())
			errors18.append(h18.GetMeanError())


		tgr12 = DefineScatErrors([1,2,3,4], [], means12, errors12)
		tgr18 = DefineScatErrors([1,2,3,4], [], means18, errors18)
	
		tgr12.GetXaxis().SetBinLabel(tgr12.GetXaxis().FindBin(0 + 1.),"Truth LR")
		tgr12.GetXaxis().SetBinLabel(tgr12.GetXaxis().FindBin(1 + 1.),"Main")
		tgr12.GetXaxis().SetBinLabel(tgr12.GetXaxis().FindBin(2 + 1.),"Full sequence")
		tgr12.GetXaxis().SetBinLabel(tgr12.GetXaxis().FindBin(3 + 1.),"LR flip")

		tgr18.GetXaxis().SetBinLabel(tgr18.GetXaxis().FindBin(0 + 1.),"Truth LR")
		tgr18.GetXaxis().SetBinLabel(tgr18.GetXaxis().FindBin(1 + 1.),"Main")
		tgr18.GetXaxis().SetBinLabel(tgr18.GetXaxis().FindBin(2 + 1.),"Full sequence")
		tgr18.GetXaxis().SetBinLabel(tgr18.GetXaxis().FindBin(3 + 1.),"LR flip")
	
		tgr12.GetXaxis().LabelsOption("h")
		tgr18.GetXaxis().LabelsOption("h")

		title = ""
		if(j==0): title = ";Fit mode;Radial decay position mean [mm]"
		else: title = ";Fit mode;Vertical decay position mean [mm]"

		# DrawScatOverlay(tgr12, tgr18, "Station 12", "Station 18", title, "../images/magic/"+orientation[j]+"Means") # DrawScat(graph, title, fname)
		DrawScat(tgr12, title, "../images/extrap/station12/"+orientation[j]+"Means") # DrawScat(graph, title, fname)
		DrawScat(tgr18, title, "../images/extrap/station18/"+orientation[j]+"Means") # DrawScat(graph, title, fname)

