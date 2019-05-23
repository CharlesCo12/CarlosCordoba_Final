#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

void curva(int tmax, string filename);
const float m = 7294.29;
const float q = 2.0;
const float dt = 0.1;

int main(){
    curva(10,"datos.dat");
    return 0;
}

void curva(int tmax, string filename){    
    ofstream outfile;
    outfile.open(filename);  
    float x = 1.0;
    float y = 0.0;
    float t = 0.0;
    float v0 = 0.0;
    float vy = 1.0;
    float E = 0.0;
    while(t<tmax)
    {
        outfile << t << " "<< x <<" " << y <<endl;
        if((t>30) && (t<50)){
            E=3.0;
        }
        else{
            E=0.0;
        }
        x = x+ dt*v0;
        y = y+ dt*vy;
        vy = vy + q*E*dt/m;
        v0 = v0;
        t = t+dt;
    }
    outfile.close();
}