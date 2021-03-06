void verticalPosOverlay3()
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
   
   TH1F *MainFit__26 = new TH1F("MainFit__26","Station 18",400,-200,200);
   MainFit__26->SetBinContent(153,1);
   MainFit__26->SetBinContent(160,1);
   MainFit__26->SetBinContent(163,1);
   MainFit__26->SetBinContent(164,1);
   MainFit__26->SetBinContent(166,1);
   MainFit__26->SetBinContent(167,1);
   MainFit__26->SetBinContent(168,1);
   MainFit__26->SetBinContent(170,3);
   MainFit__26->SetBinContent(171,1);
   MainFit__26->SetBinContent(172,2);
   MainFit__26->SetBinContent(173,3);
   MainFit__26->SetBinContent(174,2);
   MainFit__26->SetBinContent(175,2);
   MainFit__26->SetBinContent(176,6);
   MainFit__26->SetBinContent(177,4);
   MainFit__26->SetBinContent(178,6);
   MainFit__26->SetBinContent(179,2);
   MainFit__26->SetBinContent(180,5);
   MainFit__26->SetBinContent(181,2);
   MainFit__26->SetBinContent(182,7);
   MainFit__26->SetBinContent(183,5);
   MainFit__26->SetBinContent(184,7);
   MainFit__26->SetBinContent(185,9);
   MainFit__26->SetBinContent(186,8);
   MainFit__26->SetBinContent(187,10);
   MainFit__26->SetBinContent(188,5);
   MainFit__26->SetBinContent(189,13);
   MainFit__26->SetBinContent(190,10);
   MainFit__26->SetBinContent(191,9);
   MainFit__26->SetBinContent(192,10);
   MainFit__26->SetBinContent(193,6);
   MainFit__26->SetBinContent(194,10);
   MainFit__26->SetBinContent(195,7);
   MainFit__26->SetBinContent(196,8);
   MainFit__26->SetBinContent(197,14);
   MainFit__26->SetBinContent(198,9);
   MainFit__26->SetBinContent(199,15);
   MainFit__26->SetBinContent(200,14);
   MainFit__26->SetBinContent(201,6);
   MainFit__26->SetBinContent(202,8);
   MainFit__26->SetBinContent(203,15);
   MainFit__26->SetBinContent(204,14);
   MainFit__26->SetBinContent(205,3);
   MainFit__26->SetBinContent(206,14);
   MainFit__26->SetBinContent(207,10);
   MainFit__26->SetBinContent(208,7);
   MainFit__26->SetBinContent(209,16);
   MainFit__26->SetBinContent(210,10);
   MainFit__26->SetBinContent(211,6);
   MainFit__26->SetBinContent(212,6);
   MainFit__26->SetBinContent(213,14);
   MainFit__26->SetBinContent(214,7);
   MainFit__26->SetBinContent(215,4);
   MainFit__26->SetBinContent(216,6);
   MainFit__26->SetBinContent(217,4);
   MainFit__26->SetBinContent(218,4);
   MainFit__26->SetBinContent(219,2);
   MainFit__26->SetBinContent(220,1);
   MainFit__26->SetBinContent(221,9);
   MainFit__26->SetBinContent(222,3);
   MainFit__26->SetBinContent(223,5);
   MainFit__26->SetBinContent(224,6);
   MainFit__26->SetBinContent(225,3);
   MainFit__26->SetBinContent(226,3);
   MainFit__26->SetBinContent(227,1);
   MainFit__26->SetBinContent(228,1);
   MainFit__26->SetBinContent(230,1);
   MainFit__26->SetBinContent(231,2);
   MainFit__26->SetBinContent(232,2);
   MainFit__26->SetBinContent(234,3);
   MainFit__26->SetBinContent(235,1);
   MainFit__26->SetBinContent(236,1);
   MainFit__26->SetBinContent(246,1);
   MainFit__26->SetMinimum(0);
   MainFit__26->SetMaximum(20);
   MainFit__26->SetEntries(420);
   MainFit__26->SetStats(0);
   MainFit__26->SetLineColor(4);
   MainFit__26->SetLineWidth(3);
   MainFit__26->GetXaxis()->SetTitle("Vertical decay position [mm]");
   MainFit__26->GetXaxis()->SetRange(101,300);
   MainFit__26->GetXaxis()->CenterTitle(true);
   MainFit__26->GetXaxis()->SetLabelFont(42);
   MainFit__26->GetXaxis()->SetLabelSize(0.035);
   MainFit__26->GetXaxis()->SetTitleOffset(1.1);
   MainFit__26->GetXaxis()->SetTitleFont(42);
   MainFit__26->GetYaxis()->SetTitle("Tracks");
   MainFit__26->GetYaxis()->CenterTitle(true);
   MainFit__26->GetYaxis()->SetNdivisions(4000510);
   MainFit__26->GetYaxis()->SetLabelFont(42);
   MainFit__26->GetYaxis()->SetLabelSize(0.035);
   MainFit__26->GetYaxis()->SetTitleOffset(1.1);
   MainFit__26->GetYaxis()->SetTitleFont(42);
   MainFit__26->GetZaxis()->SetLabelFont(42);
   MainFit__26->GetZaxis()->SetLabelSize(0.035);
   MainFit__26->GetZaxis()->SetTitleSize(0.035);
   MainFit__26->GetZaxis()->SetTitleFont(42);
   MainFit__26->Draw("");
   
   TH1F *FullSeqFit__27 = new TH1F("FullSeqFit__27","",400,-200,200);
   FullSeqFit__27->SetBinContent(156,1);
   FullSeqFit__27->SetBinContent(159,1);
   FullSeqFit__27->SetBinContent(160,1);
   FullSeqFit__27->SetBinContent(163,1);
   FullSeqFit__27->SetBinContent(164,3);
   FullSeqFit__27->SetBinContent(165,1);
   FullSeqFit__27->SetBinContent(168,1);
   FullSeqFit__27->SetBinContent(169,1);
   FullSeqFit__27->SetBinContent(170,2);
   FullSeqFit__27->SetBinContent(171,2);
   FullSeqFit__27->SetBinContent(172,2);
   FullSeqFit__27->SetBinContent(173,2);
   FullSeqFit__27->SetBinContent(174,4);
   FullSeqFit__27->SetBinContent(175,2);
   FullSeqFit__27->SetBinContent(176,8);
   FullSeqFit__27->SetBinContent(177,5);
   FullSeqFit__27->SetBinContent(178,9);
   FullSeqFit__27->SetBinContent(179,7);
   FullSeqFit__27->SetBinContent(180,5);
   FullSeqFit__27->SetBinContent(181,1);
   FullSeqFit__27->SetBinContent(182,12);
   FullSeqFit__27->SetBinContent(183,4);
   FullSeqFit__27->SetBinContent(184,8);
   FullSeqFit__27->SetBinContent(185,8);
   FullSeqFit__27->SetBinContent(186,9);
   FullSeqFit__27->SetBinContent(187,11);
   FullSeqFit__27->SetBinContent(188,7);
   FullSeqFit__27->SetBinContent(189,11);
   FullSeqFit__27->SetBinContent(190,10);
   FullSeqFit__27->SetBinContent(191,11);
   FullSeqFit__27->SetBinContent(192,14);
   FullSeqFit__27->SetBinContent(193,7);
   FullSeqFit__27->SetBinContent(194,13);
   FullSeqFit__27->SetBinContent(195,9);
   FullSeqFit__27->SetBinContent(196,8);
   FullSeqFit__27->SetBinContent(197,22);
   FullSeqFit__27->SetBinContent(198,13);
   FullSeqFit__27->SetBinContent(199,17);
   FullSeqFit__27->SetBinContent(200,16);
   FullSeqFit__27->SetBinContent(201,9);
   FullSeqFit__27->SetBinContent(202,13);
   FullSeqFit__27->SetBinContent(203,19);
   FullSeqFit__27->SetBinContent(204,19);
   FullSeqFit__27->SetBinContent(205,7);
   FullSeqFit__27->SetBinContent(206,19);
   FullSeqFit__27->SetBinContent(207,8);
   FullSeqFit__27->SetBinContent(208,8);
   FullSeqFit__27->SetBinContent(209,16);
   FullSeqFit__27->SetBinContent(210,10);
   FullSeqFit__27->SetBinContent(211,6);
   FullSeqFit__27->SetBinContent(212,9);
   FullSeqFit__27->SetBinContent(213,17);
   FullSeqFit__27->SetBinContent(214,8);
   FullSeqFit__27->SetBinContent(215,11);
   FullSeqFit__27->SetBinContent(216,7);
   FullSeqFit__27->SetBinContent(217,8);
   FullSeqFit__27->SetBinContent(218,6);
   FullSeqFit__27->SetBinContent(219,3);
   FullSeqFit__27->SetBinContent(220,3);
   FullSeqFit__27->SetBinContent(221,10);
   FullSeqFit__27->SetBinContent(222,7);
   FullSeqFit__27->SetBinContent(223,7);
   FullSeqFit__27->SetBinContent(224,6);
   FullSeqFit__27->SetBinContent(225,4);
   FullSeqFit__27->SetBinContent(226,3);
   FullSeqFit__27->SetBinContent(227,1);
   FullSeqFit__27->SetBinContent(228,3);
   FullSeqFit__27->SetBinContent(229,1);
   FullSeqFit__27->SetBinContent(230,2);
   FullSeqFit__27->SetBinContent(231,3);
   FullSeqFit__27->SetBinContent(232,1);
   FullSeqFit__27->SetBinContent(233,1);
   FullSeqFit__27->SetBinContent(234,1);
   FullSeqFit__27->SetBinContent(235,2);
   FullSeqFit__27->SetBinContent(239,4);
   FullSeqFit__27->SetBinContent(246,1);
   FullSeqFit__27->SetMinimum(0);
   FullSeqFit__27->SetMaximum(20);
   FullSeqFit__27->SetEntries(532);
   FullSeqFit__27->SetStats(0);
   FullSeqFit__27->SetLineColor(2);
   FullSeqFit__27->SetLineWidth(3);
   FullSeqFit__27->GetXaxis()->SetTitle("Vertical decay position [mm]");
   FullSeqFit__27->GetXaxis()->SetRange(101,300);
   FullSeqFit__27->GetXaxis()->CenterTitle(true);
   FullSeqFit__27->GetXaxis()->SetLabelFont(42);
   FullSeqFit__27->GetXaxis()->SetLabelSize(0.035);
   FullSeqFit__27->GetXaxis()->SetTitleOffset(1.1);
   FullSeqFit__27->GetXaxis()->SetTitleFont(42);
   FullSeqFit__27->GetYaxis()->SetTitle("Tracks");
   FullSeqFit__27->GetYaxis()->CenterTitle(true);
   FullSeqFit__27->GetYaxis()->SetNdivisions(4000510);
   FullSeqFit__27->GetYaxis()->SetLabelFont(42);
   FullSeqFit__27->GetYaxis()->SetLabelSize(0.035);
   FullSeqFit__27->GetYaxis()->SetTitleOffset(1.1);
   FullSeqFit__27->GetYaxis()->SetTitleFont(42);
   FullSeqFit__27->GetZaxis()->SetLabelFont(42);
   FullSeqFit__27->GetZaxis()->SetLabelSize(0.035);
   FullSeqFit__27->GetZaxis()->SetTitleSize(0.035);
   FullSeqFit__27->GetZaxis()->SetTitleFont(42);
   FullSeqFit__27->Draw("SAME");
   
   TH1F *TruthLR__28 = new TH1F("TruthLR__28","",400,-200,200);
   TruthLR__28->SetBinContent(156,1);
   TruthLR__28->SetBinContent(159,1);
   TruthLR__28->SetBinContent(160,1);
   TruthLR__28->SetBinContent(163,1);
   TruthLR__28->SetBinContent(164,2);
   TruthLR__28->SetBinContent(166,1);
   TruthLR__28->SetBinContent(168,2);
   TruthLR__28->SetBinContent(170,3);
   TruthLR__28->SetBinContent(171,2);
   TruthLR__28->SetBinContent(172,3);
   TruthLR__28->SetBinContent(173,3);
   TruthLR__28->SetBinContent(174,5);
   TruthLR__28->SetBinContent(175,2);
   TruthLR__28->SetBinContent(176,4);
   TruthLR__28->SetBinContent(177,6);
   TruthLR__28->SetBinContent(178,7);
   TruthLR__28->SetBinContent(179,6);
   TruthLR__28->SetBinContent(180,6);
   TruthLR__28->SetBinContent(181,3);
   TruthLR__28->SetBinContent(182,12);
   TruthLR__28->SetBinContent(183,6);
   TruthLR__28->SetBinContent(184,9);
   TruthLR__28->SetBinContent(185,10);
   TruthLR__28->SetBinContent(186,12);
   TruthLR__28->SetBinContent(187,6);
   TruthLR__28->SetBinContent(188,8);
   TruthLR__28->SetBinContent(189,11);
   TruthLR__28->SetBinContent(190,12);
   TruthLR__28->SetBinContent(191,11);
   TruthLR__28->SetBinContent(192,11);
   TruthLR__28->SetBinContent(193,13);
   TruthLR__28->SetBinContent(194,14);
   TruthLR__28->SetBinContent(195,13);
   TruthLR__28->SetBinContent(196,9);
   TruthLR__28->SetBinContent(197,21);
   TruthLR__28->SetBinContent(198,13);
   TruthLR__28->SetBinContent(199,11);
   TruthLR__28->SetBinContent(200,17);
   TruthLR__28->SetBinContent(201,13);
   TruthLR__28->SetBinContent(202,14);
   TruthLR__28->SetBinContent(203,20);
   TruthLR__28->SetBinContent(204,18);
   TruthLR__28->SetBinContent(205,11);
   TruthLR__28->SetBinContent(206,12);
   TruthLR__28->SetBinContent(207,13);
   TruthLR__28->SetBinContent(208,9);
   TruthLR__28->SetBinContent(209,15);
   TruthLR__28->SetBinContent(210,11);
   TruthLR__28->SetBinContent(211,8);
   TruthLR__28->SetBinContent(212,12);
   TruthLR__28->SetBinContent(213,15);
   TruthLR__28->SetBinContent(214,7);
   TruthLR__28->SetBinContent(215,10);
   TruthLR__28->SetBinContent(216,7);
   TruthLR__28->SetBinContent(217,7);
   TruthLR__28->SetBinContent(218,3);
   TruthLR__28->SetBinContent(219,4);
   TruthLR__28->SetBinContent(220,6);
   TruthLR__28->SetBinContent(221,11);
   TruthLR__28->SetBinContent(222,9);
   TruthLR__28->SetBinContent(223,8);
   TruthLR__28->SetBinContent(224,8);
   TruthLR__28->SetBinContent(225,2);
   TruthLR__28->SetBinContent(226,3);
   TruthLR__28->SetBinContent(227,2);
   TruthLR__28->SetBinContent(228,3);
   TruthLR__28->SetBinContent(229,1);
   TruthLR__28->SetBinContent(230,2);
   TruthLR__28->SetBinContent(231,2);
   TruthLR__28->SetBinContent(232,3);
   TruthLR__28->SetBinContent(234,2);
   TruthLR__28->SetBinContent(235,3);
   TruthLR__28->SetBinContent(236,1);
   TruthLR__28->SetBinContent(238,1);
   TruthLR__28->SetBinContent(239,3);
   TruthLR__28->SetMinimum(0);
   TruthLR__28->SetMaximum(20);
   TruthLR__28->SetEntries(557);
   TruthLR__28->SetStats(0);
   TruthLR__28->SetLineWidth(3);
   TruthLR__28->GetXaxis()->SetTitle("Vertical decay position [mm]");
   TruthLR__28->GetXaxis()->SetRange(101,300);
   TruthLR__28->GetXaxis()->CenterTitle(true);
   TruthLR__28->GetXaxis()->SetLabelFont(42);
   TruthLR__28->GetXaxis()->SetLabelSize(0.035);
   TruthLR__28->GetXaxis()->SetTitleOffset(1.1);
   TruthLR__28->GetXaxis()->SetTitleFont(42);
   TruthLR__28->GetYaxis()->SetTitle("Tracks");
   TruthLR__28->GetYaxis()->CenterTitle(true);
   TruthLR__28->GetYaxis()->SetNdivisions(4000510);
   TruthLR__28->GetYaxis()->SetLabelFont(42);
   TruthLR__28->GetYaxis()->SetLabelSize(0.035);
   TruthLR__28->GetYaxis()->SetTitleOffset(1.1);
   TruthLR__28->GetYaxis()->SetTitleFont(42);
   TruthLR__28->GetZaxis()->SetLabelFont(42);
   TruthLR__28->GetZaxis()->SetLabelSize(0.035);
   TruthLR__28->GetZaxis()->SetTitleSize(0.035);
   TruthLR__28->GetZaxis()->SetTitleFont(42);
   TruthLR__28->Draw("SAME");
   
   TLegend *leg = new TLegend(0,0,0,0,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("MainFit","#splitline{MainFit}{Mean = -0.77#pm0.7 ns}","lpf");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("FullSeqFit","#splitline{FullSeqFit}{Mean = -0.15#pm0.7 ns}","lpf");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("TruthLR","#splitline{TruthLR}{Mean = -0.012#pm0.6 ns}","lpf");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   leg->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
