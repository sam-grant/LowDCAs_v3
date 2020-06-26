# Plot radial and vertical distributions for each fit mode, with and without quality

from ROOT import TFile, TH1
from plotFunc import LoadPlotFunc, FancyDraw1D

LoadPlotFunc()


fnames = [ "nonePlusWrong/simPlots.root" ] #"magicPlots_noQ.root" , "magicPlots_Q.root"]
fitModes = [ "MainFit", "FullSeqFit", "TruthLR", "FlipLR" ] 
stations = [ "station12", "station18" ]

for i in range(len(fnames)): # quality on/off files

	# get file
	file = TFile.Open("../runNominalSim/"+fnames[i])
	print(file)

	for j in range(len(fitModes)): # fit modes 

		for k in range(len(stations)): # stations 

			radial = file.Get("extrapPlots"+fitModes[j]+"/vertices/"+stations[k]+"/h_radialPos") 
			vertical = file.Get("extrapPlots"+fitModes[j]+"/vertices/"+stations[k]+"/h_verticalPos")

			radial.GetXaxis().SetRangeUser(-100,100)
			vertical.GetXaxis().SetRangeUser(-100,100)

			# print(radial)
			# print(vertical)

			# Now plot

			FancyDraw1D(radial, ";Radial decay position [mm];Tracks", "../images/extrap/"+stations[k]+"_"+fitModes[j]+"_radialPos")
			FancyDraw1D(vertical, ";Vertical decay position [mm];Tracks", "../images/extrap/"+stations[k]+"_"+fitModes[j]+"_vertialPos")