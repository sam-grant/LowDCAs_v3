# Plotter for truth LR information
# !!! - Fraction of tracks with wrong LR guess !!!
# - Fraction of tracks with p-values below 5%
# - Reduced chi^2


# keep this around for it's many useful functions that took ages to write
#
# INTENDED FOR LOW DCA TRUTH SCANS, BUT IT'S OLD AND VERY CONFUSING

# IT DOES HAVE UNIQUE CODE THAT MAKES A PLOT OF THE FRACTION OF WRONG HITS PER TRACK FOR EACH THRESHOLD
#

from ROOT import gROOT
from array import array
from plotFunc import *

LoadPlotFunc()

def Ratio(wrongHist, allHist):#, rebin):

	# Clone to be safe
	# allHist.Rebin(rebin)
	# wrongHist.Rebin(rebin)

	ratio = wrongHist.Clone("ratio")

	ratio.Divide(allHist)

	return ratio

def Mean(all_):

	means_ = []

	for ihist in range(len(all_)):

		means_.append(all_[ihist].GetMean())

	return means_

# Return the number of tracks with a p-value less than 5%

def pValFrac(all_):

 	# Loop over the bins
 	# Get bin x-values
 	# if x-value is < 5%, sum the bin contents
 	# Divide by total entries
 	tracksLessThan_ = []

 	for ihist in range(0,len(all_)):

 		tracks = 0

 		for bin in range(0, all_[ihist].GetNbinsX()):

 			pValue = all_[ihist].GetBinCenter(bin+1)
 			# print("p-value", pValue)
 			# binVal = hist.GetBinContent(bin+1) + binVal
 			if(pValue < 0.05):

 				tracks = all_[ihist].GetBinContent(bin+1) + tracks
 				# fraction = binVal / hist.GetEntries()

 		# print("tracks ",tracks)
 		print(tracks / all_[ihist].GetEntries())
 		tracksLessThan_.append(tracks / all_[ihist].GetEntries())

 	return tracksLessThan_

def TotalTracks(all_):
	totalTracks_ = []
	print(len(all_))
	for i in range(len(all_)):
		totalTracks_.append(all_[i].GetEntries())
	return totalTracks_

def Frac(rightOrWrong_, all_):
	frac_ = []
	for i in range(0,len(all_)):
		# print("rightOrWrong_[i].GetEntries() ",rightOrWrong_[i].GetEntries())
		# print("all_[i].GetEntries() ",all_[i].GetEntries())
		frac_.append(rightOrWrong_[i].GetEntries() / all_[i].GetEntries() )
	return frac_

def DrawHist1D(hist,title,fname,i): 

	c1 = TCanvas("c1","",800,600)

	# hist.Rebin(4)
	hist.SetStats(0)

	hist.SetTitle(title)
			
	hist.GetXaxis().SetTitleSize(.04)
	hist.GetYaxis().SetTitleSize(.04)
	hist.GetXaxis().SetTitleOffset(1.1)
	hist.GetYaxis().SetTitleOffset(1.25)
	hist.GetXaxis().CenterTitle(1)
	hist.GetYaxis().CenterTitle(1)
	# hist.GetYaxis().SetRangeUser(.5,.7)
	if(i==0): hist.GetXaxis().SetRangeUser(-5,505)
	if(i==1): hist.GetXaxis().SetRangeUser(-5,2505)

	# hist.GetYaxis().SetRangeUser(0.50,0.70)
	hist.GetYaxis().SetMaxDigits(4)

	# hist.SetLineWidth(3)
	hist.SetLineColor(1)

	hist.Draw()
	c1.SaveAs(fname)

def DefineScat(x_, y_):

	x, y, ex, ey = array('d'), array('d'), array('d'), array('d')
	n = 0
	n = len(x_)
	if(n==0):
		return

	# print("n :"+str(n))
	for i in range(0,n):

#		frac = wrong_[i].GetEntries() / all_[i].GetEntries()
		# print(i)
		# print(x_[i])
		x.append(x_[i])

		ex.append(0)
		y.append(y_[i])
		ey.append(0)

		# print(str(DCAs_[i])+" * "+str(y_)+" * "+str(wrong_[i].GetEntries())+" * "+str(all_[i].GetEntries()))

	return TGraphErrors(n,x,y,ex,ey)


