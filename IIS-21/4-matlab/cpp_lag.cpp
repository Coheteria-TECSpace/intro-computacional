/******************************************************
 * Interpolar polinomio mediante Lagrange             *
 * Lenguaje C++                                       *
 ******************************************************/

#include <vector>
#include <iostream>

using namespace std;

// Prototipo de funcion
double lagrange_pol_lim(vector<double> x,vector<double> y,double sust);

int main(int argc, char **argv) {
    vector<double> voltaje = {0.0, 0.16, 0.2, 0.31, 0.45, 0.54, 0.6, 
        0.62, 0.65, 0.68, 0.74, 0.82, 0.94, 0.97, 0.99, 1.0};
    vector<double> fuerza = {0.0, 0.11, 0.14, 0.22, 0.35, 0.46, 0.58, 
        0.67, 0.77, 0.88, 1.24, 2.02, 5.09, 7.25, 8.85, 10.0};
    // Llamado a funcion
    cout << lagrange_pol_lim(voltaje,fuerza,0.98) << endl;
    return 0;
}

double lagrange_pol_lim(vector<double> x,vector<double> y,double sust) {

    // Proceso de interpolar datos por método de Lagrange
    vector<double> factores = {};
    double subfactor = 0.0;
    double aprox = 0.0;

    // f(x) = yi*(x - x(j))/(xi - x(j))
    for (int i = 0; i < x.size(); i++) {
        factores.push_back(1.0);
        for (int j = 0; j < x.size(); j++) {
            if ((j != i) && (x.at(i) - x.at(j) != 0)) {
                subfactor = (sust - x.at(j))/(x.at(i) - x.at(j));
                factores.at(i) *= subfactor;
            }
        }
        factores.at(i) *= y.at(i);
        aprox += factores.at(i);
    }
    return aprox;
}
