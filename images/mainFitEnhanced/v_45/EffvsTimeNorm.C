void EffvsTimeNorm()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Aug  6 02:47:30 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(0.5742703,0.8823904,3.551329,1.658384);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1006[35] = {
   3.055153,
   1.427928,
   1.399042,
   1.366654,
   1.367559,
   1.345088,
   1.336694,
   1.319834,
   1.306242,
   1.299523,
   1.278394,
   1.333299,
   1.296364,
   1.285357,
   1.255778,
   1.243578,
   1.23367,
   1.227031,
   1.200262,
   1.197156,
   1.196481,
   1.197007,
   1.187986,
   1.179001,
   1.16065,
   1.163614,
   1.137311,
   1.147388,
   1.13391,
   1.126409,
   1.131841,
   1.114912,
   1.092538,
   1.084194,
   1.070447};
   Double_t Graph0_fy1006[35] = {
   1.529052,
   1.250765,
   1.234964,
   1.227829,
   1.221713,
   1.217125,
   1.214577,
   1.211519,
   1.207951,
   1.205912,
   1.203364,
   1.179918,
   1.165138,
   1.154434,
   1.14526,
   1.139144,
   1.133028,
   1.124363,
   1.117737,
   1.11366,
   1.106014,
   1.099898,
   1.094292,
   1.091743,
   1.088175,
   1.084608,
   1.077982,
   1.074414,
   1.071356,
   1.068807,
   1.049949,
   1.038736,
   1.028033,
   1.022936,
   1.011723};
   Double_t Graph0_fex1006[35] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph0_fey1006[35] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   TGraphErrors *gre = new TGraphErrors(35,Graph0_fx1006,Graph0_fy1006,Graph0_fex1006,Graph0_fey1006);
   gre->SetName("Graph0");
   gre->SetTitle(";CPU time / event (normalised to mainFit);Track efficiency");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1006 = new TH1F("Graph_Graph1006","",100,0.8719762,3.253623);
   Graph_Graph1006->SetMinimum(0.9599898);
   Graph_Graph1006->SetMaximum(1.580785);
   Graph_Graph1006->SetDirectory(0);
   Graph_Graph1006->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1006->SetLineColor(ci);
   Graph_Graph1006->GetXaxis()->SetTitle("CPU time / event (normalised to mainFit)");
   Graph_Graph1006->GetXaxis()->CenterTitle(true);
   Graph_Graph1006->GetXaxis()->SetLabelFont(42);
   Graph_Graph1006->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1006->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1006->GetXaxis()->SetTitleFont(42);
   Graph_Graph1006->GetYaxis()->SetTitle("Track efficiency");
   Graph_Graph1006->GetYaxis()->CenterTitle(true);
   Graph_Graph1006->GetYaxis()->SetNdivisions(4000510);
   Graph_Graph1006->GetYaxis()->SetLabelFont(42);
   Graph_Graph1006->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1006->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph1006->GetYaxis()->SetTitleFont(42);
   Graph_Graph1006->GetZaxis()->SetLabelFont(42);
   Graph_Graph1006->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1006->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1006->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1006);
   
   gre->Draw("ap");
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