def DrawScat(plot, title, fname): #, grid):

	c2 = TCanvas("c2","",800,600)

	plot.SetTitle(title)			
	plot.GetXaxis().SetTitleSize(.04)
	plot.GetYaxis().SetTitleSize(.04)
	plot.GetXaxis().SetTitleOffset(1.1)
	plot.GetYaxis().SetTitleOffset(1.25)
	plot.GetXaxis().CenterTitle(1)
	plot.GetYaxis().CenterTitle(1)
	# plot.GetYaxis().SetRangeUser(0.086,0.106)\
	# plot.GetYaxis().SetRangeUser(0.5,0.7)
	# plot.GetXaxis().SetRangeUser(-5,2500)
	plot.GetYaxis().SetMaxDigits(4)
	#plot.SetMarkerSize(3)
	#plot.SetLineWidth(3)
	plot.SetMarkerStyle(20) # Full circle
	#plot.SetMarkerColor(4)
	#plot.SetLineColor(4)
	plot.Draw("AP")
	#if(grid==1): 
#		c2.SetGrid()
	c2.SaveAs(fname+".png")
	c2.SaveAs(fname+".pdf")
	return

def DrawManyScat(plots_, title, fname): #, grid):

	c2 = TCanvas("c2","",800,600)

	l1 = TLegend(0.59,0.39,0.89,0.89)
	l1.SetHeader("#bf{Low DCA thresholds}")
	dca = 0;
	l1.AddEntry(plots_[0],str(dca)+" #mum")
	l1.SetBorderSize(0)

	plots_[0].SetTitle(title)			
	plots_[0].GetXaxis().SetTitleSize(.04)
	plots_[0].GetYaxis().SetTitleSize(.04)
	plots_[0].GetXaxis().SetTitleOffset(1.1)
	plots_[0].GetYaxis().SetTitleOffset(1.25)
	plots_[0].GetXaxis().CenterTitle(1)
	plots_[0].GetYaxis().CenterTitle(1)
	# plot.GetYaxis().SetRangeUser(0.086,0.106)\
	# plot.GetYaxis().SetRangeUser(0.5,0.7)
	# plot.GetXaxis().SetRangeUser(-5,2500)
	plots_[0].GetYaxis().SetMaxDigits(4)
	#plot.SetMarkerSize(3)
	#plot.SetLineWidth(3)
	plots_[0].SetMarkerStyle(20) # Full circle
	plots_[0].SetMarkerColor(1)
	#plot.SetLineColor(4)
	plots_[0].Draw("AP")

	for i_plot in range(0,len(plots_)):

		if(i_plot==0): continue
		dca = dca + 100
		l1.AddEntry(plots_[i_plot],str(dca)+" #mum")
		# Skip yellow one
		if((i_plot+1)>=5): plots_[i_plot].SetMarkerColor(i_plot+2)
		else: plots_[i_plot].SetMarkerColor(i_plot+1)
		plots_[i_plot].SetMarkerStyle(20)
		# plots_[i_plot].SetMarkerSize(3)
		plots_[i_plot].Draw("P SAME")
	#if(grid==1): 
#		c2.SetGrid()
	l1.Draw("SAME")
	c2.SaveAs(fname+".png")
	c2.SaveAs(fname+".pdf")

	return

def DrawScatOverlay(plot1, plot2, title, fname):

	c2 = TCanvas("c2","",800,600)

	leg = TLegend(0.11,0.69,0.69,0.89)
	leg.SetBorderSize(0)

	plot1.SetTitle(title)			
	plot1.GetXaxis().SetTitleSize(.04)
	plot1.GetYaxis().SetTitleSize(.04)
	plot1.GetXaxis().SetTitleOffset(1.1)
	plot1.GetYaxis().SetTitleOffset(1.25)
	plot1.GetXaxis().CenterTitle(1)
	plot1.GetYaxis().CenterTitle(1)
	# plot.GetYaxis().SetRangeUser(0.086,0.106)
	# plot1.GetXaxis().SetRangeUser(-5,505)
	plot1.GetYaxis().SetMaxDigits(4)
	plot1.GetYaxis().SetRangeUser(0,1)
	#plot.SetMarkerSize(3)
	#plot.SetLineWidth(3)
	plot1.SetMarkerStyle(20) # Full circle
	plot2.SetMarkerStyle(24) # Open circle
	#plot.SetMarkerColor(4)
	#plot.SetLineColor(4)

	leg.AddEntry(plot1, "Fraction of tracks with a wrong LR choice")
	leg.AddEntry(plot2, "Fraction of tracks with an ambiguous LR choice")
	
	plot1.Draw("AP")
	plot2.Draw("P same")

	leg.Draw("same")

	c2.SaveAs(fname)

	return

