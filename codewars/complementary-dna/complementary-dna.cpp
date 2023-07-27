#include <string>

std::string DNAStrand(const std::string& dna)
{
  //your code here
  std::string comp = "";
  for (unsigned long i = 0; i < dna.size(); i++) {
    if (dna[i] == 'A') {
      comp += 'T';
    } else if (dna[i] == 'T') {
      comp += 'A';
    } else if (dna[i] == 'C') {
      comp += 'G';
    } else {
      comp += 'C';
    }
  }
  return comp;
}