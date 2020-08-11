void EffvsF()
{
//=========Macro generated from canvas: c/c
//=========  (Tue Aug 11 06:49:37 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(-0.09283804,0.8654084,0.8355423,1.769493);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1001[35] = {
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
   Double_t Graph0_fy1001[35] = {
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
   
   TH1F *Graph_Graph1001 = new TH1F("Graph_Graph1001","",100,0,0.7427043);
   Graph_Graph1001->SetMinimum(0.9558168);
   Graph_Graph1001->SetMaximum(1.679084);
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
   TLine *line = new TLine(0.6349825,0.9558168,0.6349825,1.679084);
   line->SetLineColor(2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