# Wrap main in a function
def main():

	# Set drift time model
	flavour = "garfield"
	# flavour = "gauss"
	# flavour = "perfect"
	# flavour = "perfectVacuum"

	# Initiate file list
	files_ = []

	for i_lowDCA in range(0,21):

		# Load files into list
		file = TFile.Open("../runSimPlots/"+flavour+"/simPlotsMerged"+str(i_lowDCA)+".root")
		print("Loading ... "+str(file))
		files_.append(file)

	# Directories
	nWrongString_ = [ "noneWrong", "oneWrong", "twoWrong", "threeWrong", "fourWrong", "fiveWrong", "fivePlusWrong" ]
	# nPlusWrong = [ "nonePlusWrong", "onePlusWrong", "twoPlusWrong", "threePlusWrong", "fourPlusWrong", "fivePlusWrong", "fivePlusWrong" ]
#	nWrong_ = [0,1,2,3,4,5]
	
	# Low DCA thresholds
	DCAs_ = list(range(0,525,25)) # ] # , list(range(0,2600,100))]
	
	# Map DCAs to floats
	map(float, DCAs_)

	nWrongEntriesPerThres_ = []

	for i_lowDCA in range(0,len(DCAs_)):

		nWrongEntries_ = []

		# print("Low DCA threshold:\t"+str(DCAs_[i_lowDCA])+" um")

		# Only deal with divible by 100
		tmp = float(DCAs_[i_lowDCA])/100
		# print(tmp)
		if((tmp.is_integer())==0): continue
		
		print("Low DCA threshold:\t"+str(DCAs_[i_lowDCA])+" um")

		for i_wrong in range(0, len(nWrongString_)):

			tmp = files_[i_lowDCA].Get(nWrongString_[i_wrong]+"/Run")
			n = tmp.GetEntries()

			# Print number of entries
			print(nWrongString_[i_wrong]+"\t"+str(n))
		
			# Append into an array
			nWrongEntries_.append(n)

		# Append each list into another list, per threshold
		nWrongEntriesPerThres_.append(nWrongEntries_)
		# print(nPlusWrong[i_wrong]+"/Run")


	# Define them all as TGraphs 

	tgr_ = []
#	l1 = TLegend(0.69,0.69)

	for i_graph in range(0,len(nWrongEntriesPerThres_)):

		tgr = DefineScat([1,2,3,4,5,6,7], nWrongEntriesPerThres_[i_graph])

		if(i_graph==0):
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(0 + 1.),"None wrong")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(1 + 1.),"One wrong")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(2 + 1.),"Two wrong")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(3 + 1.),"Three wrong")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(4 + 1.),"Four wrong")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(5 + 1.),"Five wrong")
			tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(6 + 1.),"Five+ wrong")
			tgr.GetXaxis().LabelsOption("h")
			tgr.GetHistogram().SetMinimum(0)
			tgr.GetHistogram().SetMaximum(2500)
		tgr_.append(tgr)

	DrawManyScat(tgr_,";Wrong LR choices / track;Tracks","../images/WrongHitsPerTrk")

	
	#################################################################################

	# tmp = files_[0].Get(nPlusWrong[i_wrong]+"/Run")
#	g1 = DefineScat([1,2,3,4,5,6,7], nWrongEntriesPerThres_[i_counter])
#	i_counter = i_counter + 1
#	l1.AddEntry(g1,str(DCAs_[i_lowDCA]))
#	g1.SetMarkerColor(i_lowDCA)
	# g1.GetXaxis().SetNdivisions(7,1)
	# g1.GetXaxis().SetNdivisions(-69);
	# g1.GetXaxis().LabelsOption("h")
	# g1.GetXaxis().SetBinLabel(2, "test")
		


#		l1.Draw("same")
	# g1.GetYaxis().SetMinimum(0)
#	pi = ROOT.TMath.Pi()
	#i = 0
	#while i <= xax.GetXmax():
	#	binIndex = xax.FindBin(i)
#
##   # 	bin_index = xax.FindBin(i)
#    #	xax.SetBinLabel(binIndex,nWrongString_[i])
    #	i+=1
	#gPad.Modified()
	#gPad.Update()
	
