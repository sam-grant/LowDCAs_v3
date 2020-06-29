# measuredDCAPlotter.py

# Makes plots of the fraction of wrong hits for tracks with one wrong hit per track

from ROOT import TFile, TCanvas, TH1F, TH1D, TLegend, TAxis, TAttMarker, TGraph, TGraphErrors
from ROOT import gROOT
from array import array	
	
def FancyDraw1D(hist1, title, fname, zoom): 

	c0 = TCanvas("","",800,600)

	hist1.SetStats(0)

	hist1.SetTitle(title)
			
	hist1.GetXaxis().SetTitleSize(.04)
	hist1.GetYaxis().SetTitleSize(.04)
	hist1.GetXaxis().SetTitleOffset(1.1)
	hist1.GetYaxis().SetTitleOffset(1.1)
	hist1.GetXaxis().CenterTitle(1)
	hist1.GetYaxis().CenterTitle(1)
 	hist1.GetYaxis().SetMaxDigits(4)

	hist1.SetLineWidth(3)
	hist1.SetLineColor(1)	
	hist1.SetLineColor(1)

	if(zoom==0): 
		hist1.GetXaxis().SetRangeUser(0,2500)
	else: 
		hist1.GetXaxis().SetRangeUser(0,500)
	# c0.SetLogy()

	hist1.Draw()

	# c0.SetGrid()
	
	c0.SaveAs(fname+".png")
	c0.SaveAs(fname+".pdf")

def Ratio(wrongHist, allHist):

	ratio = wrongHist.Clone("ratio")

	ratio.Divide(allHist)

	return ratio

path = "/gm2/data/users/sgrant/tracks/lowDCAs/vacuum_2um_allTimes_noMaterial_noBinning/filteredTracks/tracksMainFit"
names = ["leadingHitsAllDCAs.root", "leadingHitsLowDCAs.root" "filteredTracks_leadingHitsHighDCAs.root" "filteredTracks_nonLeadingHitsAllDCAs.root"","vacuum_20um_mainFit_posTimes","vacuum_20um_fullSeqFit_posTimes","vacuum_20um_fullSeqFit_allTimes"]

filterTracks
for i in range(0,len(names)):

	# Grab files
#	file = TFile.Open("../runSimPlots/"+names[i]+"/"+names[i]+".root")
	file = TFile.Open("../runSimPlots/"+names[i]+".root")

	# Grab plain DCA histograms
	h1 = file.Get("oneWrongPlanesHitCut/WrongHits/DCA");
	# Draw it
	FancyDraw1D(h1, ";Measured DCA [#mum];Hits","../images/DCAs_wrongHits_"+names[i],0)

	# Grab numerator hists
	h2 = file.Get("oneWrongPlanesHitCut/WrongHits/DCA")
	
	# Get ratio hist
	r1 = Ratio(h2, h1)

	# Draw it
	FancyDraw1D(r1, ";Measured DCA [#mum];Fraction of wrong LR choices","../images/fracWrongDCAs_"+names[i], 0)
	FancyDraw1D(r1, ";Measured DCA [#mum];Fraction of wrong LR choices","../images/fracWrongDCAsZoom_"+names[i], 1)
