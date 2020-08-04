void EffvsF()
{
//=========Macro generated from canvas: c/c
//=========  (Tue Aug  4 11:27:11 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(-0.103077,0.8823904,0.927693,1.658384);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1001[35] = {
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
   Double_t Graph0_fy1001[35] = {
   1.529052,
   1.250765,
   1.234964,
   1.227829,
   1.221713,
   1.217125,
   1.214577,
   1.211519,
   1.207951,
   1.205912,
   1.203364,
   1.179918,
   1.165138,
   1.154434,
   1.14526,
   1.139144,
   1.133028,
   1.124363,
   1.117737,
   1.11366,
   1.106014,
   1.099898,
   1.094292,
   1.091743,
   1.088175,
   1.084608,
   1.077982,
   1.074414,
   1.071356,
   1.068807,
   1.049949,
   1.038736,
   1.028033,
   1.022936,
   1.011723};
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
   
   TH1F *Graph_Graph1001 = new TH1F("Graph_Graph1001","",100,0,0.824616);
   Graph_Graph1001->SetMinimum(0.9599898);
   Graph_Graph1001->SetMaximum(1.580785);
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
   TLine *line = new TLine(0.6340932,0.9599898,0.6340932,1.580785);
   line->SetLineColor(2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
