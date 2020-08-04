void FvsFSQCalls()
{
//=========Macro generated from canvas: c/c
//=========  (Mon Aug  3 22:36:42 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   gStyle->SetOptFit(1);
   c->SetHighLightColor(2);
   c->Range(-0.102821,-5.000002,0.9253894,223);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1007[21] = {
   0.7519943,
   0.1450947,
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
   0.04625393};
   Double_t Graph0_fy1007[21] = {
   185,
   52,
   48,
   45,
   44,
   42,
   41,
   41,
   40,
   39,
   38,
   38,
   37,
   36,
   36,
   35,
   35,
   34,
   34,
   34,
   33};
   Double_t Graph0_fex1007[21] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
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
   Double_t Graph0_fey1007[21] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
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
   TGraphErrors *gre = new TGraphErrors(21,Graph0_fx1007,Graph0_fy1007,Graph0_fex1007,Graph0_fey1007);
   gre->SetName("Graph0");
   gre->SetTitle(";(t_{m+f} #minus t_{m})/t_{f} / event;Times FSQ is called / event");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1007 = new TH1F("Graph_Graph1007","",100,0,0.8225683);
   Graph_Graph1007->SetMinimum(17.8);
   Graph_Graph1007->SetMaximum(200.2);
   Graph_Graph1007->SetDirectory(0);
   Graph_Graph1007->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1007->SetLineColor(ci);
   Graph_Graph1007->GetXaxis()->SetTitle("(t_{m+f} #minus t_{m})/t_{f} / event");
   Graph_Graph1007->GetXaxis()->CenterTitle(true);
   Graph_Graph1007->GetXaxis()->SetLabelFont(42);
   Graph_Graph1007->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1007->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1007->GetXaxis()->SetTitleFont(42);
   Graph_Graph1007->GetYaxis()->SetTitle("Times FSQ is called / event");
   Graph_Graph1007->GetYaxis()->CenterTitle(true);
   Graph_Graph1007->GetYaxis()->SetNdivisions(4000510);
   Graph_Graph1007->GetYaxis()->SetLabelFont(42);
   Graph_Graph1007->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1007->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph1007->GetYaxis()->SetTitleFont(42);
   Graph_Graph1007->GetZaxis()->SetLabelFont(42);
   Graph_Graph1007->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1007->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1007->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1007);
   
   
   TF1 *lineFit11008 = new TF1("lineFit1","pol1",0,0.8225683, TF1::EAddToList::kNo);
   lineFit11008->SetFillColor(19);
   lineFit11008->SetFillStyle(0);
   lineFit11008->SetLineWidth(3);
   lineFit11008->SetChisquare(10.15348);
   lineFit11008->SetNDF(19);
   lineFit11008->GetXaxis()->SetLabelFont(42);
   lineFit11008->GetXaxis()->SetLabelSize(0.035);
   lineFit11008->GetXaxis()->SetTitleSize(0.035);
   lineFit11008->GetXaxis()->SetTitleFont(42);
   lineFit11008->GetYaxis()->SetLabelFont(42);
   lineFit11008->GetYaxis()->SetLabelSize(0.035);
   lineFit11008->GetYaxis()->SetTitleSize(0.035);
   lineFit11008->GetYaxis()->SetTitleOffset(0);
   lineFit11008->GetYaxis()->SetTitleFont(42);
   lineFit11008->SetParameter(0,22.12412);
   lineFit11008->SetParError(0,0.2004518);
   lineFit11008->SetParLimits(0,0,0);
   lineFit11008->SetParameter(1,216.088);
   lineFit11008->SetParError(1,1.096378);
   lineFit11008->SetParLimits(1,0,0);
   lineFit11008->SetParent(gre);
   gre->GetListOfFunctions()->Add(lineFit11008);
   
   TPaveStats *ptstats = new TPaveStats(0.11,0.69,0.49,0.89,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(0);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *ptstats_LaTex = ptstats->AddText("#chi^{2} / ndf = 10.15 / 19");
   ptstats_LaTex = ptstats->AddText("p0       = 22.12 #pm 0.2005 ");
   ptstats_LaTex = ptstats->AddText("p1       = 216.1 #pm 1.096 ");
   ptstats->SetOptStat(0);
   ptstats->SetOptFit(111);
   ptstats->Draw();
   gre->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(gre->GetListOfFunctions());
   gre->Draw("ap");
   TLine *line = new TLine(0.6340932,17.8,0.6340932,200.2);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
