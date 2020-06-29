# General useful pyROOT utilies
from ROOT import TH1
from array import array

def LoadUtils():
	print("Loaded utils.py...\n")
	return

def Ratio(numHist, denHist):

	ratio = numHist.Clone("ratio")

	ratio.Divide(denHist)

	return ratio
