# Plot fraction of p-values < 5% over low DCA thresholds

from ROOT import TFile, TCanvas, TH1F, TH1D, TLegend, TAxis, TAttMarker, TGraph, TGraphErrors
from ROOT import gROOT
from array import array

def Ratio(wrongHist, allHist):#, rebin):

	# Clone to be safe
	# allHist.Rebin(rebin)
	# wrongHist.Rebin(rebin)

	ratio = wrongHist.Clone("ratio")

	ratio.Divide(allHist)

	return ratio

# Return the number of tracks with a p-value less than 5%

def pValFrac(hist):

 	# Loop over the bins
 	# Get bin x-values
 	# if x-value is < 5%, sum the bin contents
 	# Divide by total entries
 	tracksLessThan = 0.0

 	tracks = 0

 	for bin in range(hist.GetNbinsX()):

 		pValue = hist.GetBinCenter(bin+1)
 		print("p-value", pValue)
 		# binVal = hist.GetBinContent(bin+1) + binVal
 		if(pValue < 0.05):

 			tracks = hist.GetBinContent(bin+1) + tracks
 				# fraction = binVal / hist.GetEntries()

 	tracksLessThan = tracks / hist.GetEntries()
 	print(tracksLessThan)

 	return tracksLessThan

def pValFracBROKEN(all_):

 	# Loop over the bins
 	# Get bin x-values
 	# if x-value is < 5%, sum the bin contents
 	# Divide by total entries
 	tracksLessThan_ = []

 	for ihist in range(len(all_)-1):

 		tracks = 0

 		for bin in range(all_[ihist].GetNbinsX()):

 			pValue = all_[ihist].GetBinCenter(bin+1)
 			print("p-value", pValue)
 			# binVal = hist.GetBinContent(bin+1) + binVal
 			if(pValue < 0.05):

 				tracks = all_[ihist].GetBinContent(bin+1) + tracks
 				# fraction = binVal / hist.GetEntries()

 		# print("tracks ",tracks)
 		print(tracks / all_[ihist].GetEntries())
 		tracksLessThan_.append(tracks / all_[ihist].GetEntries())

 	return tracksLessThan_


def DefineScat(x_,y_):

	x, y = array('f'), array('f') #, array('d'), array('d')
	n = 0
	n = len(y_)
	if(n==0):
		return

	print("n :"+str(n))
	for i in range(0,n):

#		frac = wrong_[i].GetEntries() / all_[i].GetEntries()
		# print(i)
		# print(x_[i])
		x.append(x_[i])
		
		#print(y_[i])
		y.append(y_[i])
		

		# print(str(DCAs_[i])+" * "+str(y_)+" * "+str(wrong_[i].GetEntries())+" * "+str(all_[i].GetEntries()))

	return TGraph(n,x,y) #,ex,ey)


def DrawScat(plot, title, fname):

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
	c2.SaveAs(fname)

	return

# Wrap main in a function
def main():

	#shortFile = TFile.Open("../runSimPlots/simScanPlotsTruthT0.root")
	dirName = "garfield"

	imageFmt = ".pdf"

	pValueHists = []
	pValueFractions = []

	for i in range(21):

		file = TFile.Open("../runSimPlots/"+str(dirName)+"/simPlotsMerged"+str(i)+".root")
		hist = file.Get("nonePlusWrong/pValues")
		pValueHists.append(hist)

		frac = pValFrac(pValueHists[i])
		pValueFractions.append(frac)


	print(str(len(pValueHists))+" histograms analysed")

	#pValueFractions = array('f') 
	#frac = pValFrac(pValueHists[19])
	#pValueFractions = pValFrac(pValueHists)

	#for i in range(len(pValueHists)-1): # last one is zero
#
#	#	frac = pValFrac(pValueHists[i])
#	#	print(frac.GetMean())
#
#	#	pValueFractions.append(frac)
#	#	print(frac)

	# Plot them
	DCAs = list(range(0,525,25))

	if(len(DCAs)!=len(pValueFractions)): print("ERROR")

	gr = DefineScat(DCAs, pValueFractions)

	DrawScat(gr,";Low DCA threshold [#mum];Fraction of tracks with p-value < 5%", "../images/pValueFrac_sim_noInflator"+imageFmt)




	#
	# Take ratio of all and wrong DCAs
	#
	
