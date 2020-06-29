void lowDCARecoScan_Q()
{
//=========Macro generated from canvas: c/
//=========  (Wed May 20 08:45:27 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "",201,1103,800,600);
   c->SetHighLightColor(2);
   c->Range(-0.06875001,2169,0.61875,2661);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1001[21] = {
   0,
   0.025,
   0.05,
   0.075,
   0.1,
   0.125,
   0.15,
   0.175,
   0.2,
   0.225,
   0.25,
   0.275,
   0.3,
   0.325,
   0.35,
   0.375,
   0.4,
   0.425,
   0.45,
   0.475,
   0.5};
   Double_t Graph0_fy1001[21] = {
   2579,
   2460,
   2475,
   2480,
   2479,
   2468,
   2470,
   2453,
   2444,
   2440,
   2438,
   2440,
   2448,
   2466,
   2458,
   2477,
   2470,
   2435,
   2404,
   2322,
   2251};
   Double_t Graph0_fex1001[21] = {
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
   Double_t Graph0_fey1001[21] = {
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
   TGraphErrors *gre = new TGraphErrors(21,Graph0_fx1001,Graph0_fy1001,Graph0_fex1001,Graph0_fey1001);
   gre->SetName("Graph0");
   gre->SetTitle(";Lock low DCA threshold [#mum];Tracks passing quality cuts");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1001 = new TH1F("Graph_Graph1001","",100,0,0.55);
   Graph_Graph1001->SetMinimum(2218.2);
   Graph_Graph1001->SetMaximum(2611.8);
   Graph_Graph1001->SetDirectory(0);
   Graph_Graph1001->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1001->SetLineColor(ci);
   Graph_Graph1001->GetXaxis()->SetTitle("Lock low DCA threshold [#mum]");
   Graph_Graph1001->GetXaxis()->CenterTitle(true);
   Graph_Graph1001->GetXaxis()->SetLabelFont(42);
   Graph_Graph1001->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1001->GetXaxis()->SetTitleFont(42);
   Graph_Graph1001->GetYaxis()->SetTitle("Tracks passing quality cuts");
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
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
