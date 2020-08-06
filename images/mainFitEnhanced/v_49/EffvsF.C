void EffvsF()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Aug  6 01:58:15 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(-0.09450954,0.8652021,0.8505858,1.770524);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1001[35] = {
   0.6914753,
   0.2225321,
   0.2097181,
   0.20311,
   0.1977088,
   0.1919455,
   0.1884151,
   0.1840247,
   0.1813392,
   0.1791617,
   0.1767377,
   0.1593422,
   0.1499721,
   0.1423279,
   0.1369765,
   0.1315331,
   0.1265086,
   0.1217893,
   0.1178033,
   0.1137906,
   0.1110609,
   0.1076788,
   0.1032573,
   0.1009087,
   0.09808293,
   0.09437803,
   0.09216676,
   0.09042068,
   0.08716739,
   0.08468304,
   0.07473409,
   0.0661299,
   0.05802107,
   0.05198723,
   0.04546506};
   Double_t Graph0_fy1001[35] = {
   1.619637,
   1.306931,
   1.292492,
   1.283003,
   1.278465,
   1.27434,
   1.27104,
   1.265264,
   1.259488,
   1.255363,
   1.253713,
   1.230198,
   1.213696,
   1.200083,
   1.192244,
   1.183168,
   1.172442,
   1.164604,
   1.155528,
   1.148927,
   1.140677,
   1.132426,
   1.1283,
   1.122937,
   1.117987,
   1.111799,
   1.106023,
   1.10231,
   1.099422,
   1.096947,
   1.076733,
   1.061469,
   1.044967,
   1.028878,
   1.016089};
   Double_t Graph0_fex1001[35] = {
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
   Double_t Graph0_fey1001[35] = {
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
   TGraphErrors *gre = new TGraphErrors(35,Graph0_fx1001,Graph0_fy1001,Graph0_fex1001,Graph0_fey1001);
   gre->SetName("Graph0");
   gre->SetTitle(";(t_{m+f} #minus t_{m})/t_{f};Track efficiency");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1001 = new TH1F("Graph_Graph1001","",100,0,0.7560763);
   Graph_Graph1001->SetMinimum(0.9557343);
   Graph_Graph1001->SetMaximum(1.679992);
   Graph_Graph1001->SetDirectory(0);
   Graph_Graph1001->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1001->SetLineColor(ci);
   Graph_Graph1001->GetXaxis()->SetTitle("(t_{m+f} #minus t_{m})/t_{f}");
   Graph_Graph1001->GetXaxis()->CenterTitle(true);
   Graph_Graph1001->GetXaxis()->SetLabelFont(42);
   Graph_Graph1001->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1001->GetXaxis()->SetTitleFont(42);
   Graph_Graph1001->GetYaxis()->SetTitle("Track efficiency");
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
   TLine *line = new TLine(0.6484418,0.9557343,0.6484418,1.679992);
   line->SetLineColor(2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
