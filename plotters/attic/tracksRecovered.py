# plot the number of tracks per filter condition

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import *
from ROOT import gROOT

LoadPlotFunc()

# Left this as a list, in case you need to make more configs
config = ["reco", "nominal", "optimal"] 
thresholds = ["0", "140", "500"]

# List for tracks
tracks0 = []
tracks1 = []
tracks2 = []


tracks = [tracks0,tracks1,tracks2]

for i in range(len(config)):

	for j in range(len(thresholds)):

		if (i==0): file = TFile.Open("../plots/flipLR/"+config[i]+"/recoPlots"+thresholds[j]+".root")
		else: file = TFile.Open("../plots/flipLR/"+config[i]+"/simPlots"+thresholds[j]+".root")
		# Get N tracks recovered

		flip = file.Get("flip/Run")
		noFlip = file.Get("noFlip/Run")

		recovered = flip.GetEntries() - noFlip.GetEntries()

		print(recovered)

		tracks[i].append(recovered)

for i in range(len(tracks0)):
	print(tracks[0][i])


for i in range(len(tracks0)):
	
	tgr0 = DefineScat([1,2,3], tracks0)
	tgr1 = DefineScat([1,2,3], tracks1)
	tgr2 = DefineScat([1,2,3], tracks2)

	tgr0.GetXaxis().SetBinLabel(tgr0.GetXaxis().FindBin(0 + 1.),"Nominal reco")
	tgr0.GetXaxis().SetBinLabel(tgr0.GetXaxis().FindBin(1 + 1.),"Nominal sim")
	tgr0.GetXaxis().SetBinLabel(tgr0.GetXaxis().FindBin(2 + 1.),"Optimised sim")
	tgr1.GetXaxis().SetBinLabel(tgr0.GetXaxis().FindBin(0 + 1.),"Nominal reco")
	tgr1.GetXaxis().SetBinLabel(tgr0.GetXaxis().FindBin(1 + 1.),"Nominal sim")
	tgr1.GetXaxis().SetBinLabel(tgr0.GetXaxis().FindBin(2 + 1.),"Optimised sim")
	tgr2.GetXaxis().SetBinLabel(tgr0.GetXaxis().FindBin(0 + 1.),"Nominal reco")
	tgr2.GetXaxis().SetBinLabel(tgr0.GetXaxis().FindBin(1 + 1.),"Nominal sim")
	tgr2.GetXaxis().SetBinLabel(tgr0.GetXaxis().FindBin(2 + 1.),"Optimised sim")

	tgr0.GetXaxis().LabelsOption("h")
	tgr1.GetXaxis().LabelsOption("h")
	tgr2.GetXaxis().LabelsOption("h")


tgr0.GetXaxis().SetTickLength(0)
DrawScatOverlay3(tgr0,tgr1,tgr2,"Low DCA threshold: 0 #mum","Low DCA threshold: 140 #mum","Low DCA threshold: 500 #mum",";Tracking configuration;Tracks recovered", "../images/flippedTracks/tracksRecovered")