#include <string>
#include "Python.h"

using namespace std;
  

int main(int argc, char** argv)  
{  
    Py_Initialize();  
    PyRun_SimpleString("import pylab");  
    PyRun_SimpleString("pylab.plot(range(5))");  
    PyRun_SimpleString("pylab.show()");  
    Py_Exit(0);  
} 