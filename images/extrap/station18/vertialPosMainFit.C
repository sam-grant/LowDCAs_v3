void vertialPosMainFit()
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
   
   TH1F *MainFit__4 = new TH1F("MainFit__4","",400,-200,200);
   MainFit__4->SetBinContent(153,1);
   MainFit__4->SetBinContent(160,1);
   MainFit__4->SetBinContent(163,1);
   MainFit__4->SetBinContent(164,1);
   MainFit__4->SetBinContent(166,1);
   MainFit__4->SetBinContent(167,1);
   MainFit__4->SetBinContent(168,1);
   MainFit__4->SetBinContent(170,3);
   MainFit__4->SetBinContent(171,1);
   MainFit__4->SetBinContent(172,2);
   MainFit__4->SetBinContent(173,3);
   MainFit__4->SetBinContent(174,2);
   MainFit__4->SetBinContent(175,2);
   MainFit__4->SetBinContent(176,6);
   MainFit__4->SetBinContent(177,4);
   MainFit__4->SetBinContent(178,6);
   MainFit__4->SetBinContent(179,2);
   MainFit__4->SetBinContent(180,5);
   MainFit__4->SetBinContent(181,2);
   MainFit__4->SetBinContent(182,7);
   MainFit__4->SetBinContent(183,5);
   MainFit__4->SetBinContent(184,7);
   MainFit__4->SetBinContent(185,9);
   MainFit__4->SetBinContent(186,8);
   MainFit__4->SetBinContent(187,10);
   MainFit__4->SetBinContent(188,5);
   MainFit__4->SetBinContent(189,13);
   MainFit__4->SetBinContent(190,10);
   MainFit__4->SetBinContent(191,9);
   MainFit__4->SetBinContent(192,10);
   MainFit__4->SetBinContent(193,6);
   MainFit__4->SetBinContent(194,10);
   MainFit__4->SetBinContent(195,7);
   MainFit__4->SetBinContent(196,8);
   MainFit__4->SetBinContent(197,14);
   MainFit__4->SetBinContent(198,9);
   MainFit__4->SetBinContent(199,15);
   MainFit__4->SetBinContent(200,14);
   MainFit__4->SetBinContent(201,6);
   MainFit__4->SetBinContent(202,8);
   MainFit__4->SetBinContent(203,15);
   MainFit__4->SetBinContent(204,14);
   MainFit__4->SetBinContent(205,3);
   MainFit__4->SetBinContent(206,14);
   MainFit__4->SetBinContent(207,10);
   MainFit__4->SetBinContent(208,7);
   MainFit__4->SetBinContent(209,16);
   MainFit__4->SetBinContent(210,10);
   MainFit__4->SetBinContent(211,6);
   MainFit__4->SetBinContent(212,6);
   MainFit__4->SetBinContent(213,14);
   MainFit__4->SetBinContent(214,7);
   MainFit__4->SetBinContent(215,4);
   MainFit__4->SetBinContent(216,6);
   MainFit__4->SetBinContent(217,4);
   MainFit__4->SetBinContent(218,4);
   MainFit__4->SetBinContent(219,2);
   MainFit__4->SetBinContent(220,1);
   MainFit__4->SetBinContent(221,9);
   MainFit__4->SetBinContent(222,3);
   MainFit__4->SetBinContent(223,5);
   MainFit__4->SetBinContent(224,6);
   MainFit__4->SetBinContent(225,3);
   MainFit__4->SetBinContent(226,3);
   MainFit__4->SetBinContent(227,1);
   MainFit__4->SetBinContent(228,1);
   MainFit__4->SetBinContent(230,1);
   MainFit__4->SetBinContent(231,2);
   MainFit__4->SetBinContent(232,2);
   MainFit__4->SetBinContent(234,3);
   MainFit__4->SetBinContent(235,1);
   MainFit__4->SetBinContent(236,1);
   MainFit__4->SetBinContent(246,1);
   MainFit__4->SetMinimum(0);
   MainFit__4->SetMaximum(20);
   MainFit__4->SetEntries(420);
   MainFit__4->SetLineWidth(3);
   MainFit__4->GetXaxis()->SetTitle("Vertical decay position [mm]");
   MainFit__4->GetXaxis()->SetRange(101,300);
   MainFit__4->GetXaxis()->CenterTitle(true);
   MainFit__4->GetXaxis()->SetLabelFont(42);
   MainFit__4->GetXaxis()->SetLabelSize(0.035);
   MainFit__4->GetXaxis()->SetTitleOffset(1.1);
   MainFit__4->GetXaxis()->SetTitleFont(42);
   MainFit__4->GetYaxis()->SetTitle("Tracks");
   MainFit__4->GetYaxis()->CenterTitle(true);
   MainFit__4->GetYaxis()->SetNdivisions(4000510);
   MainFit__4->GetYaxis()->SetLabelFont(42);
   MainFit__4->GetYaxis()->SetLabelSize(0.035);
   MainFit__4->GetYaxis()->SetTitleOffset(1.1);
   MainFit__4->GetYaxis()->SetTitleFont(42);
   MainFit__4->GetZaxis()->SetLabelFont(42);
   MainFit__4->GetZaxis()->SetLabelSize(0.035);
   MainFit__4->GetZaxis()->SetTitleSize(0.035);
   MainFit__4->GetZaxis()->SetTitleFont(42);
   MainFit__4->Draw("");
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
