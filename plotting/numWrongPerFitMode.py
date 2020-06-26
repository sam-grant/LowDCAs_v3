# plot the number of tracks per filter condition

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import *
from ROOT import gROOT

LoadPlotFunc()

fitModes = [ "trackPlotsTruthLR", "trackPlotsMainFit", "trackPlotsFullSeqFit", "tracksLRFlip" ] 
orientation = [ "radialPos", "verticalPos" ] 

# Need no quality

# get file
file1 = TFile.Open("../plots/flipLR/magic/magicPlots_noQ.root")
file2 = TFile.Open("../plots/flipLR/magic/magicPlots_Q.root")

print(file1)
print(file2)

tracks = [] 
scaleFactors = []

for k in range(len(fitModes)): 

	h1 = file1.Get(fitModes[k]+"/Run") 
	h2 = file2.Get(fitModes[k]+"/Run") 

	print(h1)


	# scaleFactors.append(h1.GetEntries())
	tracks.append(h2.GetEntries()/h1.GetEntries())


# Normalise


# for k in range(len(scaleFactors)):

# 	tracks[k] = tracks[k]/scaleFactors[k]

tgr = DefineScat([1,2,3,4], tracks) 

tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(0 + 1.),"Truth LR")
tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(1 + 1.),"Main")
tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(2 + 1.),"Full sequence")
tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(3 + 1.),"LR flip")
tgr.GetXaxis().LabelsOption("h")


DrawScat(tgr, ";Fit mode;Fraction of tracks passing quality cuts", "../images/magic/tracksPassing") # DrawScat(graph, title, fname)