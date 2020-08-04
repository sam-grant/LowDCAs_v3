
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
pValueCutLo = [ "0.000", "0.001", "0.002", "0.003", "0.004", "0.005", "0.006", "0.007", "0.008", "0.009", "0.010", "0.011", "0.012", "0.013", "0.014", "0.015", "0.016", "0.017", "0.018", "0.019", "0.020" ]    

NFSQ = [ 13509, 3811, 3527, 3348, 3239, 3135, 3060, 2995, 2928, 2878, 2824, 2777, 2730, 2687, 2656, 2626, 2589, 2546, 2515, 2487, 2460 ]

tPerEvent = [ 19.5465, 8.93486, 8.53029, 8.29398, 8.22356, 8.03432, 7.95626, 7.89287, 7.8504, 7.67913, 7.65926, 7.65494, 7.65831, 7.60059, 7.54311, 7.4257, 7.44466, 7.27638, 7.34085, 7.25462, 7.20663 ]


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

file = TFile.Open("../plots/reco/recoPlots_pValueCutFineScan.root")

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

DrawScat(DefineScat(pValueCutLoFloat, eff), ";p-value low cut;Track efficiency over mainFit","../images/mainFitEnhanced/fine/efficiency")
DrawScat(DefineScat(tPerEvent, eff), ";CPU time / event [s];Track efficiency over mainFit","../images/mainFitEnhanced/fine/EffVsTime")
# DrawScat(DefineScat(pValueCutLoFloat, timeLoss), ";p-value low cut;CPU time increase / event [s]","../images/mainFitEnhanced/fine/timeIncrease")
DrawScat(DefineScat(pValueCutLoFloat, NFSQPerEvent), ";p-value low cut;Times FSQ is called / event","../images/mainFitEnhanced/fine/FSQCalls")
DrawScatX2Line(DefineScat(pValueCutLoFloat, tPerEvent), ";p-value low cut;CPU time / event [s]","../images/mainFitEnhanced/fine/time", t_m/nEvents, t_f/nEvents) 
DrawScat(DefineScat(pValueCutLoFloat, tracksPerSecondNorm), ";p-value low cut;Tracks per second (normalised to mainFit) [s^{-1}]","../images/mainFitEnhanced/fine/tracksPerSecondNorm")
tgr = DefineScat(pValueCutLoFloat, tracksPerSecond)
tgr.GetYaxis().SetRangeUser(1.5,4.5)
DrawScatX2Line(tgr, ";p-value low cut;Quality tracks per second [s^{-1}]","../images/mainFitEnhanced/fine/tracksPerSecond", (trk_m/t_m), (trk_f/t_f))

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
DrawScatYLine(tgr2, ";(t_{m+f} #minus t_{m})/t_{f} / event;Times FSQ is called / event","../images/mainFitEnhanced/fine/FvsFSQCalls", 1-(t_m/t_f))

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

