#include <iostream>

using namespace std;

class CKelvin
{
double dK;

public:
 CKelvin(double Celsius=0)
{
 dK = Celsius + 273.15;
}
operator double() { return dK;}

};

int
main(void)
{
  double dCelsiusDegree;
  cout<<"Input the temperature in Celsius->";
  cin>>dCelsiusDegree;

  CKelvin K(dCelsiusDegree);

  cout<<"In Celsius it is="
    <<endl 
  	<<double(K)-273.15 
  	<<"In Kelvin it is="
  	<<endl
  	<<double(K)
  	<<endl;

  return EXIT_SUCCESS;
}