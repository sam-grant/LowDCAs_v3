void radialPosTruthLR()
{
//=========Macro generated from canvas: c/c
//=========  (Tue Jun 30 09:42:32 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(0,0,1,1);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   
   TH1F *TruthLR__9 = new TH1F("TruthLR__9","",400,-200,200);
   TruthLR__9->SetBinContent(157,1);
   TruthLR__9->SetBinContent(163,2);
   TruthLR__9->SetBinContent(164,1);
   TruthLR__9->SetBinContent(166,1);
   TruthLR__9->SetBinContent(167,8);
   TruthLR__9->SetBinContent(168,2);
   TruthLR__9->SetBinContent(169,1);
   TruthLR__9->SetBinContent(170,2);
   TruthLR__9->SetBinContent(171,1);
   TruthLR__9->SetBinContent(172,6);
   TruthLR__9->SetBinContent(173,4);
   TruthLR__9->SetBinContent(174,2);
   TruthLR__9->SetBinContent(175,6);
   TruthLR__9->SetBinContent(176,2);
   TruthLR__9->SetBinContent(177,3);
   TruthLR__9->SetBinContent(178,6);
   TruthLR__9->SetBinContent(179,3);
   TruthLR__9->SetBinContent(180,6);
   TruthLR__9->SetBinContent(181,4);
   TruthLR__9->SetBinContent(182,6);
   TruthLR__9->SetBinContent(183,4);
   TruthLR__9->SetBinContent(184,7);
   TruthLR__9->SetBinContent(185,8);
   TruthLR__9->SetBinContent(186,4);
   TruthLR__9->SetBinContent(187,10);
   TruthLR__9->SetBinContent(188,5);
   TruthLR__9->SetBinContent(189,9);
   TruthLR__9->SetBinContent(190,2);
   TruthLR__9->SetBinContent(191,7);
   TruthLR__9->SetBinContent(192,6);
   TruthLR__9->SetBinContent(193,7);
   TruthLR__9->SetBinContent(194,3);
   TruthLR__9->SetBinContent(195,3);
   TruthLR__9->SetBinContent(196,12);
   TruthLR__9->SetBinContent(197,7);
   TruthLR__9->SetBinContent(198,17);
   TruthLR__9->SetBinContent(199,11);
   TruthLR__9->SetBinContent(200,11);
   TruthLR__9->SetBinContent(201,5);
   TruthLR__9->SetBinContent(202,13);
   TruthLR__9->SetBinContent(203,10);
   TruthLR__9->SetBinContent(204,11);
   TruthLR__9->SetBinContent(205,6);
   TruthLR__9->SetBinContent(206,9);
   TruthLR__9->SetBinContent(207,7);
   TruthLR__9->SetBinContent(208,9);
   TruthLR__9->SetBinContent(209,12);
   TruthLR__9->SetBinContent(210,6);
   TruthLR__9->SetBinContent(211,15);
   TruthLR__9->SetBinContent(212,6);
   TruthLR__9->SetBinContent(213,5);
   TruthLR__9->SetBinContent(214,15);
   TruthLR__9->SetBinContent(215,8);
   TruthLR__9->SetBinContent(216,10);
   TruthLR__9->SetBinContent(217,13);
   TruthLR__9->SetBinContent(218,12);
   TruthLR__9->SetBinContent(219,13);
   TruthLR__9->SetBinContent(220,7);
   TruthLR__9->SetBinContent(221,5);
   TruthLR__9->SetBinContent(222,11);
   TruthLR__9->SetBinContent(223,8);
   TruthLR__9->SetBinContent(224,8);
   TruthLR__9->SetBinContent(225,11);
   TruthLR__9->SetBinContent(226,8);
   TruthLR__9->SetBinContent(227,6);
   TruthLR__9->SetBinContent(228,3);
   TruthLR__9->SetBinContent(229,2);
   TruthLR__9->SetBinContent(230,6);
   TruthLR__9->SetBinContent(231,4);
   TruthLR__9->SetBinContent(232,5);
   TruthLR__9->SetBinContent(233,2);
   TruthLR__9->SetBinContent(234,2);
   TruthLR__9->SetBinContent(236,2);
   TruthLR__9->SetBinContent(237,4);
   TruthLR__9->SetBinContent(239,1);
   TruthLR__9->SetBinContent(240,2);
   TruthLR__9->SetBinContent(241,5);
   TruthLR__9->SetBinContent(242,3);
   TruthLR__9->SetBinContent(245,1);
   TruthLR__9->SetMinimum(0);
   TruthLR__9->SetMaximum(20);
   TruthLR__9->SetEntries(491);
   TruthLR__9->SetLineWidth(3);
   TruthLR__9->GetXaxis()->SetTitle("Radial decay position [mm]");
   TruthLR__9->GetXaxis()->SetRange(101,300);
   TruthLR__9->GetXaxis()->CenterTitle(true);
   TruthLR__9->GetXaxis()->SetLabelFont(42);
   TruthLR__9->GetXaxis()->SetLabelSize(0.035);
   TruthLR__9->GetXaxis()->SetTitleOffset(1.1);
   TruthLR__9->GetXaxis()->SetTitleFont(42);
   TruthLR__9->GetYaxis()->SetTitle("Tracks");
   TruthLR__9->GetYaxis()->CenterTitle(true);
   TruthLR__9->GetYaxis()->SetNdivisions(4000510);
   TruthLR__9->GetYaxis()->SetLabelFont(42);
   TruthLR__9->GetYaxis()->SetLabelSize(0.035);
   TruthLR__9->GetYaxis()->SetTitleOffset(1.1);
   TruthLR__9->GetYaxis()->SetTitleFont(42);
   TruthLR__9->GetZaxis()->SetLabelFont(42);
   TruthLR__9->GetZaxis()->SetLabelSize(0.035);
   TruthLR__9->GetZaxis()->SetTitleSize(0.035);
   TruthLR__9->GetZaxis()->SetTitleFont(42);
   TruthLR__9->Draw("");
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
