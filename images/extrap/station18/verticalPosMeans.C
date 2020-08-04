void verticalPosMeans()
{
//=========Macro generated from canvas: c/c
//=========  (Tue Jun 30 09:40:25 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(0.25,-2.02957,4.75,1.141206);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1004[4] = {
   1,
   2,
   3,
   4};
   Double_t Graph0_fy1004[4] = {
   -0.03299838,
   -0.7725489,
   -0.1646205,
   -0.7725489};
   Double_t Graph0_fex1004[4] = {
   0,
   0,
   0,
   0};
   Double_t Graph0_fey1004[4] = {
   0.6457413,
   0.7285589,
   0.661515,
   0.7285589};
   TGraphErrors *gre = new TGraphErrors(4,Graph0_fx1004,Graph0_fy1004,Graph0_fex1004,Graph0_fey1004);
   gre->SetName("Graph0");
   gre->SetTitle(";Fit mode;Vertical decay position mean [mm]");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1004 = new TH1F("Graph_Graph1004","",100,0.7,4.3);
   Graph_Graph1004->SetMinimum(-1.712493);
   Graph_Graph1004->SetMaximum(0.824128);
   Graph_Graph1004->SetDirectory(0);
   Graph_Graph1004->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1004->SetLineColor(ci);
   Graph_Graph1004->GetXaxis()->SetTitle("Fit mode");
   Graph_Graph1004->GetXaxis()->SetBinLabel(9,"Truth LR");
   Graph_Graph1004->GetXaxis()->SetBinLabel(37,"Main");
   Graph_Graph1004->GetXaxis()->SetBinLabel(64,"Full sequence");
   Graph_Graph1004->GetXaxis()->SetBinLabel(92,"LR flip");
   Graph_Graph1004->GetXaxis()->SetBit(TAxis::kLabelsHori);
   Graph_Graph1004->GetXaxis()->CenterTitle(true);
   Graph_Graph1004->GetXaxis()->SetLabelFont(42);
   Graph_Graph1004->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1004->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1004->GetXaxis()->SetTitleFont(42);
   Graph_Graph1004->GetYaxis()->SetTitle("Vertical decay position mean [mm]");
   Graph_Graph1004->GetYaxis()->CenterTitle(true);
   Graph_Graph1004->GetYaxis()->SetNdivisions(4000510);
   Graph_Graph1004->GetYaxis()->SetLabelFont(42);
   Graph_Graph1004->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1004->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph1004->GetYaxis()->SetTitleFont(42);
   Graph_Graph1004->GetZaxis()->SetLabelFont(42);
   Graph_Graph1004->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1004->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1004->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1004);
   
   gre->Draw("ap");
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
