# plot number of tracks passing quality cuts for different low DCA thresholds

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import *
from ROOT import gROOT

LoadPlotFunc()

config = "nominal"

thresholds = [ "0.025", "0.050", "0.075","0.100",
	    "0.125", "0.150", "0.175", "0.200",
	    "0.225", "0.250", "0.275", "0.300",
	    "0.325", "0.350", "0.375", "0.400",
	    "0.425", "0.450", "0.475", "0.500" ] 

xaxis = []

qualityTracks = []
qualityPValues = []

for i in range(len(thresholds)):

    file = TFile.Open("../plots/simScan/"+config+"/simPlots.root") 

    print(file)

    tracks = file.Get(thresholds[i]+"/Run")

    pValues = file.Get(thresholds[i]+"/pValues")

    qualityTracks.append(tracks.GetEntries())
    qualityPValues.append(pValFrac(pValues))

    print(float(thresholds[i]))
    print(tracks.GetEntries())
    print(pValFrac(pValues))
    
    xaxis.append(float(thresholds[i])*1000)
    

print("Max tracks\t"+str(max(qualityTracks)))
print("Min p-value\t"+str(min(qualityPValues)))

tgr1 = DefineScat(xaxis, qualityTracks)
tgr2 = DefineScat(xaxis, qualityPValues)


DrawScat(tgr1,";Lock low DCA threshold [#mum];Tracks passing quality cuts","../images/"+config+"/scans/qualityTracks")
DrawScat(tgr2,";Lock low DCA threshold [#mum];Tracks passing quality cuts with p-values < 5%","../images/"+config+"/scans/qualityPValues")

