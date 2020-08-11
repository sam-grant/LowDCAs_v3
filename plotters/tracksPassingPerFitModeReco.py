# plot the number of tracks per filter condition

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import *
from ROOT import gROOT

LoadPlotFunc()

# fitModes = [ "trackPlotsTruthLR", "trackPlotsMainFit", "trackPlotsFullSeqFit", "tracksLRFlip" ] 
# fitModes = [ "trackPlotsMainFit",  "tracksLRFlip" ] 
# fitModes = [ "TruthLR", "MainFit", "FullSeqFit", "FlipLR" ] 
fitModes = [ "MainFit", "FlipLR", "FullSeqFit" ] 

# get file
# file1 = TFile.Open("../plots/nominalSim/nominalSimPlots/magicPlots_noQ.root")
# file2 = TFile.Open("../plots/nominalSim/nominalSimPlots/magicPlots_Q.root")

files = [ "recoPlots_enhanced.root"] #testFSQ.root" ] #nominalSimPlotsQ.root", "nominalSimPlotsNoQ.root"]

tracksPassing = [] 
scaleFactors = []

for k in range(len(fitModes)): 

	fileQ = TFile.Open("../plots/reco/recoPlots_testFSQ.root") #nominalSim/nominalSimPlotsQ.root")
	# fileNoQ = TFile.Open("../plots/nominalSim/nominalSimPlotsNoQ.root")

	print(fileQ)
	# print(fileNoQ)

	hQ = fileQ.Get("trackPlots"+fitModes[k]+"/Run") 
	# hNoQ = fileNoQ.Get("trackPlots"+fitModes[k]+"/Run") 

	print(hQ)
	# print(hNoQ)
	print(hQ.GetEntries())

#	tracksPassing.append(hQ.GetEntries()) # /hNoQ.GetEntries())
tracksPassing.append(1962)
tracksPassing.append(3000)
tracksPassing.append(2984)
# tgr = DefineScat([1,2,3,4], tracksPassing) 
tgr = DefineScat([1,2,3], tracksPassing) 


tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(0 + 1.),"Main")
tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(1 + 1.),"Main+FSQ")
tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(2 + 1.),"FSQ")
# tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(3 + 1.),"LR flip")
tgr.GetXaxis().LabelsOption("h")


DrawScat(tgr, ";Fit mode;Quality tracks", "../images/eff/tracksPerFitModeReco") # DrawScat(graph, title, fname)