#	DrawScat(g1, ";Wrong LR choices / track;Tracks","../images/WrongHitsPerTrk") # ,1)
#		print("Entries:\t"+str(n))





	# DCA threshold arrays, short and long
	#DCAs_ = [list(range(0,525,25))] # , list(range(0,2600,100))]

	# Plot the fraction of wrong hits for the zeroth file (zero threshold)




	# # histType = ["Run","pValues"]
	# # nameType = ["Fraction of wrong tracks","Fraction of tracks with p-value < 5%"]
	
	# # Loop over histogram types

	# files_ = [shortFile, longFile]

	# #fileType = ".png"
	# fileType = ".png"

	# #
	# # Take ratio of all and wrong DCAs
	# #
	
	# ratio_ = []

	# for i_ratio in range(0,1):

	# 	# print(files_[i_ratio])

	# 	# twat1 = files_[i_ratio].Get("plots0/AllHits/DCA")

	# 	# print(3)
	# 	ratio1 = Ratio(files_[i_ratio].Get("plots0/WrongHits/DCA"), files_[i_ratio].Get("plots0/AllHits/DCA")) #, 1)
	# 	ratio2 = Ratio(files_[i_ratio].Get("plots0/WrongHits/DCAOneWrongPerTrack"), files_[i_ratio].Get("plots0/AllHits/DCA")) #, 1)
	# 	#ratio = Ratio(files_[0].Get("plots0/WrongHits/DCA"), files_[0].Get("plots0/AllHits/DCA"), 1)
	# 	DrawHist1D(files_[i_ratio].Get("plots0/AllHits/DCA"), ";Measured DCA [#mum];Hits", "../images/DCAs"+str(i_ratio)+fileType, 1)
	# 	DrawHist1D(ratio1, ";Measured DCA [#mum];Fraction of tracks with a wrong LR choice", "../images/DCARatio"+str(i_ratio)+fileType, 1)
	# 	DrawHist1D(ratio2, ";Measured DCA [#mum];Fraction of tracks with one wrong LR choice", "../images/DCARatioOneWrongPerTrack"+str(i_ratio)+fileType, 1)

	# 	# ratio1 = Ratio(files_[i_ratio].Get("plots0/WrongHits/DCA"), files_[i_ratio].Get("plots0/AllHits/DCA")) #, 1)
	# 	# ratio2 = Ratio(files_[i_ratio].Get("plots0/WrongHits/DCAOneWrongPerTrack"), files_[i_ratio].Get("plots0/AllHits/DCA")) #, 1)
	# 	# #ratio = Ratio(files_[0].Get("plots0/WrongHits/DCA"), files_[0].Get("plots0/AllHits/DCA"), 1)
	# 	# DrawHist1D(files_[i_ratio].Get("plots0/AllHits/DCA"), ";Measured DCA [#mum];Hits", "../images/DCAs"+str(i_ratio)+fileType, i_ratio)
	# 	# DrawHist1D(ratio1, ";Measured DCA [#mum];Fraction of hits with a wrong LR choice", "../images/DCARatio"+str(i_ratio)+fileType, i_ratio)
	# 	# DrawHist1D(ratio2, ";Measured DCA [#mum];Fraction of hits with a wrong LR choice", "../images/DCARatioOneWrongPerTrack"+str(i_ratio)+fileType, i_ratio)
	
	# # Loop over DCA scan
	# for ifile in range(0,1):
	
	# 	print("ifile",ifile)
	
	# 	allHitsTracks_ = []
	# 	allHitsPValues_ = []
	# 	allHitsChiSqrDof_ = []

	# 	wrongHitsTracks_ = []
	# 	wrongHitsPValues_ = []
	# 	wrongHitsChiSqrDof_ = []

	# 	rightHitsTracks_ = []
	# 	rightHitsPValues_ = []
	# 	rightHitsChiSqrDof_ = []

	# 	ambiguousHitsTracks_ = []
	# 	ambiguousHitsPValues_ = []
	# 	ambiguousHitsChiSqrDof_ = []
		
	# 	for ihist in range(0,len(DCAs_[ifile])):
	
	# 		allHitsTracks_.append(files_[ifile].Get("plots"+str(ihist)+"/AllHits/Run"))
	# 		allHitsPValues_.append(files_[ifile].Get("plots"+str(ihist)+"/AllHits/pValues"))
	# 		allHitsChiSqrDof_.append(files_[ifile].Get("plots"+str(ihist)+"/AllHits/ChiSqrDof"))

	# 		wrongHitsTracks_.append(files_[ifile].Get("plots"+str(ihist)+"/WrongHits/Run"))
	# 		wrongHitsPValues_.append(files_[ifile].Get("plots"+str(ihist)+"/WrongHits/pValues"))
	# 		wrongHitsChiSqrDof_.append(files_[ifile].Get("plots"+str(ihist)+"/WrongHits/ChiSqrDof"))

	# 		rightHitsTracks_.append(files_[ifile].Get("plots"+str(ihist)+"/RightHits/Run"))	
	# 		rightHitsPValues_.append(files_[ifile].Get("plots"+str(ihist)+"/RightHits/pValues"))
	# 		rightHitsChiSqrDof_.append(files_[ifile].Get("plots"+str(ihist)+"/RightHits/ChiSqrDof"))

	# 		ambiguousHitsTracks_.append(files_[ifile].Get("plots"+str(ihist)+"/AmbiguousHits/Run"))	
	# 		ambiguousHitsPValues_.append(files_[ifile].Get("plots"+str(ihist)+"/AmbiguousHits/pValues"))
	# 		ambiguousHitsChiSqrDof_.append(files_[ifile].Get("plots"+str(ihist)+"/AmbiguousHits/ChiSqrDof"))

	# 	if(ifile == 0): # Fine scan from 0 - 500 um

	# 		# All tracks
	# 		DrawScat(DefineScat(TotalTracks(allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Total number of tracks", "../images/TotalTracksSimShort"+fileType)
	# 		DrawScat(DefineScat(pValFrac(allHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with p-value < 5%", "../images/pValueFracSimShort"+fileType)
	# 		DrawScat(DefineScat(pValFrac(wrongHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with a wrong LR choice with a p-value < 5%", "../images/pValueWrongFracShort"+fileType)
	# 		# DrawScat(DefineScat(pValFrac(ambiguousHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of ambiguous LR tracks with p-value < 5%", "../images/pValueAmbiguousFracShort"+fileType)
	# 		# DrawScat(DefineScat(Mean(allHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Mean p-value", "../images/pValueMeansShort"+fileType)
	# 		# Fractions of each type of track
	# 		DrawScat(DefineScat(Frac(wrongHitsTracks_, allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with a wrong LR choice", "../images/FracWrongTracksShort"+fileType)
	# 		# DrawScat(DefineScat(Frac(rightHitsTracks_, allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with only correct LR choices", "../images/FracRightTracksShort"+fileType)
	# 		DrawScat(DefineScat(Frac(ambiguousHitsTracks_, allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with an ambiguous LR choice", "../images/FracAmbiguousTracksShort"+fileType)

	# 		DrawScatOverlay(DefineScat(Frac(wrongHitsTracks_, allHitsTracks_), DCAs_[ifile]),DefineScat(Frac(ambiguousHitsTracks_, allHitsTracks_), DCAs_[ifile]),";Low DCA threshold [#mum];Fraction of tracks","../images/FracWrongAmbTracksShort"+fileType)
		
	# 	else: # Coarse scan from 0 - 2500 um

	# 		# All tracks
	# 		DrawScat(DefineScat(TotalTracks(allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Total number of tracks", "../images/TotalTracksSimLong"+fileType)
	# 		# DrawScat(DefineScat(Mean(allHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Mean p-value", "../images/pValueMeansSimLong"+fileType)
	# 		DrawScat(DefineScat(Mean(allHitsChiSqrDof_), DCAs_[ifile]), ";Low DCA threshold [#mum];Mean #chi^{2}/ndf", "../images/chiSqrDofSimLong"+fileType)
	# 		DrawScat(DefineScat(pValFrac(allHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with p-value < 5%", "../images/pValueFracSimLong"+fileType)
	# 		DrawScat(DefineScat(pValFrac(wrongHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of wrong LR tracks with p-value < 5%", "../images/pValueWrongFracLong"+fileType)
	# 		DrawScat(DefineScat(pValFrac(ambiguousHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of ambiguous LR tracks with p-value < 5%", "../images/pValueAmbiguousFracLong"+fileType)
			
	# 		# Fractions of each type of track
	# 		DrawScat(DefineScat(Frac(wrongHitsTracks_, allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with a wrong LR choice", "../images/FracWrongTracksLong"+fileType)
	# 		DrawScat(DefineScat(Frac(rightHitsTracks_, allHitsTracks_, ), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with only right LR choices", "../images/FracRightTracksLong"+fileType)
	# 		DrawScat(DefineScat(Frac(ambiguousHitsTracks_, allHitsTracks_, ), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with an ambiguous LR choice", "../images/FracAmbiguousTracksLong"+fileType)
	
		
	# draw1D(histsArrayCut, DCAsArray, ";p-value;Tracks / 0.005","../Plots/pValues1DExtreme.pdf")
	# drawScat(histsArrayCut, DCAsArray, ";Low DCA Threshold [#mum];Mean p-value","../Plots/pValuesScatExtreme.pdf")

# Execute main
if __name__ == "__main__":
	main()








