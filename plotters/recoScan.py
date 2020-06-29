# plot number of tracks passing quality cuts for different low DCA thresholds

from ROOT import TFile, TH1, TGraphErrors
from plotFunc import *
from ROOT import gROOT

LoadPlotFunc()

# config = "gaussErrors"
config = "uniformErrors"


thresholds = [ "0.000", "0.025", "0.050", "0.075","0.100",
	    "0.125", "0.150", "0.175", "0.200",
	    "0.225", "0.250", "0.275", "0.300",
	    "0.325", "0.350", "0.375", "0.400",
	    "0.425", "0.450", "0.475", "0.500" ] 

xaxis = []

noQualityTracks = []
qualityTracks = []
trackFrac = []

noQualityPValues = []
qualityPValues = []

for i in range(len(thresholds)):

    file = TFile.Open("../plots/recoScan/"+config+"/"+thresholds[i]+"/recoPlots.root")

    print(file)

    tracksQ = file.Get("quality/Run")
    tracksNoQ = file.Get("noQuality/Run")

    # pValuesQ = file.Get("quality/pValues")
    # pValuesNoQ = file.Get("noQuality/pValues")

    # qualityPValues.append(pValFrac(pValuesQ))
    # noQualityPValues.append(pValFrac(pValuesNoQ))

    qualityTracks.append(tracksQ.GetEntries())
    noQualityTracks.append(tracksNoQ.GetEntries())

    trackFrac.append(tracksQ.GetEntries()/tracksNoQ.GetEntries())

    # print(float(thresholds[i]))
    # print(tracksQ.GetEntries())
    # print(pValFrac(pValuesNoQ))
    
    xaxis.append(float(thresholds[i])*1000)
    

# print("Max tracks\t"+str(max(qualityTracks)))
# print("Min p-value\t"+str(min(noQualityPValues)))

tgr1 = DefineScat(xaxis, qualityTracks)
tgr2 = DefineScat(xaxis, trackFrac)
# tgr3 = DefineScat(xaxis, qualityPValues)
# tgr4 = DefineScat(xaxis, noQualityPValues)

tgr1.GetYaxis().SetTitleOffset(2.0)
tgr2.GetYaxis().SetTitleOffset(2.0)


DrawScat(tgr1,";Lock low DCA threshold [#mum];Tracks","../images/recoScans/tracksCoarse")
DrawScat(tgr2,";Lock low DCA threshold [#mum];Fraction of tracks passing quality cuts","../images/recoScans/trackFracCoarse")
# DrawScat(tgr3,";Lock low DCA threshold [#mum];Tracks passing quality cuts with p-values < 5%","../images/lowDCAPValScan_"+config+"_Q")
# DrawScat(tgr4,";Lock low DCA threshold [#mum];Tracks with p-values < 5%","../images/lowDCAPValScan_"+config+"_noQ")