#
#
#		# print(files_[i_ratio])
#
#		# twat1 = files_[i_ratio].Get("plots0/AllHits/DCA")
#
#		# print(3)
#		ratio1 = Ratio(files_[i_ratio].Get("plots0/WrongHits/DCA"), files_[i_ratio].Get("plots0/AllHits/DCA")) #, 1)
#		ratio2 = Ratio(files_[i_ratio].Get("plots0/WrongHits/DCAOneWrongPerTrack"), files_[i_ratio].Get("plots0/AllHits/DCA")) #, 1)
#		#ratio = Ratio(files_[0].Get("plots0/WrongHits/DCA"), files_[0].Get("plots0/AllHits/DCA"), 1)
#		DrawHist1D(files_[i_ratio].Get("plots0/AllHits/DCA"), ";Measured DCA [#mum];Hits", "../images/DCAs"+str(i_ratio)+fileType, 1)
#		DrawHist1D(ratio1, ";Measured DCA [#mum];Fraction of tracks with a wrong LR choice", "../images/DCARatio"+str(i_ratio)+fileType, 1)
#		DrawHist1D(ratio2, ";Measured DCA [#mum];Fraction of tracks with one wrong LR choice", "../images/DCARatioOneWrongPerTrack"+str(i_ratio)+fileType, 1)
#
#		# ratio1 = Ratio(files_[i_ratio].Get("plots0/WrongHits/DCA"), files_[i_ratio].Get("plots0/AllHits/DCA")) #, 1)
#		# ratio2 = Ratio(files_[i_ratio].Get("plots0/WrongHits/DCAOneWrongPerTrack"), files_[i_ratio].Get("plots0/AllHits/DCA")) #, 1)
#		# #ratio = Ratio(files_[0].Get("plots0/WrongHits/DCA"), files_[0].Get("plots0/AllHits/DCA"), 1)
#		# DrawHist1D(files_[i_ratio].Get("plots0/AllHits/DCA"), ";Measured DCA [#mum];Hits", "../images/DCAs"+str(i_ratio)+fileType, i_ratio)
#		# DrawHist1D(ratio1, ";Measured DCA [#mum];Fraction of hits with a wrong LR choice", "../images/DCARatio"+str(i_ratio)+fileType, i_ratio)
#		# DrawHist1D(ratio2, ";Measured DCA [#mum];Fraction of hits with a wrong LR choice", "../images/DCARatioOneWrongPerTrack"+str(i_ratio)+fileType, i_ratio)
#	
#	# Loop over DCA scan
#	for ifile in range(0,1):
#	
#		print("ifile",ifile)
#	
#		allHitsTracks_ = []
#		allHitsPValues_ = []
#		allHitsChiSqrDof_ = []
#
#		wrongHitsTracks_ = []
#		wrongHitsPValues_ = []
#		wrongHitsChiSqrDof_ = []
#
#		rightHitsTracks_ = []
#		rightHitsPValues_ = []
#		rightHitsChiSqrDof_ = []
#
#		ambiguousHitsTracks_ = []
#		ambiguousHitsPValues_ = []
#		ambiguousHitsChiSqrDof_ = []
#		
#		for ihist in range(0,len(DCAs_[ifile])):
#	
#			allHitsTracks_.append(files_[ifile].Get("plots"+str(ihist)+"/AllHits/Run"))
#			allHitsPValues_.append(files_[ifile].Get("plots"+str(ihist)+"/AllHits/pValues"))
#			allHitsChiSqrDof_.append(files_[ifile].Get("plots"+str(ihist)+"/AllHits/ChiSqrDof"))
#
#			wrongHitsTracks_.append(files_[ifile].Get("plots"+str(ihist)+"/WrongHits/Run"))
#			wrongHitsPValues_.append(files_[ifile].Get("plots"+str(ihist)+"/WrongHits/pValues"))
#			wrongHitsChiSqrDof_.append(files_[ifile].Get("plots"+str(ihist)+"/WrongHits/ChiSqrDof"))
#
#			rightHitsTracks_.append(files_[ifile].Get("plots"+str(ihist)+"/RightHits/Run"))	
#			rightHitsPValues_.append(files_[ifile].Get("plots"+str(ihist)+"/RightHits/pValues"))
#			rightHitsChiSqrDof_.append(files_[ifile].Get("plots"+str(ihist)+"/RightHits/ChiSqrDof"))
#
#			ambiguousHitsTracks_.append(files_[ifile].Get("plots"+str(ihist)+"/AmbiguousHits/Run"))	
#			ambiguousHitsPValues_.append(files_[ifile].Get("plots"+str(ihist)+"/AmbiguousHits/pValues"))
#			ambiguousHitsChiSqrDof_.append(files_[ifile].Get("plots"+str(ihist)+"/AmbiguousHits/ChiSqrDof"))
#
#		if(ifile == 0): # Fine scan from 0 - 500 um
#
#			# All tracks
#			DrawScat(DefineScat(TotalTracks(allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Total number of tracks", "../images/TotalTracksSimShort"+fileType)
#			DrawScat(DefineScat(pValFrac(allHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with p-value < 5%", "../images/pValueFracSimShort"+fileType)
#			DrawScat(DefineScat(pValFrac(wrongHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with a wrong LR choice with a p-value < 5%", "../images/pValueWrongFracShort"+fileType)
#			# DrawScat(DefineScat(pValFrac(ambiguousHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of ambiguous LR tracks with p-value < 5%", "../images/pValueAmbiguousFracShort"+fileType)
#			# DrawScat(DefineScat(Mean(allHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Mean p-value", "../images/pValueMeansShort"+fileType)
#			# Fractions of each type of track
#			DrawScat(DefineScat(Frac(wrongHitsTracks_, allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with a wrong LR choice", "../images/FracWrongTracksShort"+fileType)
#			# DrawScat(DefineScat(Frac(rightHitsTracks_, allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with only correct LR choices", "../images/FracRightTracksShort"+fileType)
#			DrawScat(DefineScat(Frac(ambiguousHitsTracks_, allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with an ambiguous LR choice", "../images/FracAmbiguousTracksShort"+fileType)
#
#			DrawScatOverlay(DefineScat(Frac(wrongHitsTracks_, allHitsTracks_), DCAs_[ifile]),DefineScat(Frac(ambiguousHitsTracks_, allHitsTracks_), DCAs_[ifile]),";Low DCA threshold [#mum];Fraction of tracks","../images/FracWrongAmbTracksShort"+fileType)
#		
#		else: # Coarse scan from 0 - 2500 um
#
#			# All tracks
#			DrawScat(DefineScat(TotalTracks(allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Total number of tracks", "../images/TotalTracksSimLong"+fileType)
#			# DrawScat(DefineScat(Mean(allHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Mean p-value", "../images/pValueMeansSimLong"+fileType)
#			DrawScat(DefineScat(Mean(allHitsChiSqrDof_), DCAs_[ifile]), ";Low DCA threshold [#mum];Mean #chi^{2}/ndf", "../images/chiSqrDofSimLong"+fileType)
#			DrawScat(DefineScat(pValFrac(allHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with p-value < 5%", "../images/pValueFracSimLong"+fileType)
#			DrawScat(DefineScat(pValFrac(wrongHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of wrong LR tracks with p-value < 5%", "../images/pValueWrongFracLong"+fileType)
#			DrawScat(DefineScat(pValFrac(ambiguousHitsPValues_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of ambiguous LR tracks with p-value < 5%", "../images/pValueAmbiguousFracLong"+fileType)
#			
#			# Fractions of each type of track
#			DrawScat(DefineScat(Frac(wrongHitsTracks_, allHitsTracks_), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with a wrong LR choice", "../images/FracWrongTracksLong"+fileType)
#			DrawScat(DefineScat(Frac(rightHitsTracks_, allHitsTracks_, ), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with only right LR choices", "../images/FracRightTracksLong"+fileType)
#			DrawScat(DefineScat(Frac(ambiguousHitsTracks_, allHitsTracks_, ), DCAs_[ifile]), ";Low DCA threshold [#mum];Fraction of tracks with an ambiguous LR choice", "../images/FracAmbiguousTracksLong"+fileType)
#	
#		
#	# draw1D(histsArrayCut, DCAsArray, ";p-value;Tracks / 0.005","../Plots/pValues1DExtreme.pdf")
#	# drawScat(histsArrayCut, DCAsArray, ";Low DCA Threshold [#mum];Mean p-value","../Plots/pValuesScatExtreme.pdf")

# Execute main
if __name__ == "__main__":
	main()








