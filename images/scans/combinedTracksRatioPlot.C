void combinedTracksRatioPlot()
{
//=========Macro generated from canvas: c/c
//=========  (Mon Jun 29 20:06:17 2020) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "c",0,0,800,800);
   c->SetHighLightColor(2);
   c->Range(0,0,1,1);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
  
// ------------>Primitives in pad: p1
   TPad *p1 = new TPad("p1", "p1",0,0.3,1,1);
   p1->Draw();
   p1->cd();
   p1->Range(-69.4375,4900,569.9375,8566.667);
   p1->SetFillColor(0);
   p1->SetBorderMode(0);
   p1->SetBorderSize(2);
   p1->SetBottomMargin(0);
   p1->SetFrameBorderMode(0);
   p1->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1001[21] = {
   0,
   25,
   50,
   75,
   100,
   125,
   150,
   175,
   200,
   225,
   250,
   275,
   300,
   325,
   350,
   375,
   400,
   425,
   450,
   475,
   500};
   Double_t Graph0_fy1001[21] = {
   8076,
   7993,
   7846,
   7720,
   7615,
   7548,
   7465,
   7435,
   7390,
   7341,
   7313,
   7309,
   7300,
   7253,
   7235,
   7215,
   7148,
   7013,
   6867,
   6670,
   6392};
   Double_t Graph0_fex1001[21] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
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
   Double_t Graph0_fey1001[21] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
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
   TGraphErrors *gre = new TGraphErrors(21,Graph0_fx1001,Graph0_fy1001,Graph0_fex1001,Graph0_fey1001);
   gre->SetName("Graph0");
   gre->SetTitle("");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1001 = new TH1F("Graph_Graph1001","",100,0,550);
   Graph_Graph1001->SetMinimum(4900);
   Graph_Graph1001->SetMaximum(8200);
   Graph_Graph1001->SetDirectory(0);
   Graph_Graph1001->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1001->SetLineColor(ci);
   Graph_Graph1001->GetXaxis()->SetRange(0,92);
   Graph_Graph1001->GetXaxis()->SetLabelFont(42);
   Graph_Graph1001->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1001->GetXaxis()->SetTitleFont(42);
   Graph_Graph1001->GetYaxis()->SetTitle("Tracks passing quality cuts");
   Graph_Graph1001->GetYaxis()->CenterTitle(true);
   Graph_Graph1001->GetYaxis()->SetLabelFont(42);
   Graph_Graph1001->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1001->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph1001->GetYaxis()->SetTitleFont(42);
   Graph_Graph1001->GetZaxis()->SetLabelFont(42);
   Graph_Graph1001->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1001->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1001);
   
   gre->Draw("ap");
   
   Double_t Graph1_fx1002[21] = {
   0,
   25,
   50,
   75,
   100,
   125,
   150,
   175,
   200,
   225,
   250,
   275,
   300,
   325,
   350,
   375,
   400,
   425,
   450,
   475,
   500};
   Double_t Graph1_fy1002[21] = {
   5188,
   5207,
   5221,
   5243,
   5328,
   5375,
   5468,
   5547,
   5653,
   5752,
   5890,
   6001,
   6143,
   6230,
   6252,
   6293,
   6320,
   6228,
   6113,
   5930,
   5660};
   Double_t Graph1_fex1002[21] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
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
   Double_t Graph1_fey1002[21] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
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
   gre = new TGraphErrors(21,Graph1_fx1002,Graph1_fy1002,Graph1_fex1002,Graph1_fey1002);
   gre->SetName("Graph1");
   gre->SetTitle("Graph");
   gre->SetFillStyle(1000);
   gre->SetMarkerStyle(24);
   
   TH1F *Graph_Graph1002 = new TH1F("Graph_Graph1002","Graph",100,0,550);
   Graph_Graph1002->SetMinimum(5074.8);
   Graph_Graph1002->SetMaximum(6433.2);
   Graph_Graph1002->SetDirectory(0);
   Graph_Graph1002->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1002->SetLineColor(ci);
   Graph_Graph1002->GetXaxis()->SetLabelFont(42);
   Graph_Graph1002->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1002->GetXaxis()->SetTitleFont(42);
   Graph_Graph1002->GetYaxis()->SetLabelFont(42);
   Graph_Graph1002->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1002->GetYaxis()->SetTitleOffset(0);
   Graph_Graph1002->GetYaxis()->SetTitleFont(42);
   Graph_Graph1002->GetZaxis()->SetLabelFont(42);
   Graph_Graph1002->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1002->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1002);
   
   gre->Draw("p ");
   
   TLegend *leg = new TLegend(0.5,0.67,0.88,0.88,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("Graph0","Any number of wrong hits","lpf");
   entry->SetFillStyle(1000);
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph1","No wrong hits","lpf");
   entry->SetFillStyle(1000);
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(24);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   p1->Modified();
   c->cd();
  
// ------------>Primitives in pad: p2
   TPad *p2 = new TPad("p2", "p2",0,0.05,1,0.3);
   p2->Draw();
   p2->cd();
   p2->Range(-69.4375,0.5432763,569.9375,0.9149797);
   p2->SetFillColor(0);
   p2->SetBorderMode(0);
   p2->SetBorderSize(2);
   p2->SetTopMargin(0);
   p2->SetBottomMargin(0.2);
   p2->SetFrameBorderMode(0);
   p2->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1003[21] = {
   0,
   25,
   50,
   75,
   100,
   125,
   150,
   175,
   200,
   225,
   250,
   275,
   300,
   325,
   350,
   375,
   400,
   425,
   450,
   475,
   500};
   Double_t Graph0_fy1003[21] = {
   0.6423972,
   0.651445,
   0.6654346,
   0.6791451,
   0.6996717,
   0.7121092,
   0.7324849,
   0.7460659,
   0.7649526,
   0.7835445,
   0.805415,
   0.8210426,
   0.8415068,
   0.8589549,
   0.8641327,
   0.8722107,
   0.8841634,
   0.888065,
   0.8901995,
   0.8890555,
   0.8854819};
   Double_t Graph0_fex1003[21] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
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
   Double_t Graph0_fey1003[21] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
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
   gre = new TGraphErrors(21,Graph0_fx1003,Graph0_fy1003,Graph0_fex1003,Graph0_fey1003);
   gre->SetName("Graph0");
   gre->SetTitle("");
   gre->SetFillStyle(1000);
   gre->SetLineColor(2);
   gre->SetMarkerColor(2);
   gre->SetMarkerStyle(24);
   
   TH1F *Graph_Graph1003 = new TH1F("Graph_Graph1003","",100,0,550);
   Graph_Graph1003->SetMinimum(0.617617);
   Graph_Graph1003->SetMaximum(0.9149797);
   Graph_Graph1003->SetDirectory(0);
   Graph_Graph1003->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1003->SetLineColor(ci);
   Graph_Graph1003->GetXaxis()->SetTitle("Lock low DCA threshold [#mum]");
   Graph_Graph1003->GetXaxis()->SetRange(0,92);
   Graph_Graph1003->GetXaxis()->CenterTitle(true);
   Graph_Graph1003->GetXaxis()->SetLabelFont(43);
   Graph_Graph1003->GetXaxis()->SetLabelSize(15);
   Graph_Graph1003->GetXaxis()->SetTitleSize(20);
   Graph_Graph1003->GetXaxis()->SetTitleOffset(3.5);
   Graph_Graph1003->GetXaxis()->SetTitleFont(43);
   Graph_Graph1003->GetYaxis()->SetTitle("Ratio");
   Graph_Graph1003->GetYaxis()->CenterTitle(true);
   Graph_Graph1003->GetYaxis()->SetNdivisions(6);
   Graph_Graph1003->GetYaxis()->SetLabelFont(43);
   Graph_Graph1003->GetYaxis()->SetLabelSize(15);
   Graph_Graph1003->GetYaxis()->SetTitleSize(20);
   Graph_Graph1003->GetYaxis()->SetTitleOffset(1.75);
   Graph_Graph1003->GetYaxis()->SetTitleFont(43);
   Graph_Graph1003->GetZaxis()->SetLabelFont(42);
   Graph_Graph1003->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1003->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1003->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1003);
   
   gre->Draw("ap");
   p2->Modified();
   c->cd();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
