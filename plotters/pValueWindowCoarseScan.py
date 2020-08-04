
# Make plot of efficiency gain over mainFit vs pVal X
# Time / event vs pVal
# Times FSQ is called vs pVal X
# F vs pValue
# Times FSQ vs F
# Time - time_main / event X
# Quality tracks / s (normalised to mainFit) 

from ROOT import TFile, TH1, TGraphErrors, TF1, gStyle, gPad, TPaveText
from plotFunc import LoadPlotFunc, DefineScat, DrawScat, DrawScatXLine, DrawScatX2Line, DrawScatYLine
from ROOT import gROOT

LoadPlotFunc()

# Vectors
pValueCutLo = [ "0.000", "0.005", "0.010", "0.015", "0.020", "0.025", "0.030", "0.035", "0.040", "0.045" ] 
NFSQ = [ 13509, 3135, 2842, 2626, 2460, 2342, 2253, 2167, 2109, 2046 ]
tPerEvent = [ 19.5465, 8.28937, 8.06233, 7.713, 7.55266, 7.24138, 7.13307, 6.98993, 6.93654, 6.84859]

# Constants
nEvents = 73
t_m = 467.04524
t_f = 1276.405
trk_m = 1962
trk_f = 2948


# Holders
tracks = [] 
tracksPerSecond = []
tracksPerSecondNorm = []
timeLoss = []
F = []
eff = []
pValueCutLoFloat = []
NFSQPerEvent = []

file = TFile.Open("../plots/reco/recoPlots_pValueCutCoarseScan.root")

tgr_ = []

# Fill holders
for i in range(len(pValueCutLo)):
        
        trk = (file.Get(pValueCutLo[i]+"/Run")).GetEntries()

        tracks.append(trk)
        tracksPerSecond.append(trk/(nEvents*tPerEvent[i]))
        tracksPerSecondNorm.append( (trk/(nEvents*tPerEvent[i])) / (trk_m/t_m) )
        timeLoss.append(tPerEvent[i] - t_m/nEvents)
        F.append((tPerEvent[i]-(t_m/nEvents))/(t_f/nEvents))
        eff.append(trk/trk_m)
        pValueCutLoFloat.append(float(pValueCutLo[i]))
        NFSQPerEvent.append(NFSQ[i]/nEvents)

# Now Draw

DrawScat(DefineScat(pValueCutLoFloat, eff), ";p-value low cut;Track efficiency over mainFit","../images/mainFitEnhanced/coarse/efficiency")
DrawScat(DefineScat(tPerEvent, eff), ";CPU time / event [s];Track efficiency over mainFit","../images/mainFitEnhanced/coarse/EffVsTime")
# DrawScat(DefineScat(pValueCutLoFloat, timeLoss), ";p-value low cut;CPU time increase / event [s]","../images/mainFitEnhanced/coarse/timeIncrease")
DrawScat(DefineScat(pValueCutLoFloat, NFSQPerEvent), ";p-value low cut;Times FSQ is called / event","../images/mainFitEnhanced/coarse/FSQCalls")
DrawScatX2Line(DefineScat(pValueCutLoFloat, tPerEvent), ";p-value low cut;CPU time / event [s]","../images/mainFitEnhanced/coarse/time", t_m/nEvents, t_f/nEvents) 
DrawScat(DefineScat(pValueCutLoFloat, tracksPerSecondNorm), ";p-value low cut;Tracks per second (normalised to mainFit) [s^{-1}]","../images/mainFitEnhanced/coarse/tracksPerSecondNorm")
tgr = DefineScat(pValueCutLoFloat, tracksPerSecond)
tgr.GetYaxis().SetRangeUser(1.5,4.5)
DrawScatX2Line(tgr, ";p-value low cut;Quality tracks per second [s^{-1}]","../images/mainFitEnhanced/coarse/tracksPerSecond", (trk_m/t_m), (trk_f/t_f))

# What a mess
tgr2 = DefineScat(F, NFSQPerEvent)
lineFit = TF1("lineFit1","pol1")
lineFit.SetLineWidth(3)
lineFit.SetLineColor(1)
tgr2.Fit(lineFit)
# Stat box formatting
gStyle.SetStatFormat("6.3g")
gStyle.SetOptFit(111)
tgr2.Draw()
gPad.Update()
statBox = tgr2.FindObject("stats")
statBox.SetBorderSize(0)
# statBox.SetY2NDC(0.89)
# statBox.SetY1NDC(0.71)
# statBox.SetX2NDC(0.49)
# statBox.SetX1NDC(0.11)
statBox.SetX1NDC(0.11)
statBox.SetX2NDC(0.49)
statBox.SetY1NDC(0.69)
statBox.SetY2NDC(0.89)
# txt1 = TPaveText(x_0,gPad.GetUymin()+0.1,x_0+30,gPad.GetUymin()+1.50)
txt1 = TPaveText(0.65,100,0.75,120)
txt1.AddText(str(lineFit.Eval(1-(t_m/t_f))))
print(lineFit.Eval(1-(t_m/t_f)))
txt1.SetFillColor(0)
txt1.SetTextFont(44)
txt1.SetTextSize(26)
# statBox.SetTextFont(44)
# statBox.SetTextSize(26)
statBox.Draw()
gPad.Update()
txt1.Draw()
gPad.Update()
DrawScatYLine(tgr2, ";(t_{m+f} #minus t_{m})/t_{f} / event;Times FSQ is called / event","../images/mainFitEnhanced/coarse/FvsFSQCalls", 1-(t_m/t_f))

# Tested

#DrawScat(DefineScat(pValueCutLoFloat, tPerEvent), ";p-value low cut;CPU time / event [s]","../images/mainFitEnhanced/coarse/time")


#         tracks_.append(tracks.GetEntries())
#         if(f == 0): tracksCoarse_.append(tracks.GetEntries())
#         else: tracksCoarseNoneWrong_.append(tracks.GetEntries())
        
#         xaxis_.append(float(thresholds[i])*1000)
    
#     tgr = DefineScat(xaxis_, tracks_)
#     tgr_.append(tgr)
    
# DrawScat(tgr_[0],";Lock low DCA threshold [#mum];Tracks","../images/scans/tracksCoarse")
# DrawScat(tgr_[1],";Lock low DCA threshold [#mum];Tracks with no wrong hits","../images/scans/tracksCoarseNoneWrong")

# # Take ratio
# ratio_ = [] 

# for i in range(len(tracksCoarse_)):

#     ratio_.append(tracksCoarseNoneWrong_[i] / tracksCoarse_[i])
 
# tgr_ratio = DefineScat(xaxis_, ratio_)
# DrawScat(tgr_ratio,";Lock low DCA threshold [#mum];Fraction of tracks with no wrong hits","../images/scans/tracksRatio")


    # DrawScat(tgr2,";Lock low DCA threshold [#mum];Tracks passing quality cuts with p-values < 5%","../images/"+config+"/scans/qualityPValues")

