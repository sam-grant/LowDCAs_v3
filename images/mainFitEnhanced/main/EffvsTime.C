void EffvsTime()
{
//=========Macro generated from canvas: c/c
//=========  (Tue Aug  4 11:27:11 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(0.8823904,3.674112,1.658384,22.72098);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1005[35] = {
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
   Double_t Graph0_fy1005[35] = {
   19.5465,
   9.13571,
   8.9509,
   8.74369,
   8.74948,
   8.60571,
   8.55201,
   8.44414,
   8.35718,
   8.31419,
   8.17901,
   8.53029,
   8.29398,
   8.22356,
   8.03432,
   7.95626,
   7.89287,
   7.8504,
   7.67913,
   7.65926,
   7.65494,
   7.65831,
   7.60059,
   7.54311,
   7.4257,
   7.44466,
   7.27638,
   7.34085,
   7.25462,
   7.20663,
   7.24138,
   7.13307,
   6.98993,
   6.93654,
   6.84859};
   Double_t Graph0_fex1005[35] = {
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
   Double_t Graph0_fey1005[35] = {
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
   TGraphErrors *gre = new TGraphErrors(35,Graph0_fx1005,Graph0_fy1005,Graph0_fex1005,Graph0_fey1005);
   gre->SetName("Graph0");
   gre->SetTitle(";CPU time / event;Track efficiency");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1005 = new TH1F("Graph_Graph1005","",100,0.9599898,1.580785);
   Graph_Graph1005->SetMinimum(5.578799);
   Graph_Graph1005->SetMaximum(20.81629);
   Graph_Graph1005->SetDirectory(0);
   Graph_Graph1005->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1005->SetLineColor(ci);
   Graph_Graph1005->GetXaxis()->SetTitle("CPU time / event");
   Graph_Graph1005->GetXaxis()->CenterTitle(true);
   Graph_Graph1005->GetXaxis()->SetLabelFont(42);
   Graph_Graph1005->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1005->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1005->GetXaxis()->SetTitleFont(42);
   Graph_Graph1005->GetYaxis()->SetTitle("Track efficiency");
   Graph_Graph1005->GetYaxis()->CenterTitle(true);
   Graph_Graph1005->GetYaxis()->SetNdivisions(4000510);
   Graph_Graph1005->GetYaxis()->SetLabelFont(42);
   Graph_Graph1005->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1005->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph1005->GetYaxis()->SetTitleFont(42);
   Graph_Graph1005->GetZaxis()->SetLabelFont(42);
   Graph_Graph1005->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1005->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1005->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1005);
   
   gre->Draw("ap");
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
