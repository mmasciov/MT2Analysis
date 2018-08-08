#ifndef SHORTTRACKLOOPER_H
#define SHORTTRACKLOOPER_H

// C++
#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <map>
#include <vector>

// ROOT
#include "TMath.h"
#include "TLorentzVector.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile.h"
#include "TChain.h"

#include "../CORE/Tools/utils.h"

#include "../MT2CORE/mt2tree.h"

#define likely(x)       __builtin_expect((x),1)
#define unlikely(x)     __builtin_expect((x),0)

class ShortTrackLooper {
 public:
  ShortTrackLooper();
  ~ShortTrackLooper();
  int loop(TChain* ch_st, char* infile);
};

#endif
