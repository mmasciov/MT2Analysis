import ROOT
import glob
import os

ROOT.gROOT.SetBatch(1)

dir = "looper_output/v6/qcd/"
dir_noRS = "looper_output/v6/qcd_noRS/"

hrs = ROOT.TH1D("hrs","",44,0,44)
hnrs = ROOT.TH1D("hnrs","",44,0,44)

h_evts_rs = ROOT.TH1D("h_evts_rs","",1,0,2)
h_evts_nrs = ROOT.TH1D("h_evts_nrs","",1,0,2)

frs = ROOT.TFile(os.path.join(dir,"merged_hists.root"))
fnrs = ROOT.TFile(os.path.join(dir_noRS,"merged_hists.root"))
ibin = 0
for ht_reg in ["L","M","H","UH"]:
  sum_rs = 0
  sum_nrs = 0
  for top_reg in range(1,12):
    ibin+=1
    print ibin, top_reg, ht_reg

    if h_evts_rs:
      h_evts_rs.Reset()
    if h_evts_nrs:
      h_evts_nrs.Reset()
    try:
      h_evts_rs = frs.Get("sr{0}{1}/h_Events_w".format(top_reg,ht_reg))
    except:
      pass
    try:
      h_evts_nrs = fnrs.Get("sr{0}{1}/h_Events_w".format(top_reg,ht_reg))
    except:
      pass

    if h_evts_rs:
      hrs.SetBinContent(ibin, h_evts_rs.GetBinContent(1))
      hrs.SetBinError(ibin, h_evts_rs.GetBinError(1))
    else:
      hrs.SetBinContent(ibin, 0)
      hrs.SetBinError(ibin, 0)

    if h_evts_nrs:
      hnrs.SetBinContent(ibin, h_evts_nrs.GetBinContent(1))
      hnrs.SetBinError(ibin, h_evts_nrs.GetBinError(1))
    else:
      hnrs.SetBinContent(ibin, 0)
      hnrs.SetBinError(ibin, 0)

    sum_rs += hrs.GetBinContent(ibin)
    sum_nrs += hnrs.GetBinContent(ibin)

  ratio = sum_rs/sum_nrs if sum_nrs > 0 else 0
  print "{0} HT: rs = {1}, nrs = {2}, ratio = {3}".format(ht_reg, sum_rs, sum_nrs, ratio)
        
ROOT.gStyle.SetOptStat(0)

c = ROOT.TCanvas("c","c",900,600)

pads = []
pads.append(ROOT.TPad("1","1",0.0,0.18,1.0,1.0))
pads.append(ROOT.TPad("2","2",0.0,0.0,1.0,0.19))

pads[0].SetTopMargin(0.08)
pads[0].SetBottomMargin(0.13)
pads[0].SetRightMargin(0.05)
pads[0].SetLeftMargin(0.10)

pads[1].SetRightMargin(0.05)
pads[1].SetLeftMargin(0.10)

pads[0].Draw()
pads[1].Draw()
pads[0].cd()

pads[0].SetLogy(1)
pads[1].SetTickx(1)
pads[0].SetTicky(1)
pads[1].SetTicky(1)

hrs.SetLineColor(ROOT.kBlack)
hrs.SetMarkerColor(ROOT.kBlack)
hrs.SetMarkerStyle(20)

hnrs.SetLineColor(401)
hnrs.SetMarkerColor(401)
hnrs.SetMarkerStyle(20)

hnrs.GetYaxis().SetRangeUser(1e-3,1e3)
hnrs.GetXaxis().SetLabelSize(0)

hnrs.Draw("PE")
hrs.Draw("PE SAME")

line = ROOT.TLine()
line.SetLineStyle(2)
for ix in [11,22,33]:
  x = pads[0].GetLeftMargin() + ix/44.0 * (1-pads[0].GetLeftMargin()-pads[0].GetRightMargin())
  line.DrawLineNDC(x,1-pads[0].GetTopMargin(),x,pads[0].GetBottomMargin())

leg = ROOT.TLegend(0.815,0.78,0.94,0.9)
leg.AddEntry(hrs, "R&S from MC")
leg.AddEntry(hnrs, "QCD MC")
leg.Draw()

text = ROOT.TLatex()
text.SetNDC(1)
text.SetTextSize(0.03)
text.DrawLatex(0.18,0.79,"Low H_{T}")
text.DrawLatex(0.39,0.79,"Medium H_{T}")
text.DrawLatex(0.60,0.79,"High H_{T}")
text.DrawLatex(0.81,0.73,"Extreme H_{T}")
text.SetTextFont(42)
text.SetTextSize(0.04)
text.DrawLatex(0.8,0.93,"1 fb^{-1} (13 TeV)")


binWidth = (1-pads[0].GetLeftMargin()-pads[1].GetRightMargin())/44.0
binLabels = ["2-3j, 0b", "2-3j, 1b", "2-3j, 2b", "4-6j, 0b", "4-6j, 1b", "4-6j, 2b", "#geq7j, 0b", "#geq7j, 1b", "#geq7j, 2b", "2-6j, #geq3b", "#geq7j, #geq3b"]
text = ROOT.TLatex()
text.SetNDC(1)
text.SetTextAlign(32)
text.SetTextAngle(90)
text.SetTextSize(min(binWidth * 1.3,0.027))
text.SetTextFont(42)
for ibin in range(11):
  x = pads[0].GetLeftMargin() + (ibin+0.5)*binWidth
  y = pads[0].GetBottomMargin()-0.009
  text.DrawLatex(x,y,binLabels[ibin])
  text.DrawLatex(x+11*binWidth,y,binLabels[ibin])
  text.DrawLatex(x+22*binWidth,y,binLabels[ibin])
  text.DrawLatex(x+33*binWidth,y,binLabels[ibin])



## ratio
pads[1].cd()

h_ratio = hrs.Clone("h_ratio")
h_ratio.Divide(hnrs)

h_ratio.GetYaxis().SetRangeUser(0,5)
h_ratio.GetYaxis().SetNdivisions(505)
h_ratio.GetYaxis().SetTitle("R&S/MC")
h_ratio.GetYaxis().SetTitleSize(0.16)
h_ratio.GetYaxis().SetTitleOffset(0.18)
h_ratio.GetYaxis().SetLabelSize(0.13)
h_ratio.GetYaxis().CenterTitle()
h_ratio.GetYaxis().SetTickLength(0.02)
h_ratio.GetXaxis().SetLabelSize(0)
h_ratio.GetXaxis().SetTitle("")
h_ratio.GetXaxis().SetNdivisions(44,0,0)
h_ratio.GetXaxis().SetTickSize(0.06)
h_ratio.SetMarkerStyle(20)
h_ratio.SetMarkerSize(1.0)
h_ratio.SetLineWidth(1)

h_ratio.Draw("PE")

line = ROOT.TLine()
line.DrawLine(0,1,44,1)

username = os.environ["USER"]
c.SaveAs("/home/users/{0}/public_html/mt2/RebalanceAndSmear/MCtests/closure.pdf".format(username))
c.SaveAs("/home/users/{0}/public_html/mt2/RebalanceAndSmear/MCtests/closure.png".format(username))

raw_input()
