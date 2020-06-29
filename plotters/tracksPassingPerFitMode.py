# plot the number of tracks per filter condition

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import *
from ROOT import gROOT

LoadPlotFunc()

# fitModes = [ "trackPlotsTruthLR", "trackPlotsMainFit", "trackPlotsFullSeqFit", "tracksLRFlip" ] 
fitModes = [ "TruthLR", "MainFit", "FullSeqFit", "FlipLR" ] 

# get file
# file1 = TFile.Open("../plots/nominalSim/nominalSimPlots/magicPlots_noQ.root")
# file2 = TFile.Open("../plots/nominalSim/nominalSimPlots/magicPlots_Q.root")

files = ["nominalSimPlotsQ.root", "nominalSimPlotsNoQ.root"]

tracksPassing = [] 
scaleFactors = []

for k in range(len(fitModes)): 

	fileQ = TFile.Open("../plots/nominalSim/nominalSimPlotsQ.root")
	fileNoQ = TFile.Open("../plots/nominalSim/nominalSimPlotsNoQ.root")

	print(fileQ)
	print(fileNoQ)

	hQ = fileQ.Get("trackPlots"+fitModes[k]+"/Run") 
	hNoQ = fileNoQ.Get("trackPlots"+fitModes[k]+"/Run") 

	print(hQ)
	print(hNoQ)

	tracksPassing.append(hQ.GetEntries()/hNoQ.GetEntries())

tgr = DefineScat([1,2,3,4], tracksPassing) 

tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(0 + 1.),"Truth LR")
tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(1 + 1.),"Main")
tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(2 + 1.),"Full sequence")
tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(3 + 1.),"LR flip")
tgr.GetXaxis().LabelsOption("h")


DrawScat(tgr, ";Fit mode;Fraction of tracks passing quality cuts", "../images/eff/tracksPassingNomSim") # DrawScat(graph, title, fname)