from ROOT import gROOT, TFile
from array import array
from plotFunc import *

LoadPlotFunc()

nWrong = [ "noneWrong", "oneWrong", "twoWrong", "threeWrong", "fourWrong", "fiveWrong", "fivePlusWrong" ]

thresholds = [ "0.000", "0.025", "0.050", "0.075","0.100",
	    "0.125", "0.150", "0.175", "0.200",
	    "0.225", "0.250", "0.275", "0.300",
	    "0.325", "0.350", "0.375", "0.400",
	    "0.425", "0.450", "0.475", "0.500" ] 


entries = []

tgr_ = []


for i_thres in range(len(thresholds)):

	if(((float(thresholds[i_thres])/.1).is_integer())==0): continue

	print(thresholds[i_thres])

	tmp = []

	for i_nWrong in range(len(nWrong)):

		file = TFile.Open("../runNominalSimScan/"+nWrong[i_nWrong]+"/simPlots_coarse.root")

		h1 = file.Get(thresholds[i_thres]+"/Run")

		print("thresholds[i_thres]\t"+thresholds[i_thres])

		print("h1.GetEntries()\t"+str(h1.GetEntries()))

		tmp.append(h1.GetEntries())

	print(len(tmp))

	tgr = DefineScat([1,2,3,4,5,6,7], tmp)

	# entries.append(tmp)

	# 
	# Now plot

# print(len(entries))

# for i_tgr in range(len(entries)):

# 	tgr = DefineScat([1,2,3,4,5,6,7], entries[i_tgr]) # this needs to be number of tracks versus nwrong

 	tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(0 + 1.),"None wrong")
 	tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(1 + 1.),"One wrong")
 	tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(2 + 1.),"Two wrong")
 	tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(3 + 1.),"Three wrong")
 	tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(4 + 1.),"Four wrong")
 	tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(5 + 1.),"Five wrong")
 	tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(6 + 1.),"Five+ wrong")
 	tgr.GetXaxis().LabelsOption("h")
 	tgr_.append(tgr)


	tgr.GetHistogram().SetMinimum(0)
	tgr.GetHistogram().SetMaximum(1000)

DrawManyScat(tgr_,";Wrong LR choices / track;Tracks","../images/WrongHitsPerCoarseLowDCA")





# for i_graph in range(0,len(nWrongEntriesPerThres_)):
# 	tgr = DefineScat([1,2,3,4,5,6,7], nWrongEntriesPerThres_[i_graph])
# 	if(i_graph==0):
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(0 + 1.),"None wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(1 + 1.),"One wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(2 + 1.),"Two wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(3 + 1.),"Three wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(4 + 1.),"Four wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(5 + 1.),"Five wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(6 + 1.),"Five+ wrong")
# 		tgr.GetXaxis().LabelsOption("h")
# 		tgr.GetHistogram().SetMinimum(0)
# 		tgr.GetHistogram().SetMaximum(2500)
# 	tgr_.append(tgr)
# 



# 		nWrongEntries_ = []
# 		# print("Low DCA threshold:\t"+str(DCAs_[i_thres])+" um")
		

	
# 		print("Low DCA threshold:\t"+str(DCAs_[i_thres])+" um")
# 		for i_wrong in range(0, len(nWrong)):
# 			tmp = files_[i_thres].Get(nWrong[i_wrong]+"/Run")
# 			n = tmp.GetEntries()
# 			# Print number of entries
# 			print(nWrong[i_wrong]+"\t"+str(n))
	
# 		# Append into an array
# 		nWrongEntries_.append(n)
# 	# Append each list into another list, per threshold
# 	nWrongEntriesPerThres_.append(nWrongEntries_)
# 	# print(nPlusWrong[i_wrong]+"/Run")
# # Define them all as TGraphs 
# tgr_ = []
# 	l1 = TLegend(0.69,0.69)
# for i_graph in range(0,len(nWrongEntriesPerThres_)):
# 	tgr = DefineScat([1,2,3,4,5,6,7], nWrongEntriesPerThres_[i_graph])
# 	if(i_graph==0):
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(0 + 1.),"None wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(1 + 1.),"One wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(2 + 1.),"Two wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(3 + 1.),"Three wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(4 + 1.),"Four wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(5 + 1.),"Five wrong")
# 		tgr.GetXaxis().SetBinLabel(tgr.GetXaxis().FindBin(6 + 1.),"Five+ wrong")
# 		tgr.GetXaxis().LabelsOption("h")
# 		tgr.GetHistogram().SetMinimum(0)
# 		tgr.GetHistogram().SetMaximum(2500)
# 	tgr_.append(tgr)
# DrawManyScat(tgr_,";Wrong LR choices / track;Tracks","../images/WrongHitsPerTrk")
	
	#################################################################################

	# tmp = files_[0].Get(nPlusWrong[i_wrong]+"/Run")
#	g1 = DefineScat([1,2,3,4,5,6,7], nWrongEntriesPerThres_[i_counter])
#	i_counter = i_counter + 1
#	l1.AddEntry(g1,str(DCAs_[i_thres]))
#	g1.SetMarkerColor(i_thres)
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
#    #	xax.SetBinLabel(binIndex,nWrong[i])
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

# # Execute main
# if __name__ == "__main__":
# 	main()








