#ifndef FSL_H
#define FSL_H

// C++
#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <map>

// ROOT
#include "TMath.h"
#include "TLorentzVector.h"
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TProfile.h"
#include "TChain.h"

// Tools
#include "../CORE/Tools/utils.h"
#include "../CORE/Tools/goodrun.h"
#include "../CORE/Tools/dorky/dorky.h"
#include "../CORE/Tools/badEventFilter.h"

#include "../MT2CORE/mt2tree.h"
#include "../MT2CORE/configurations.h"
#include "../MT2CORE/applyWeights.h"

#define likely(x)       __builtin_expect((x),1)
#define unlikely(x)     __builtin_expect((x),0)

class FshortLooper {
 public:
  FshortLooper();
  ~FshortLooper();
  int InEtaPhiVetoRegion(float eta, float phi);
  bool FillHists(const std::vector<TH2D*> hist, const double weight, const int fill_type, const int len_index=1);
  int loop(TChain* ch_st, char* infile, std::string config_tag);
  float getAverageISRWeight(const int evt_id, const int var);
 private:
  MT2Configuration config_;
  MT2Configuration data_config_;

};

#endif
