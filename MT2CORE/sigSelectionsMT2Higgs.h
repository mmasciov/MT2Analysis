#ifndef SIGNALREGIONSMT2HIGGS_H
#define SIGNALREGIONSMT2HIGGS_H

#include <string>
#include "TTree.h"
#include "SR.h"

namespace mt2 {

std::vector<SR> getSignalRegionsMT2Higgs();
std::vector<SR> getSignalRegionsHcand();
std::vector<SR> getSignalRegionsZcand();
std::vector<SR> getSignalRegionsMbbMax();
std::vector<SR> getTestRegionsMT2Higgs();

} // namespace mt2

#endif // SIGNALREGIONSMT2HIGGS_H
