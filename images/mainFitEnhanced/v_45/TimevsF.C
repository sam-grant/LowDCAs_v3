void TimevsF()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Aug  6 02:47:30 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(-0.103077,3.674112,0.927693,22.72098);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1002[35] = {
   0.7519943,
   0.1565816,
   0.146012,
   0.1341613,
   0.1344924,
   0.1262699,
   0.1231987,
   0.1170295,
   0.112056,
   0.1095974,
   0.1018662,
   0.1219565,
   0.1084415,
   0.1044141,
   0.09359108,
   0.08912668,
   0.08550129,
   0.08307235,
   0.07327709,
   0.07214069,
   0.07189362,
   0.07208636,
   0.06878524,
   0.06549786,
   0.05878296,
   0.05986731,
   0.05024307,
   0.05393023,
   0.04899857,
   0.04625393,
   0.04824135,
   0.0420469,
   0.03386045,
   0.03080698,
   0.02577695};
   Double_t Graph0_fy1002[35] = {
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
   
   TH1F *Graph_Graph1002 = new TH1F("Graph_Graph1002","",100,0,0.824616);
   Graph_Graph1002->SetMinimum(5.578799);
   Graph_Graph1002->SetMaximum(20.81629);
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
   TLine *line = new TLine(0.6340932,5.578799,0.6340932,20.81629);
   line->SetLineColor(2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
