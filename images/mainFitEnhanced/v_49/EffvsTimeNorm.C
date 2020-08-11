void EffvsTimeNorm()
{
//=========Macro generated from canvas: c/c
//=========  (Tue Aug 11 06:49:37 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(0.5977155,0.8654084,3.305486,1.769493);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1005[35] = {
   2.854191,
   1.566008,
   1.527015,
   1.503663,
   1.480435,
   1.464682,
   1.455313,
   1.446977,
   1.434672,
   1.421028,
   1.417614,
   1.370365,
   1.339152,
   1.323592,
   1.303778,
   1.28469,
   1.273722,
   1.266475,
   1.248794,
   1.24183,
   1.231293,
   1.22078,
   1.21478,
   1.206172,
   1.193889,
   1.1868,
   1.176547,
   1.170661,
   1.166725,
   1.15425,
   1.12884,
   1.104793,
   1.089524,
   1.07121,
   1.049011};
   Double_t Graph0_fy1005[35] = {
   1.618812,
   1.306518,
   1.292079,
   1.282591,
   1.278053,
   1.273927,
   1.270627,
   1.264851,
   1.259076,
   1.25495,
   1.2533,
   1.229785,
   1.213284,
   1.19967,
   1.191832,
   1.182756,
   1.17203,
   1.164191,
   1.155116,
   1.148515,
   1.140264,
   1.132013,
   1.127888,
   1.122525,
   1.117574,
   1.111386,
   1.105611,
   1.101898,
   1.09901,
   1.096535,
   1.07632,
   1.061056,
   1.044554,
   1.028465,
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
   gre->SetTitle(";CPU time / event (normalised to mainFit);Track efficiency");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1005 = new TH1F("Graph_Graph1005","",100,0.8684926,3.034709);
   Graph_Graph1005->SetMinimum(0.9558168);
   Graph_Graph1005->SetMaximum(1.679084);
   Graph_Graph1005->SetDirectory(0);
   Graph_Graph1005->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1005->SetLineColor(ci);
   Graph_Graph1005->GetXaxis()->SetTitle("CPU time / event (normalised to mainFit)");
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
   TLine *line = new TLine(2.739595,0.9558168,2.739595,1.679084);
   line->SetLineColor(2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   line = new TLine(0.8684926,1.582096,3.034709,1.582096);
   line->SetLineColor(2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
