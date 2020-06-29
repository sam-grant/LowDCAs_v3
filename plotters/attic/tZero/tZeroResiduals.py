# Format t0 plots, showing the effect of introducing a 28.65 ns t0 offset for garfield tracks

from ROOT import TFile, TCanvas, gStyle, TProfile, TLegend

def FancyDraw1D(hist1, title, fname): 

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

	hist1.Draw()

	c0.SetGrid()
	
	c0.SaveAs(fname+".png")

def FancyDraw2D(hist,title,fname): 

	c1 = TCanvas("c1","",800,600)

	hist.SetTitle(title)
			
	hist.GetXaxis().SetTitleSize(.04)
	hist.GetYaxis().SetTitleSize(.04)
	hist.GetXaxis().SetTitleOffset(1.1)
	hist.GetYaxis().SetTitleOffset(1.25)
	hist.GetXaxis().CenterTitle(1)
	hist.GetYaxis().CenterTitle(1)
	hist.GetYaxis().SetMaxDigits(4)

	hist.SetLineWidth(3)
	hist.SetLineColor(1)

	gStyle.SetPalette(55)
	hist.Draw("COLZ")
	
	c1.SaveAs(fname+".png")
	c1.SaveAs(fname+".pdf")

def FancyDrawOverlay(hist1, hist2, title, fname): 

	c2 = TCanvas("","",800,600)

	hist1.SetStats(0)
	#hist2.SetStats(0)
	
	gStyle.SetStatFormat("6.3g")
	leg = TLegend(0.55,0.65,0.89,0.89)
	#leg.SetHeader("Mean time offset")
	leg.AddEntry(hist1,"#splitline{Offset = 28.65 ns}{Mean = "+str('%s' % float('%.2g' % hist1.GetMean()))+"#pm"+str('%s' % float('%.1g' % hist1.GetMeanError()))+" ns}")
	leg.AddEntry(hist2,"#splitline{Offset = 24.60 ns}{Mean = "+str('%s' % float('%.3g' % hist2.GetMean()))+"#pm"+str('%s' % float('%.1g' % hist2.GetMeanError()))+" ns}")
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

	hist1.SetLineColor(4)	
	hist2.SetLineColor(2)

	hist1.SetMarkerColor(4)	
	hist2.SetMarkerColor(2)

	hist1.Draw()
	hist2.Draw("same")
	leg.Draw("SAME")
	
	c2.SaveAs(fname+".png")
	c2.SaveAs(fname+".pdf")

# Grab files
goodFile = TFile.Open("../runSimPlots_BK/simScanPlots2865.root")
badFile = TFile.Open("../runSimPlots_BK/simScanPlots246.root")

#goodFile = TFile.Open("../runSimPlots_BK/simScanPlots2865.root")
#badFile = TFile.Open("../runSimPlots_BK/simScanPlots246.root")

# Grab 2D histograms
h1 = goodFile.Get("plots0/AllHits/t0ResidualVersusDCA")
h2 = badFile.Get("plots0/AllHits/t0ResidualVersusDCA")

# Plot them
h1.SetStats(0)
h2.SetStats(0)
h1.GetXaxis().SetRangeUser(0,2500)
#h2.GetXaxis().SetRangeUser(0,2500)
FancyDraw2D(h1, ";Measured DCA [#mum];True #minus reco t0 [ns]","../images/t0ResidualVersusDCA2861")
FancyDraw2D(h2, ";Measured DCA [#mum];True #minus reco t0 [ns]","../images/t0ResidualVersusDCA246")

# Take profiles
FancyDraw1D(h1.ProfileX(), ";Measured DCA [#mum];True #minus reco t0 mean [ns]", "../images/t0ResidualVersusDCAProfile" )

# Grab 1D histograms
h3 = goodFile.Get("plots0/AllHits/t0Residual")
h4 = badFile.Get("plots0/AllHits/t0Residual")

FancyDrawOverlay(h3, h4, "Garfield mean time offsets;True #minus reco t0 [ns];Hits", "../images/t0Residuals")