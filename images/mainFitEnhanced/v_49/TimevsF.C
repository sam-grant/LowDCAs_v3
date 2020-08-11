void TimevsF()
{
//=========Macro generated from canvas: c/c
//=========  (Tue Aug 11 06:49:37 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(-0.09283804,0.5977155,0.8355423,3.305486);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1002[35] = {
   0.676812,
   0.2066027,
   0.1923698,
   0.1838457,
   0.1753672,
   0.1696169,
   0.1661973,
   0.1631545,
   0.1586627,
   0.1536824,
   0.1524363,
   0.1351895,
   0.1237965,
   0.1181166,
   0.1108842,
   0.1039168,
   0.09991348,
   0.09726808,
   0.09081399,
   0.08827209,
   0.08442613,
   0.08058844,
   0.07839844,
   0.07525626,
   0.07077275,
   0.06818532,
   0.06444285,
   0.06229425,
   0.0608577,
   0.05630382,
   0.0470288,
   0.03825139,
   0.03267785,
   0.02599275,
   0.01788973};
   Double_t Graph0_fy1002[35] = {
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
   gre->SetTitle(";(t_{m+f} #minus t_{m})/t_{f};CPU time / event (normalised to mainFit)");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1002 = new TH1F("Graph_Graph1002","",100,0,0.7427043);
   Graph_Graph1002->SetMinimum(0.8684926);
   Graph_Graph1002->SetMaximum(3.034709);
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
   Graph_Graph1002->GetYaxis()->SetTitle("CPU time / event (normalised to mainFit)");
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
   TLine *line = new TLine(0.6349825,0.8684926,0.6349825,3.034709);
   line->SetLineColor(2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
