void lowDCARecoScan_noQ()
{
//=========Macro generated from canvas: c/
//=========  (Wed May 20 08:45:29 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "",201,1103,800,600);
   c->SetHighLightColor(2);
   c->Range(-0.06875001,14222,0.61875,14384);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1002[21] = {
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
   Double_t Graph0_fy1002[21] = {
   14316,
   14249,
   14272,
   14257,
   14278,
   14290,
   14295,
   14291,
   14300,
   14300,
   14328,
   14309,
   14312,
   14328,
   14324,
   14339,
   14357,
   14355,
   14327,
   14329,
   14327};
   Double_t Graph0_fex1002[21] = {
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
   Double_t Graph0_fey1002[21] = {
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
   TGraphErrors *gre = new TGraphErrors(21,Graph0_fx1002,Graph0_fy1002,Graph0_fex1002,Graph0_fey1002);
   gre->SetName("Graph0");
   gre->SetTitle(";Lock low DCA threshold [#mum];Fitted tracks");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1002 = new TH1F("Graph_Graph1002","",100,0,0.55);
   Graph_Graph1002->SetMinimum(14238.2);
   Graph_Graph1002->SetMaximum(14367.8);
   Graph_Graph1002->SetDirectory(0);
   Graph_Graph1002->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1002->SetLineColor(ci);
   Graph_Graph1002->GetXaxis()->SetTitle("Lock low DCA threshold [#mum]");
   Graph_Graph1002->GetXaxis()->CenterTitle(true);
   Graph_Graph1002->GetXaxis()->SetLabelFont(42);
   Graph_Graph1002->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1002->GetXaxis()->SetTitleFont(42);
   Graph_Graph1002->GetYaxis()->SetTitle("Fitted tracks");
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
