void radialPosMeans()
{
//=========Macro generated from canvas: c/c
//=========  (Mon Jun 29 16:45:27 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(0.25,3.338347,4.75,6.676811);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1002[4] = {
   1,
   2,
   3,
   4};
   Double_t Graph0_fy1002[4] = {
   4.879367,
   4.791121,
   5.317234,
   4.791121};
   Double_t Graph0_fex1002[4] = {
   0,
   0,
   0,
   0};
   Double_t Graph0_fey1002[4] = {
   0.7536954,
   0.896363,
   0.8031658,
   0.896363};
   TGraphErrors *gre = new TGraphErrors(4,Graph0_fx1002,Graph0_fy1002,Graph0_fex1002,Graph0_fey1002);
   gre->SetName("Graph0");
   gre->SetTitle(";Fit mode;Radial decay position mean [mm]");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1002 = new TH1F("Graph_Graph1002","",100,0.7,4.3);
   Graph_Graph1002->SetMinimum(3.672194);
   Graph_Graph1002->SetMaximum(6.342964);
   Graph_Graph1002->SetDirectory(0);
   Graph_Graph1002->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1002->SetLineColor(ci);
   Graph_Graph1002->GetXaxis()->SetTitle("Fit mode");
   Graph_Graph1002->GetXaxis()->SetBinLabel(9,"Truth LR");
   Graph_Graph1002->GetXaxis()->SetBinLabel(37,"Main");
   Graph_Graph1002->GetXaxis()->SetBinLabel(64,"Full sequence");
   Graph_Graph1002->GetXaxis()->SetBinLabel(92,"LR flip");
   Graph_Graph1002->GetXaxis()->SetBit(TAxis::kLabelsHori);
   Graph_Graph1002->GetXaxis()->CenterTitle(true);
   Graph_Graph1002->GetXaxis()->SetLabelFont(42);
   Graph_Graph1002->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1002->GetXaxis()->SetTitleFont(42);
   Graph_Graph1002->GetYaxis()->SetTitle("Radial decay position mean [mm]");
   Graph_Graph1002->GetYaxis()->CenterTitle(true);
   Graph_Graph1002->GetYaxis()->SetNdivisions(4000510);
   Graph_Graph1002->GetYaxis()->SetLabelFont(42);
   Graph_Graph1002->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph1002->GetYaxis()->SetTitleFont(42);
   Graph_Graph1002->GetZaxis()->SetLabelFont(42);
   Graph_Graph1002->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1002->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1002);
   
   gre->Draw("ap");
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
