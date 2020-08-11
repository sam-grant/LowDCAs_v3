void EffvsTime()
{
//=========Macro generated from canvas: c/c
//=========  (Mon Aug 10 19:37:41 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(4.683212,0.8652021,23.9516,1.770524);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1005[35] = {
   20.7402,
   11.4155,
   11.1607,
   11.0293,
   10.9219,
   10.8073,
   10.7371,
   10.6498,
   10.5964,
   10.5531,
   10.5049,
   10.159,
   9.97268,
   9.82068,
   9.71427,
   9.60603,
   9.50612,
   9.41228,
   9.33302,
   9.25323,
   9.19895,
   9.1317,
   9.04378,
   8.99708,
   8.94089,
   8.86722,
   8.82325,
   8.78853,
   8.72384,
   8.67444,
   8.47661,
   8.30552,
   8.14428,
   8.0243,
   7.89461};
   Double_t Graph0_fy1005[35] = {
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
   
   TH1F *Graph_Graph1005 = new TH1F("Graph_Graph1005","",100,6.610051,22.02476);
   Graph_Graph1005->SetMinimum(0.9557343);
   Graph_Graph1005->SetMaximum(1.679992);
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
   TLine *line = new TLine(19.8845,0.9557343,19.8845,1.679992);
   line->SetLineColor(2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   line = new TLine(6.610051,1.583333,22.02476,1.583333);
   line->SetLineColor(2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
