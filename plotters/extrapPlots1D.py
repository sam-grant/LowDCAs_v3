# Plot radial and vertical distributions for each fit mode, with and without quality. 
# Overlay truth LR, full Seq fit, mainFit

from ROOT import TFile, TH1
from plotFunc import *

LoadPlotFunc()


fnames = [ "nominalSimPlotsQ.root" ] #"nominalSimPlotsNoQ.root",  ]

fitModes = [ "MainFit", "FullSeqFit", "TruthLR", "FlipLR" ] 

stations = [ "station12", "station18" ]

# Arrays to hold histograms


for i in range(len(fnames)): # quality on/off files

	radial12_ = []
	vertical12_ = []
	radial18_ = []
	vertical18_ = []

	# get file
	file = TFile.Open("../plots/nominalSim/"+fnames[i])

	print(file)

	for j in range(len(fitModes)): # fit modes 

		for k in range(len(stations)): # stations 

			radial = file.Get("extrapPlots"+fitModes[j]+"/vertices/"+stations[k]+"/h_radialPos") 
			vertical = file.Get("extrapPlots"+fitModes[j]+"/vertices/"+stations[k]+"/h_verticalPos")

			radial.SetName(fitModes[j])
			vertical.SetName(fitModes[j])

			if(k==0):
				radial12_.append(radial)
				vertical12_.append(vertical)
				print("Station 12, radial mean:\t"+str(radial.GetMean())+"+/-"+str(radial.GetMeanError()))
			else:
				radial18_.append(radial)
				vertical18_.append(vertical)

			radial.GetXaxis().SetRangeUser(-100,100)
			vertical.GetXaxis().SetRangeUser(-100,100)

			radial.GetYaxis().SetRangeUser(0,20)
			vertical.GetYaxis().SetRangeUser(0,20)			

			# Plot invidual ones
			FancyDraw1D(radial, ";Radial decay position [mm];Tracks", "../images/extrap/"+stations[k]+"/radialPos"+fitModes[j])
			FancyDraw1D(vertical, ";Vertical decay position [mm];Tracks", "../images/extrap/"+stations[k]+"/vertialPos"+fitModes[j])


	# FancyDraw1DOverlay3(radial12_[0],radial12_[1],radial12_[2],"test","../images/extrap/"+stations[0]+"/radialPosOverlay")
	FancyDraw1DOverlay3(radial12_[0],radial12_[1],radial12_[2],"Station 12;Radial decay position [mm];Tracks","../images/extrap/"+stations[0]+"/radialPosOverlay3")
	FancyDraw1DOverlay3(radial18_[0],radial18_[1],radial18_[2],"Station 18;Radial decay position [mm];Tracks","../images/extrap/"+stations[1]+"/radialPosOverlay3")
	FancyDraw1DOverlay3(vertical12_[0],vertical12_[1],vertical12_[2],"Station 12;Vertical decay position [mm];Tracks","../images/extrap/"+stations[0]+"/verticalPosOverlay3")
	FancyDraw1DOverlay3(vertical18_[0],vertical18_[1],vertical18_[2],"Station 18;Vertical decay position [mm];Tracks","../images/extrap/"+stations[1]+"/verticalPosOverlay3")

	# FancyDraw1DOverlay(radial12_[2],radial12_[1],"Station 12;Radial decay position [mm];Tracks","../images/extrap/"+stations[0]+"/radialPosOverlay")
	# FancyDraw1DOverlay(radial18_[2],radial18_[1],"Station 18;Radial decay position [mm];Tracks","../images/extrap/"+stations[1]+"/radialPosOverlay")
	# FancyDraw1DOverlay(vertical12_[2],vertical12_[1],"Station 12;Vertical decay position [mm];Tracks","../images/extrap/"+stations[0]+"/verticalPosOverlay")
	# FancyDraw1DOverlay(vertical18_[2],vertical18_[1],"Station 18;Vertical decay position [mm];Tracks","../images/extrap/"+stations[1]+"/verticalPosOverlay")




