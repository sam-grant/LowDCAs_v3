void verticalPosMeans()
{
//=========Macro generated from canvas: c/c
//=========  (Tue Jun 30 09:40:25 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(0.25,-2.632268,4.75,0.3050915);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1003[4] = {
   1,
   2,
   3,
   4};
   Double_t Graph0_fy1003[4] = {
   -1.450101,
   -1.078968,
   -0.9254214,
   -1.078968};
   Double_t Graph0_fex1003[4] = {
   0,
   0,
   0,
   0};
   Double_t Graph0_fey1003[4] = {
   0.6926076,
   0.7972703,
   0.7409529,
   0.7972703};
   TGraphErrors *gre = new TGraphErrors(4,Graph0_fx1003,Graph0_fy1003,Graph0_fex1003,Graph0_fey1003);
   gre->SetName("Graph0");
   gre->SetTitle(";Fit mode;Vertical decay position mean [mm]");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1003 = new TH1F("Graph_Graph1003","",100,0.7,4.3);
   Graph_Graph1003->SetMinimum(-2.338532);
   Graph_Graph1003->SetMaximum(0.01135549);
   Graph_Graph1003->SetDirectory(0);
   Graph_Graph1003->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1003->SetLineColor(ci);
   Graph_Graph1003->GetXaxis()->SetTitle("Fit mode");
   Graph_Graph1003->GetXaxis()->SetBinLabel(9,"Truth LR");
   Graph_Graph1003->GetXaxis()->SetBinLabel(37,"Main");
   Graph_Graph1003->GetXaxis()->SetBinLabel(64,"Full sequence");
   Graph_Graph1003->GetXaxis()->SetBinLabel(92,"LR flip");
   Graph_Graph1003->GetXaxis()->SetBit(TAxis::kLabelsHori);
   Graph_Graph1003->GetXaxis()->CenterTitle(true);
   Graph_Graph1003->GetXaxis()->SetLabelFont(42);
   Graph_Graph1003->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1003->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1003->GetXaxis()->SetTitleFont(42);
   Graph_Graph1003->GetYaxis()->SetTitle("Vertical decay position mean [mm]");
   Graph_Graph1003->GetYaxis()->CenterTitle(true);
   Graph_Graph1003->GetYaxis()->SetNdivisions(4000510);
   Graph_Graph1003->GetYaxis()->SetLabelFont(42);
   Graph_Graph1003->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1003->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph1003->GetYaxis()->SetTitleFont(42);
   Graph_Graph1003->GetZaxis()->SetLabelFont(42);
   Graph_Graph1003->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1003->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1003->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1003);
   
   gre->Draw("ap");
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
