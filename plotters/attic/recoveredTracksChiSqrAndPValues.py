from ROOT import TFile, TH1
from plotFunc import * 

LoadPlotFunc()

mode = ["flip", "noFlip"]
plots = ["pValues", "ChiSqrDof"] 
config = ["_recoveredTracks"]
files = ["../extrapolation/trackRecoPlots.root" ] 

for i in range(len(files)):

	file = TFile.Open(files[i])

	for j in range(len(mode)):

		for k in range(len(plots)):

			hist = file.Get(mode[j]+"/"+plots[k])
			print(mode[k]+"/"+plots[k])
	
			if(j==0 and k==0): 
				FancyDraw1D(hist, ";p-values;Tracks", "../images/flippedTracks/pValues"+config[i])
			if(j==0 and k==1): 
				FancyDraw1D(hist, ";p-values;Tracks", "../images/flippedTracks/chiSqrDof"+config[i])
			if(j==1 and k==0):
				FancyDraw1D(hist, ";#chi^{2}/NDF;Tracks", "../images/nonFlippedTracks/pValues"+config[i])
			if(j==1 and k==1):
				FancyDraw1D(hist, ";#chi^{2}/NDF;Tracks", "../images/nonFlippedTracks/chiSqrDof"+config[i])
