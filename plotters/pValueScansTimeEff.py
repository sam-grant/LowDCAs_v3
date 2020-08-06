
# Efficiency vs. F
# Time / event vs. F
# Efficiency vs. pValue window
# Time / event vs. pValue window
# Effiency vs CPU time

from ROOT import TFile, TH1, TGraphErrors, TF1, gStyle, gPad, TPaveText
from plotFunc import LoadPlotFunc, DefineScat, DrawScat, DrawScatXLine, DrawScat2XLine, DrawScatYLine, DrawScatXYYLine
from ROOT import gROOT
import pandas as pd

LoadPlotFunc()

version="49"
file = "../mainFitEnhanced/txt/pValueScans_v"+version+".csv"
data = pd.read_csv(file) 
print(data)

# Some constants
nEvents = 73
t_m = data.iloc[0]['Time/event [s]']
t_f = data.iloc[1]['Time/event [s]']
trk_m = data.iloc[0]['Tracks over Q']
trk_f = data.iloc[1]['Tracks over Q']


# Add new columns
data['F'] = (data['Time/event [s]']-t_m)/t_f
data['Eff'] = data['Tracks over Q']/trk_m
data['NFSQPerEvent'] = data[' Times FSQ is called']/nEvents

F_f = data.iloc[1]['F']
eff_f = data.iloc[1]['Eff']


# Drop first two rows
data = data.iloc[2:]

# Load into lists, pandas is too hard otherwise
pValueCutLo = data['pValueCutLo_'].tolist()
tracksQ = data['Tracks over Q'].tolist()
tPerEvent = data['Time/event [s]'].tolist()
NFSQ = data[' Times FSQ is called'].tolist()
F = data['F'].tolist()
eff = data['Eff'].tolist()
NFSQPerEvent = data['NFSQPerEvent'].tolist()

# Now Draw

# Efficiency vs. F, with a line at FSQ
DrawScatYLine(DefineScat(F,eff),";(t_{m+f} #minus t_{m})/t_{f};Track efficiency","../images/mainFitEnhanced/v_"+version+"/EffvsF",F_f)
# Time / event vs. F, with a line at FSQ
DrawScatYLine(DefineScat(F,tPerEvent),";(t_{m+f} #minus t_{m})/t_{f};CPU time / event","../images/mainFitEnhanced/v_"+version+"/TimevsF",F_f)
# Efficiency vs. pValue window, with a line at FSQ
DrawScatXLine(DefineScat(pValueCutLo,eff),";p-value low cut;Track efficiency","../images/mainFitEnhanced/v_"+version+"/EffvspVal", eff_f)
# Time / event vs. pValue window, with a line at mainFit
gr4 = DefineScat(pValueCutLo,tPerEvent)
gr4.GetYaxis().SetRangeUser(6,22)
DrawScat2XLine(gr4,";p-value low cut;CPU time / event","../images/mainFitEnhanced/v_"+version+"/TimevspVal", t_f, t_m)
# Effiency vs CPU time, with two lines at FSQ, one line at mainFit
DrawScatXYYLine(DefineScat(tPerEvent,eff),";CPU time / event;Track efficiency","../images/mainFitEnhanced/v_"+version+"/EffvsTime", t_f, eff_f, t_m)

# DrawScat(DefineScat(eff,tPerEvent),";CPU time / event;Track efficiency","../images/mainFitEnhanced/v_"+version+"/EffvsTime")
# # Effiency vs CPU time, with two lines at FSQ
# DrawScat(DefineScat(pValueCutLo,tPerEvent),";p-value low cut;CPU time / event","../images/mainFitEnhanced/v_"+version+"/TimevspVal")
# # Time / event vs. pValue window, with a line at mainFit
# DrawScat(DefineScat(pValueCutLo,eff),";p-value low cut;Track efficiency","../images/mainFitEnhanced/v_"+version+"/EffvspVal")
# # Efficiency vs. pValue window, with a line at FSQ
# DrawScatYLine(DefineScat(F,tPerEvent),";(t_{m+f} #minus t_{m})/t_{f};CPU time / event","../images/mainFitEnhanced/v_"+version+"/TimevsF",F_f)
# # Time / event vs. F, with a line at FSQ
# DrawScatYLine(DefineScat(F,eff),";(t_{m+f} #minus t_{m})/t_{f};Track efficiency","../images/mainFitEnhanced/v_"+version+"/EffvsF",F_f)
# # Efficiency vs. F, with a line at FSQ
