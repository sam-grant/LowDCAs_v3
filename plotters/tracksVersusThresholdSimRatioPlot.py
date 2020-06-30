# plot number of tracks passing quality cuts for different low DCA thresholds

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import *
from ROOT import gROOT

LoadPlotFunc()

thresholds = [ "0.000", "0.025", "0.050", "0.075","0.100",
	    "0.125", "0.150", "0.175", "0.200",
	    "0.225", "0.250", "0.275", "0.300",
	    "0.325", "0.350", "0.375", "0.400",
	    "0.425", "0.450", "0.475", "0.500" ] 

files = ["nominalSimScanPlotsCoarse.root", "nominalSimScanPlotsCoarseNoneWrong.root"]


tgr_ = []

tracksCoarse_ = [] 
tracksCoarseNoneWrong_ = []

for f in range(len(files)):

    file = TFile.Open("../plots/nominalSimScan/"+files[f])
    print(file)

    tracks_ = []
    xaxis_ = []

    # nasty hack to get ratio plot to work

    for i in range(len(thresholds)):
        
        tracks = file.Get(thresholds[i]+"/Run")

        tracks_.append(tracks.GetEntries())
        if(f == 0): tracksCoarse_.append(tracks.GetEntries())
        else: tracksCoarseNoneWrong_.append(tracks.GetEntries())
        
        xaxis_.append(float(thresholds[i])*1000)
    
    tgr = DefineScat(xaxis_, tracks_)
    tgr_.append(tgr)

# Take ratio
ratio_ = [] 

for i in range(len(tracksCoarse_)):

    ratio_.append(tracksCoarseNoneWrong_[i] / tracksCoarse_[i])
 
tgr_ratio = DefineScat(xaxis_, ratio_)

tgr_[0].GetYaxis().SetRangeUser(4900,8200)
DrawScatRatio(tgr_[0], tgr_[1], tgr_ratio, "Any number of wrong hits", "No wrong hits", "../images/scans/combinedTracksRatioPlot")


    # DrawScat(tgr2,";Lock low DCA threshold [#mum];Tracks passing quality cuts with p-values < 5%","../images/"+config+"/scans/qualityPValues")

