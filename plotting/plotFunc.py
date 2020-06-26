from ROOT import TH1, TH2, TGraphErrors, TCanvas, TLegend, gStyle
from array import array

# Need some overlay functionality, and TGraphErrors. 
# Get these from truthLRPlotter.py

def LoadPlotFunc ():
	print("Loaded plotFunc.py...\n")
	return

def FancyDraw1D(hist, title, fname): 

	c = TCanvas("c","c",800,600)

	hist.SetTitle(title)
			
	hist.GetXaxis().SetTitleSize(.04)
	hist.GetYaxis().SetTitleSize(.04)
	hist.GetXaxis().SetTitleOffset(1.1)
	hist.GetYaxis().SetTitleOffset(1.1)
	hist.GetXaxis().CenterTitle(1)
	hist.GetYaxis().CenterTitle(1)
 	hist.GetYaxis().SetMaxDigits(4)

	hist.SetLineWidth(3)
	hist.SetLineColor(1)	
	hist.SetLineColor(1)

	hist.Draw()
	
	c.SaveAs(fname+".C")
	c.SaveAs(fname+".pdf")

	return

def FancyDraw2D(hist, title, fname): 

	c = TCanvas("c","c",800,600)

	hist.SetTitle(title)
			
	hist.GetXaxis().SetTitleSize(.04)
	hist.GetYaxis().SetTitleSize(.04)
	hist.GetXaxis().SetTitleOffset(1.1)
	hist.GetYaxis().SetTitleOffset(1.1)
	hist.GetXaxis().CenterTitle(1)
	hist.GetYaxis().CenterTitle(1)
 	hist.GetYaxis().SetMaxDigits(4)

	gStyle.SetPalette(55)
	c.SetRightMargin(0.13)

	hist.Draw("COLZ")
	
	# c.SaveAs(fname+".png")
	c.SaveAs(fname+".pdf")

	return

def DefineScat(x_, y_):

	x, y, ex, ey = array('d'), array('d'), array('d'), array('d')
	n = 0
	n = len(x_)
	if(n==0):
		return

	for i in range(0,n):

		x.append(x_[i])

		ex.append(0)
		y.append(y_[i])
		ey.append(0)

	return TGraphErrors(n,x,y,ex,ey)
	
def DefineScatErrors(x_, ex_, y_, ey_):

	x, y, ex, ey = array('d'), array('d'), array('d'), array('d')
	n = 0
	n = len(x_)

	if(n==0):
		return

	for i in range(0,n):

		x.append(x_[i])

		ex.append(0)
		y.append(y_[i])
		ey.append(ey_[i])

	return TGraphErrors(n,x,y,ex,ey)

def DrawScat(graph, title, fname): #, grid):

	c = TCanvas("c","c",800,600)

	graph.SetTitle(title)			
	graph.GetXaxis().SetTitleSize(.04)
	graph.GetYaxis().SetTitleSize(.04)
	graph.GetXaxis().SetTitleOffset(1.2)
	graph.GetYaxis().SetTitleOffset(1.25)
	graph.GetXaxis().CenterTitle(1)
	graph.GetYaxis().CenterTitle(1)
	graph.GetYaxis().SetMaxDigits(4)
	graph.SetMarkerStyle(20) # Full circle
	graph.Draw("AP")
	# c.SetRightMargin(0.13)
	# c.SetGridy()
	c.SaveAs(fname+".pdf")
	c.SaveAs(fname+".C")
	# c2.SaveAs(fname+".pdf")

	return

def DrawScatOverlay(graph1, graph2, name1, name2, title, fname): #, grid):

	c = TCanvas("c","c",800,600)

	leg = TLegend(0.69,0.89,0.69,0.89)
	leg.AddEntry(graph1,name1)
	leg.AddEntry(graph2,name2)
	leg.SetBorderSize(0)

	graph1.SetTitle(title)			
	graph1.GetXaxis().SetTitleSize(.04)
	graph1.GetYaxis().SetTitleSize(.04)
	graph1.GetXaxis().SetTitleOffset(1.2)
	graph1.GetYaxis().SetTitleOffset(1.2)
	graph1.GetXaxis().CenterTitle(1)
	graph1.GetYaxis().CenterTitle(1)
	graph1.GetYaxis().SetMaxDigits(4)
	graph1.SetMarkerStyle(20) # Full circle
	graph2.SetMarkerStyle(24) # Open circle
	graph1.Draw("AP")
	graph2.Draw("P SAME")
	leg.Draw("same")
	# c.SetRightMargin(0.13)
	# c.SetGridy()
	c.SaveAs(fname+".pdf")
	c.SaveAs(fname+".C")
	# c2.SaveAs(fname+".pdf")

	return

def DrawScatOverlay3(graph1, graph2, graph3, name1, name2, name3, title, fname): #, grid):

	c = TCanvas("c","c",800,600)

	leg = TLegend(0.69,0.89,0.69,0.89)
	leg.AddEntry(graph1,name1)
	leg.AddEntry(graph2,name2)
	leg.AddEntry(graph3,name3)
	leg.SetBorderSize(0)

	graph1.SetTitle(title)			
	graph1.GetXaxis().SetTitleSize(.04)
	graph1.GetYaxis().SetTitleSize(.04)
	graph1.GetXaxis().SetTitleOffset(1.2)
	graph1.GetYaxis().SetTitleOffset(1.2)
	graph1.GetXaxis().CenterTitle(1)
	graph1.GetYaxis().CenterTitle(1)
	graph1.GetYaxis().SetMaxDigits(4)
	graph1.SetMarkerStyle(20) # Full circle
	graph2.SetMarkerStyle(24) # Open circle
	graph3.SetMarkerStyle(22) # Full triangle
	graph1.Draw("AP")
	graph2.Draw("P SAME")
	graph3.Draw("P SAME")
	leg.Draw("same")
	# c.SetRightMargin(0.13)
	# c.SetGridy()
	c.SaveAs(fname+".pdf")
	c.SaveAs(fname+".C")
	# c2.SaveAs(fname+".pdf")

	return

def pValFrac(hist):

 	# Loop over the bins
 	# Get bin x-values
 	# if x-value is < 5%, sum the bin contents
 	# Divide by total entries
 	tracksLessThan = 0.0

 	tracks = 0

 	for bin in range(hist.GetNbinsX()):

 		pValue = hist.GetBinCenter(bin+1)
 		# print("p-value", pValue)
 		# binVal = hist.GetBinContent(bin+1) + binVal
 		if(pValue < 0.05):

 			tracks = hist.GetBinContent(bin+1) + tracks
 				# fraction = binVal / hist.GetEntries()

 	tracksLessThan = tracks / hist.GetEntries()
 	# print(tracksLessThan)

 	return tracksLessThan

def DrawManyScat(plots_, title, fname): 

	c2 = TCanvas("c2","",800,600)

	l1 = TLegend(0.59,0.39,0.89,0.89)
	l1.SetHeader("#bf{Low DCA thresholds}")
	dca = 0
	l1.AddEntry(plots_[0],str(dca)+" mm")
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
	c2.SaveAs(fname+".C")
	c2.SaveAs(fname+".pdf")

	return