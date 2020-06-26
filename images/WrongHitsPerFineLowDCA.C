void WrongHitsPerFineLowDCA()
{
//=========Macro generated from canvas: c2/
//=========  (Fri Jun 19 09:28:01 2020) by ROOT version 6.12/04
   TCanvas *c2 = new TCanvas("c2", "",0,0,800,600);
   c2->SetHighLightColor(2);
   c2->Range(0,0,1,1);
   c2->SetFillColor(0);
   c2->SetBorderMode(0);
   c2->SetBorderSize(2);
   c2->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1001[7] = {
   1,
   2,
   3,
   4,
   5,
   6,
   7};
   Double_t Graph0_fy1001[7] = {
   730,
   193,
   43,
   1,
   0,
   0,
   1};
   Double_t Graph0_fex1001[7] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph0_fey1001[7] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   TGraphErrors *gre = new TGraphErrors(7,Graph0_fx1001,Graph0_fy1001,Graph0_fex1001,Graph0_fey1001);
   gre->SetName("Graph0");
   gre->SetTitle(";Wrong LR choices / track;Tracks");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1001 = new TH1F("Graph_Graph1001","",100,0.4,7.6);
   Graph_Graph1001->SetMinimum(0);
   Graph_Graph1001->SetMaximum(1000);
   Graph_Graph1001->SetDirectory(0);
   Graph_Graph1001->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1001->SetLineColor(ci);
   Graph_Graph1001->GetXaxis()->SetTitle("Wrong LR choices / track");
   Graph_Graph1001->GetXaxis()->SetBinLabel(9,"None wrong");
   Graph_Graph1001->GetXaxis()->SetBinLabel(23,"One wrong");
   Graph_Graph1001->GetXaxis()->SetBinLabel(37,"Two wrong");
   Graph_Graph1001->GetXaxis()->SetBinLabel(51,"Three wrong");
   Graph_Graph1001->GetXaxis()->SetBinLabel(64,"Four wrong");
   Graph_Graph1001->GetXaxis()->SetBinLabel(78,"Five wrong");
   Graph_Graph1001->GetXaxis()->SetBinLabel(92,"Five+ wrong");
   Graph_Graph1001->GetXaxis()->SetBit(TAxis::kLabelsHori);
   Graph_Graph1001->GetXaxis()->CenterTitle(true);
   Graph_Graph1001->GetXaxis()->SetLabelFont(42);
   Graph_Graph1001->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph1001->GetXaxis()->SetTitleFont(42);
   Graph_Graph1001->GetYaxis()->SetTitle("Tracks");
   Graph_Graph1001->GetYaxis()->CenterTitle(true);
   Graph_Graph1001->GetYaxis()->SetNdivisions(4000510);
   Graph_Graph1001->GetYaxis()->SetLabelFont(42);
   Graph_Graph1001->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph1001->GetYaxis()->SetTitleFont(42);
   Graph_Graph1001->GetZaxis()->SetLabelFont(42);
   Graph_Graph1001->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1001->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1001);
   
   gre->Draw("ap");
   
   Double_t Graph1_fx1002[7] = {
   1,
   2,
   3,
   4,
   5,
   6,
   7};
   Double_t Graph1_fy1002[7] = {
   751,
   158,
   32,
   1,
   0,
   0,
   0};
   Double_t Graph1_fex1002[7] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph1_fey1002[7] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   gre = new TGraphErrors(7,Graph1_fx1002,Graph1_fy1002,Graph1_fex1002,Graph1_fey1002);
   gre->SetName("Graph1");
   gre->SetTitle("Graph");
   gre->SetFillStyle(1000);
   gre->SetMarkerColor(2);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1002 = new TH1F("Graph_Graph1002","Graph",100,0.4,7.6);
   Graph_Graph1002->SetMinimum(0);
   Graph_Graph1002->SetMaximum(1000);
   Graph_Graph1002->SetDirectory(0);
   Graph_Graph1002->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1002->SetLineColor(ci);
   Graph_Graph1002->GetXaxis()->SetBinLabel(9,"None wrong");
   Graph_Graph1002->GetXaxis()->SetBinLabel(23,"One wrong");
   Graph_Graph1002->GetXaxis()->SetBinLabel(37,"Two wrong");
   Graph_Graph1002->GetXaxis()->SetBinLabel(51,"Three wrong");
   Graph_Graph1002->GetXaxis()->SetBinLabel(64,"Four wrong");
   Graph_Graph1002->GetXaxis()->SetBinLabel(78,"Five wrong");
   Graph_Graph1002->GetXaxis()->SetBinLabel(92,"Five+ wrong");
   Graph_Graph1002->GetXaxis()->SetBit(TAxis::kLabelsHori);
   Graph_Graph1002->GetXaxis()->SetLabelFont(42);
   Graph_Graph1002->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1002->GetXaxis()->SetTitleFont(42);
   Graph_Graph1002->GetYaxis()->SetLabelFont(42);
   Graph_Graph1002->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1002->GetYaxis()->SetTitleOffset(0);
   Graph_Graph1002->GetYaxis()->SetTitleFont(42);
   Graph_Graph1002->GetZaxis()->SetLabelFont(42);
   Graph_Graph1002->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1002->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1002);
   
   gre->Draw("p ");
   
   Double_t Graph2_fx1003[7] = {
   1,
   2,
   3,
   4,
   5,
   6,
   7};
   Double_t Graph2_fy1003[7] = {
   785,
   128,
   19,
   1,
   0,
   0,
   0};
   Double_t Graph2_fex1003[7] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph2_fey1003[7] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   gre = new TGraphErrors(7,Graph2_fx1003,Graph2_fy1003,Graph2_fex1003,Graph2_fey1003);
   gre->SetName("Graph2");
   gre->SetTitle("Graph");
   gre->SetFillStyle(1000);
   gre->SetMarkerColor(3);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1003 = new TH1F("Graph_Graph1003","Graph",100,0.4,7.6);
   Graph_Graph1003->SetMinimum(0);
   Graph_Graph1003->SetMaximum(1000);
   Graph_Graph1003->SetDirectory(0);
   Graph_Graph1003->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1003->SetLineColor(ci);
   Graph_Graph1003->GetXaxis()->SetBinLabel(9,"None wrong");
   Graph_Graph1003->GetXaxis()->SetBinLabel(23,"One wrong");
   Graph_Graph1003->GetXaxis()->SetBinLabel(37,"Two wrong");
   Graph_Graph1003->GetXaxis()->SetBinLabel(51,"Three wrong");
   Graph_Graph1003->GetXaxis()->SetBinLabel(64,"Four wrong");
   Graph_Graph1003->GetXaxis()->SetBinLabel(78,"Five wrong");
   Graph_Graph1003->GetXaxis()->SetBinLabel(92,"Five+ wrong");
   Graph_Graph1003->GetXaxis()->SetBit(TAxis::kLabelsHori);
   Graph_Graph1003->GetXaxis()->SetLabelFont(42);
   Graph_Graph1003->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1003->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1003->GetXaxis()->SetTitleFont(42);
   Graph_Graph1003->GetYaxis()->SetLabelFont(42);
   Graph_Graph1003->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1003->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1003->GetYaxis()->SetTitleOffset(0);
   Graph_Graph1003->GetYaxis()->SetTitleFont(42);
   Graph_Graph1003->GetZaxis()->SetLabelFont(42);
   Graph_Graph1003->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1003->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1003->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1003);
   
   gre->Draw("p ");
   
   Double_t Graph3_fx1004[7] = {
   1,
   2,
   3,
   4,
   5,
   6,
   7};
   Double_t Graph3_fy1004[7] = {
   841,
   105,
   6,
   0,
   0,
   0,
   0};
   Double_t Graph3_fex1004[7] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph3_fey1004[7] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   gre = new TGraphErrors(7,Graph3_fx1004,Graph3_fy1004,Graph3_fex1004,Graph3_fey1004);
   gre->SetName("Graph3");
   gre->SetTitle("Graph");
   gre->SetFillStyle(1000);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1004 = new TH1F("Graph_Graph1004","Graph",100,0.4,7.6);
   Graph_Graph1004->SetMinimum(0);
   Graph_Graph1004->SetMaximum(1000);
   Graph_Graph1004->SetDirectory(0);
   Graph_Graph1004->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1004->SetLineColor(ci);
   Graph_Graph1004->GetXaxis()->SetBinLabel(9,"None wrong");
   Graph_Graph1004->GetXaxis()->SetBinLabel(23,"One wrong");
   Graph_Graph1004->GetXaxis()->SetBinLabel(37,"Two wrong");
   Graph_Graph1004->GetXaxis()->SetBinLabel(51,"Three wrong");
   Graph_Graph1004->GetXaxis()->SetBinLabel(64,"Four wrong");
   Graph_Graph1004->GetXaxis()->SetBinLabel(78,"Five wrong");
   Graph_Graph1004->GetXaxis()->SetBinLabel(92,"Five+ wrong");
   Graph_Graph1004->GetXaxis()->SetBit(TAxis::kLabelsHori);
   Graph_Graph1004->GetXaxis()->SetLabelFont(42);
   Graph_Graph1004->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1004->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1004->GetXaxis()->SetTitleFont(42);
   Graph_Graph1004->GetYaxis()->SetLabelFont(42);
   Graph_Graph1004->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1004->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1004->GetYaxis()->SetTitleOffset(0);
   Graph_Graph1004->GetYaxis()->SetTitleFont(42);
   Graph_Graph1004->GetZaxis()->SetLabelFont(42);
   Graph_Graph1004->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1004->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1004->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1004);
   
   gre->Draw("p ");
   
   Double_t Graph4_fx1005[7] = {
   1,
   2,
   3,
   4,
   5,
   6,
   7};
   Double_t Graph4_fy1005[7] = {
   874,
   84,
   2,
   1,
   0,
   0,
   1};
   Double_t Graph4_fex1005[7] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph4_fey1005[7] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   gre = new TGraphErrors(7,Graph4_fx1005,Graph4_fy1005,Graph4_fex1005,Graph4_fey1005);
   gre->SetName("Graph4");
   gre->SetTitle("Graph");
   gre->SetFillStyle(1000);
   gre->SetMarkerColor(6);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1005 = new TH1F("Graph_Graph1005","Graph",100,0.4,7.6);
   Graph_Graph1005->SetMinimum(0);
   Graph_Graph1005->SetMaximum(1000);
   Graph_Graph1005->SetDirectory(0);
   Graph_Graph1005->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1005->SetLineColor(ci);
   Graph_Graph1005->GetXaxis()->SetBinLabel(9,"None wrong");
   Graph_Graph1005->GetXaxis()->SetBinLabel(23,"One wrong");
   Graph_Graph1005->GetXaxis()->SetBinLabel(37,"Two wrong");
   Graph_Graph1005->GetXaxis()->SetBinLabel(51,"Three wrong");
   Graph_Graph1005->GetXaxis()->SetBinLabel(64,"Four wrong");
   Graph_Graph1005->GetXaxis()->SetBinLabel(78,"Five wrong");
   Graph_Graph1005->GetXaxis()->SetBinLabel(92,"Five+ wrong");
   Graph_Graph1005->GetXaxis()->SetBit(TAxis::kLabelsHori);
   Graph_Graph1005->GetXaxis()->SetLabelFont(42);
   Graph_Graph1005->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1005->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1005->GetXaxis()->SetTitleFont(42);
   Graph_Graph1005->GetYaxis()->SetLabelFont(42);
   Graph_Graph1005->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1005->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1005->GetYaxis()->SetTitleOffset(0);
   Graph_Graph1005->GetYaxis()->SetTitleFont(42);
   Graph_Graph1005->GetZaxis()->SetLabelFont(42);
   Graph_Graph1005->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1005->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1005->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1005);
   
   gre->Draw("p ");
   
   TLegend *leg = new TLegend(0,0,0,0,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("NULL","#bf{Low DCA thresholds}","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph0","0 mm","lpf");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("Graph1","100 #mum","lpf");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("Graph2","200 #mum","lpf");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("Graph3","300 #mum","lpf");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("Graph4","400 #mum","lpf");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   leg->Draw();
   c2->Modified();
   c2->cd();
   c2->SetSelected(c2);
}
