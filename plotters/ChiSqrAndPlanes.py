# Effiency versus chi square loop for FSQ and mainFSQ
# Time versus chi square loop for FSQ and mainFSQ

from ROOT import TFile, TH1, TGraphErrors, TF1, gStyle, gPad, TPaveText, TAttAxis
from plotFunc import LoadPlotFunc, DefineScat, DrawScat, DrawScatXLine, DrawScat2XLine, DrawScatYLine, DrawScatXYYLine
from ROOT import gROOT
import pandas as pd

LoadPlotFunc()

version="49"
# file = "../mainFitEnhanced/txt/pValueScans_v"+version+".csv"
file = "../mainFitEnhanced/txt/ChiSqrAndPlanes_v"+version+".csv"
data = pd.read_csv(file) 


# Some constants
nEvents = 73

t_m = data.iloc[0]['Time/event [s]']
t_f = data.iloc[2]['Time/event [s]']
trk_m = data.iloc[0]['Tracks over Q']
trk_f = data.iloc[2]['Tracks over Q']

print(t_m,t_f,trk_m,trk_f)
# Add new columns
data['F'] = (data['Time/event [s]']-t_m)/t_f
data['Eff'] = data['Tracks over Q']/trk_m
data['NFSQPerEvent'] = data[' Times FSQ is called']/nEvents

# F_f = data.iloc[1]['F']
# eff_f = data.iloc[1]['Eff']
print(data)
# Split dataframe
mainFit = data.iloc[:2]
FSQ = data.iloc[2:6]
mainFSQ = data.iloc[6:]
print(mainFSQ)

# Make lists
eff_f = FSQ['Eff'].tolist()
eff_mF = mainFSQ['Eff'].tolist()
tPerEvent_f = FSQ['Time/event [s]'].tolist()
tPerEvent_mF = mainFSQ['Time/event [s]'].tolist()

nSeq = [1,2,3,4]

# Now Draw
gr1 = DefineScat(nSeq,eff_f)
# Set divisions to display only integers
gr1.GetXaxis().SetNdivisions(4,True)
DrawScat(gr1,";Number of sequences;Track efficiency","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/EffvsSeq_FSQ")

gr2 = DefineScat(nSeq,tPerEvent_f/t_m)
# Set divisions to display only integers
gr2.GetXaxis().SetNdivisions(4,True)
DrawScat(gr2,";Number of sequences;CPU time / event (normalised to mainFit)","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/TimevsSeq_FSQ")

# Now Draw
gr3 = DefineScat(nSeq,eff_mF)
# Set divisions to display only integers
gr3.GetXaxis().SetNdivisions(4,True)
DrawScat(gr3,";Number of sequences;Track efficiency","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/EffvsSeq_mF")

gr4 = DefineScat(nSeq,tPerEvent_mF/t_m)
# Set divisions to display only integers
gr4.GetXaxis().SetNdivisions(4,True)
DrawScat(gr4,";Number of sequences;CPU time / event (normalised to mainFit)","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/TimevsSeq_mF")
# # Load into lists, pandas is too hard otherwise
# pValueCutLo = data['pValueCutLo_'].tolist()

# tPerEvent = data['Time/event [s]'].tolist()
# NFSQ = data[' Times FSQ is called'].tolist()
# F = data['F'].tolist()
# eff = data['Eff'].tolist()
# NFSQPerEvent = data['NFSQPerEvent'].tolist()



# # Efficiency vs. F, with a line at FSQ
# DrawScatYLine(DefineScat(F,eff),";(t_{m+f} #minus t_{m})/t_{f};Track efficiency","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/EffvsF",F_f)
# # Time / event vs. F, with a line at FSQ
# DrawScatYLine(DefineScat(F,tPerEvent),";(t_{m+f} #minus t_{m})/t_{f};CPU time / event","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/TimevsF",F_f)
# # Efficiency vs. pValue window, with a line at FSQ
# DrawScatXLine(DefineScat(pValueCutLo,eff),";p-value low cut;Track efficiency","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/EffvspVal", eff_f)
# # Time / event vs. pValue window, with a line at mainFit
# gr4 = DefineScat(pValueCutLo,tPerEvent)
# gr4.GetYaxis().SetRangeUser(6,22)
# DrawScat2XLine(gr4,";p-value low cut;CPU time / event","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/TimevspVal", t_f, t_m)
# # Effiency vs CPU time, with two lines at FSQ, one line at mainFit
# DrawScatXYYLine(DefineScat(tPerEvent,eff),";CPU time / event;Track efficiency","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/EffvsTime", t_f, eff_f, t_m)
# # DrawScatXYYLine(DefineScat(tPerEvent/t_m,eff),";CPU time / event (normalised to mainFit);Track efficiency","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/EffvsTimeNorm", t_f/t_m, eff_f, t_m/t_m)
# # DrawScat(DefineScat(tPerEvent/t_m,eff),";CPU time / event (normalised to mainFit);Track efficiency","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/EffvsTimeNorm")

# 
# # Effiency vs CPU time, with two lines at FSQ
# DrawScat(DefineScat(pValueCutLo,tPerEvent),";p-value low cut;CPU time / event","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/TimevspVal")
# # Time / event vs. pValue window, with a line at mainFit
# DrawScat(DefineScat(pValueCutLo,eff),";p-value low cut;Track efficiency","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/EffvspVal")
# # Efficiency vs. pValue window, with a line at FSQ
# DrawScatYLine(DefineScat(F,tPerEvent),";(t_{m+f} #minus t_{m})/t_{f};CPU time / event","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/TimevsF",F_f)
# # Time / event vs. F, with a line at FSQ
# DrawScatYLine(DefineScat(F,eff),";(t_{m+f} #minus t_{m})/t_{f};Track efficiency","../images/mainFitEnhanced/ChiSqrAndPlanes_v"+version+"/EffvsF",F_f)
# # Efficiency vs. F, with a line at FSQ
