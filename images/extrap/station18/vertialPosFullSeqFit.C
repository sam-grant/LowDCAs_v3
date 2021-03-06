void vertialPosFullSeqFit()
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
   
   TH1F *FullSeqFit__8 = new TH1F("FullSeqFit__8","",400,-200,200);
   FullSeqFit__8->SetBinContent(156,1);
   FullSeqFit__8->SetBinContent(159,1);
   FullSeqFit__8->SetBinContent(160,1);
   FullSeqFit__8->SetBinContent(163,1);
   FullSeqFit__8->SetBinContent(164,3);
   FullSeqFit__8->SetBinContent(165,1);
   FullSeqFit__8->SetBinContent(168,1);
   FullSeqFit__8->SetBinContent(169,1);
   FullSeqFit__8->SetBinContent(170,2);
   FullSeqFit__8->SetBinContent(171,2);
   FullSeqFit__8->SetBinContent(172,2);
   FullSeqFit__8->SetBinContent(173,2);
   FullSeqFit__8->SetBinContent(174,4);
   FullSeqFit__8->SetBinContent(175,2);
   FullSeqFit__8->SetBinContent(176,8);
   FullSeqFit__8->SetBinContent(177,5);
   FullSeqFit__8->SetBinContent(178,9);
   FullSeqFit__8->SetBinContent(179,7);
   FullSeqFit__8->SetBinContent(180,5);
   FullSeqFit__8->SetBinContent(181,1);
   FullSeqFit__8->SetBinContent(182,12);
   FullSeqFit__8->SetBinContent(183,4);
   FullSeqFit__8->SetBinContent(184,8);
   FullSeqFit__8->SetBinContent(185,8);
   FullSeqFit__8->SetBinContent(186,9);
   FullSeqFit__8->SetBinContent(187,11);
   FullSeqFit__8->SetBinContent(188,7);
   FullSeqFit__8->SetBinContent(189,11);
   FullSeqFit__8->SetBinContent(190,10);
   FullSeqFit__8->SetBinContent(191,11);
   FullSeqFit__8->SetBinContent(192,14);
   FullSeqFit__8->SetBinContent(193,7);
   FullSeqFit__8->SetBinContent(194,13);
   FullSeqFit__8->SetBinContent(195,9);
   FullSeqFit__8->SetBinContent(196,8);
   FullSeqFit__8->SetBinContent(197,22);
   FullSeqFit__8->SetBinContent(198,13);
   FullSeqFit__8->SetBinContent(199,17);
   FullSeqFit__8->SetBinContent(200,16);
   FullSeqFit__8->SetBinContent(201,9);
   FullSeqFit__8->SetBinContent(202,13);
   FullSeqFit__8->SetBinContent(203,19);
   FullSeqFit__8->SetBinContent(204,19);
   FullSeqFit__8->SetBinContent(205,7);
   FullSeqFit__8->SetBinContent(206,19);
   FullSeqFit__8->SetBinContent(207,8);
   FullSeqFit__8->SetBinContent(208,8);
   FullSeqFit__8->SetBinContent(209,16);
   FullSeqFit__8->SetBinContent(210,10);
   FullSeqFit__8->SetBinContent(211,6);
   FullSeqFit__8->SetBinContent(212,9);
   FullSeqFit__8->SetBinContent(213,17);
   FullSeqFit__8->SetBinContent(214,8);
   FullSeqFit__8->SetBinContent(215,11);
   FullSeqFit__8->SetBinContent(216,7);
   FullSeqFit__8->SetBinContent(217,8);
   FullSeqFit__8->SetBinContent(218,6);
   FullSeqFit__8->SetBinContent(219,3);
   FullSeqFit__8->SetBinContent(220,3);
   FullSeqFit__8->SetBinContent(221,10);
   FullSeqFit__8->SetBinContent(222,7);
   FullSeqFit__8->SetBinContent(223,7);
   FullSeqFit__8->SetBinContent(224,6);
   FullSeqFit__8->SetBinContent(225,4);
   FullSeqFit__8->SetBinContent(226,3);
   FullSeqFit__8->SetBinContent(227,1);
   FullSeqFit__8->SetBinContent(228,3);
   FullSeqFit__8->SetBinContent(229,1);
   FullSeqFit__8->SetBinContent(230,2);
   FullSeqFit__8->SetBinContent(231,3);
   FullSeqFit__8->SetBinContent(232,1);
   FullSeqFit__8->SetBinContent(233,1);
   FullSeqFit__8->SetBinContent(234,1);
   FullSeqFit__8->SetBinContent(235,2);
   FullSeqFit__8->SetBinContent(239,4);
   FullSeqFit__8->SetBinContent(246,1);
   FullSeqFit__8->SetMinimum(0);
   FullSeqFit__8->SetMaximum(20);
   FullSeqFit__8->SetEntries(532);
   FullSeqFit__8->SetLineWidth(3);
   FullSeqFit__8->GetXaxis()->SetTitle("Vertical decay position [mm]");
   FullSeqFit__8->GetXaxis()->SetRange(101,300);
   FullSeqFit__8->GetXaxis()->CenterTitle(true);
   FullSeqFit__8->GetXaxis()->SetLabelFont(42);
   FullSeqFit__8->GetXaxis()->SetLabelSize(0.035);
   FullSeqFit__8->GetXaxis()->SetTitleOffset(1.1);
   FullSeqFit__8->GetXaxis()->SetTitleFont(42);
   FullSeqFit__8->GetYaxis()->SetTitle("Tracks");
   FullSeqFit__8->GetYaxis()->CenterTitle(true);
   FullSeqFit__8->GetYaxis()->SetNdivisions(4000510);
   FullSeqFit__8->GetYaxis()->SetLabelFont(42);
   FullSeqFit__8->GetYaxis()->SetLabelSize(0.035);
   FullSeqFit__8->GetYaxis()->SetTitleOffset(1.1);
   FullSeqFit__8->GetYaxis()->SetTitleFont(42);
   FullSeqFit__8->GetZaxis()->SetLabelFont(42);
   FullSeqFit__8->GetZaxis()->SetLabelSize(0.035);
   FullSeqFit__8->GetZaxis()->SetTitleSize(0.035);
   FullSeqFit__8->GetZaxis()->SetTitleFont(42);
   FullSeqFit__8->Draw("");
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
