void tracksPerSecondNorm()
{
//=========Macro generated from canvas: c/c
//=========  (Mon Aug  3 22:36:41 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(-0.00275,0.3883881,0.02475,1.060957);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1005[21] = {
   0,
   0.001,
   0.002,
   0.003,
   0.004,
   0.005,
   0.006,
   0.007,
   0.008,
   0.009,
   0.01,
   0.011,
   0.012,
   0.013,
   0.014,
   0.015,
   0.016,
   0.017,
   0.018,
   0.019,
   0.02};
   Double_t Graph0_fy1005[21] = {
   0.500483,
   0.8616786,
   0.8849613,
   0.8987736,
   0.8981429,
   0.911992,
   0.9160215,
   0.9184206,
   0.9163277,
   0.9312445,
   0.9302544,
   0.9243896,
   0.9188732,
   0.9211319,
   0.9259896,
   0.9375568,
   0.9321029,
   0.9478336,
   0.9363999,
   0.9448332,
   0.9488625};
   Double_t Graph0_fex1005[21] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
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
   Double_t Graph0_fey1005[21] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
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
   TGraphErrors *gre = new TGraphErrors(21,Graph0_fx1005,Graph0_fy1005,Graph0_fex1005,Graph0_fey1005);
   gre->SetName("Graph0");
   gre->SetTitle(";p-value low cut;Tracks per second (normalised to mainFit) [s^{-1}]");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1005 = new TH1F("Graph_Graph1005","",100,0,0.022);
   Graph_Graph1005->SetMinimum(0.4556451);
   Graph_Graph1005->SetMaximum(0.9937005);
   Graph_Graph1005->SetDirectory(0);
   Graph_Graph1005->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1005->SetLineColor(ci);
   Graph_Graph1005->GetXaxis()->SetTitle("p-value low cut");
   Graph_Graph1005->GetXaxis()->CenterTitle(true);
   Graph_Graph1005->GetXaxis()->SetLabelFont(42);
   Graph_Graph1005->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1005->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1005->GetXaxis()->SetTitleFont(42);
   Graph_Graph1005->GetYaxis()->SetTitle("Tracks per second (normalised to mainFit) [s^{-1}]");
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
