from ROOT import TFile, TCanvas, gStyle, TProfile, TLegend

def FancyDraw1D(hist1, title, fname): 

	c0 = TCanvas("","",800,600)

	#hist1.SetStats(0)

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

	# c0.SetLogy()

	hist1.Draw()

	# c0.SetGrid()
	
	c0.SaveAs(fname+".png")
	c0.SaveAs(fname+".pdf")

#names = ["vacuum_20um_truthLR_allTimes","vacuum_20um_truthLR_posTimes","vacuum_20um_mainFit_allTimes","vacuum_20um_mainFit_posTimes","vacuum_20um_fullSeqFit_posTimes"]#,"vacuum_20um_fullSeqFit_posTimes"]
names = ["vacuum_2um_truthLR_allTimes_noMaterial_withBinning", "vacuum_2um_truthLR_allTimes_noMaterial_noBinning"]

for i in range(0,len(names)):
	
#	file = TFile.Open("../runSimPlots/"+names[i]+"/"+names[i]+".root")
	file = TFile.Open("../runSimPlots/"+names[i]+"/simPlots_"+names[i]+".root") 

	hist = file.Get("nonePlusWrong/pValues")

	FancyDraw1D(hist, ";p-values;Tracks","../images/pValues_"+names[i])