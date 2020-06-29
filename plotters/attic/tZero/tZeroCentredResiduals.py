# Format t0 plots, showing the effect of introducing a 28.65 ns t0 offset for garfield tracks

from ROOT import TFile, TCanvas, gStyle, TProfile, TLegend


def FancyDrawOverlay(hist1, hist2, hist3, title, fname): 

	c2 = TCanvas("","",800,600)

	hist1.SetStats(0)
	hist2.SetStats(0)
	hist3.SetStats(0)
	#hist2.SetStats(0)
	
	gStyle.SetStatFormat("6.3g")
	leg = TLegend(0.55,0.65,0.89,0.89)
	#leg.SetHeader("Mean time offset")
	leg.AddEntry(hist1,"#splitline{#bf{Garfield}}{Mean = "+str('%s' % float('%.2g' % hist1.GetMean()))+" #pm "+str('%s' % float('%.1g' % hist1.GetMeanError()))+" ns}")
	leg.AddEntry(hist2,"#splitline{#bf{Gaussian}}{Mean = "+str('%s' % float('%.2g' % hist2.GetMean()))+" #pm "+str('%s' % float('%.1g' % hist1.GetMeanError()))+" ns}")
	leg.AddEntry(hist3,"#splitline{#bf{Truth}}{Mean = "+str('%s' % float('%.3g' % hist3.GetMean()))+" #pm "+str('%s' % float('%.1g' % hist2.GetMeanError()))+" ns}")
	leg.SetBorderSize(0)

	hist1.SetTitle(title)
			
	hist1.GetXaxis().SetTitleSize(.04)
	hist1.GetYaxis().SetTitleSize(.04)
	hist1.GetXaxis().SetTitleOffset(1.1)
	hist1.GetYaxis().SetTitleOffset(1.1)
	hist1.GetXaxis().CenterTitle(1)
	hist1.GetYaxis().CenterTitle(1)
 	hist1.GetYaxis().SetMaxDigits(4)

	hist1.SetLineWidth(3)
	hist2.SetLineWidth(3)	
	hist3.SetLineWidth(3)	

	hist1.SetLineColor(2)	
	hist2.SetLineColor(4)
	hist3.SetLineColor(1)	
	
	hist1.SetMarkerColor(2)	
	hist2.SetMarkerColor(4)
	hist3.SetMarkerColor(1)	

	hist1.Draw()
	hist2.Draw("same")
	hist3.Draw("same")
	leg.Draw("SAME")
	
	c2.SaveAs(fname+".png")
	c2.SaveAs(fname+".pdf")

# Grab files
garfieldFile = TFile.Open("../runSimPlots/garfield/simPlotsMerged0.root") # Garfield, no DCA threshold
# gaussFile = TFile.Open("../runSimPlots_BK/simScanPlots246.root") # Gaussian, no DCA threshold
gaussFile = TFile.Open("../runSimPlots/gauss/simPlotsMerged0.root") # Gaussian, no DCA threshold
perfectFile = TFile.Open("../runSimPlots/perfect/simPlotsMerged0.root") # Truth, no DCA threshold
#goodFile = TFile.Open("../runSimPlots_BK/simScanPlots2865.root")
#badFile = TFile.Open("../runSimPlots_BK/simScanPlots246.root")

# Grab histograms
garfieldHist = garfieldFile.Get("nonePlusWrong/t0Residual")
gaussHist = gaussFile.Get("nonePlusWrong/t0Residual")
perfectHist = perfectFile.Get("nonePlusWrong/t0Residual")

# Plot them
FancyDrawOverlay(garfieldHist, gaussHist, perfectHist, ";True #minus reco t0 [ns];Hits", "../images/t0ResidualsCentred")





