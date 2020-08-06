void TimevsF()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Aug  6 01:58:15 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(-0.09450954,4.683212,0.8505858,23.9516);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1002[35] = {
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
   Double_t Graph0_fy1002[35] = {
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
   Double_t Graph0_fex1002[35] = {
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
   Double_t Graph0_fey1002[35] = {
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
   TGraphErrors *gre = new TGraphErrors(35,Graph0_fx1002,Graph0_fy1002,Graph0_fex1002,Graph0_fey1002);
   gre->SetName("Graph0");
   gre->SetTitle(";(t_{m+f} #minus t_{m})/t_{f};CPU time / event");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1002 = new TH1F("Graph_Graph1002","",100,0,0.7560763);
   Graph_Graph1002->SetMinimum(6.610051);
   Graph_Graph1002->SetMaximum(22.02476);
   Graph_Graph1002->SetDirectory(0);
   Graph_Graph1002->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1002->SetLineColor(ci);
   Graph_Graph1002->GetXaxis()->SetTitle("(t_{m+f} #minus t_{m})/t_{f}");
   Graph_Graph1002->GetXaxis()->CenterTitle(true);
   Graph_Graph1002->GetXaxis()->SetLabelFont(42);
   Graph_Graph1002->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1002->GetXaxis()->SetTitleFont(42);
   Graph_Graph1002->GetYaxis()->SetTitle("CPU time / event");
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
   TLine *line = new TLine(0.6484418,6.610051,0.6484418,22.02476);
   line->SetLineColor(2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
