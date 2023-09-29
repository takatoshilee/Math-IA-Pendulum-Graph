#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;

// Constants:
const int n = 1000; // Number of terms in partial sum
const double grav = 9.81; // Acceleration due to gravity in meters per (second squared)
const int num_points = 30; // Number of points for angles and lengths

// Function to calculate the elliptic integral
double elliptic_integral(int n, double r) {
    double partial_sum = 1.0; // n=0 term
    double prod = 1.0; // This will be the double factorial term
    
    for (int i = 1; i <= n; ++i) {
        prod *= (2 * i - 1) / static_cast<double>(2 * i); // Ensure floating-point division
        partial_sum += pow(prod, 2) * pow(r, 2 * i); // Adds term to partial sum
    }
    
    return (M_PI / 2) * partial_sum; // Adds factor of pi/2
}

int main() {
    // Create arrays of angles and lengths
    vector<double> angles;
    vector<double> lengths;
    
    for (int i = 0; i < num_points; ++i) {
        double angle = static_cast<double>(i) * (90.0 / static_cast<double>(num_points - 1));
        angles.push_back(angle);
        lengths.push_back(1.0 + static_cast<double>(i) * (2.0 / static_cast<double>(num_points - 1)));
    }

    // Open a file for writing data
    ofstream dataFile("pendulum_data.txt");

    // Iterate over initial angles and lengths, and calculate the percentage error
    for (double angle : angles) {
        for (double length : lengths) {
            double phi = angle * (M_PI / 180); // Converts degrees to radians
            
            // Period is 4 sqrt(L/g) F(r), where r = sin(phi / 2):
            double true_period = 4 * sqrt(length / grav) * elliptic_integral(n, sin(phi / 2));
            double approx_period = 2 * M_PI * sqrt(length / grav);
            double percent_error = ((true_period / approx_period) - 1) * 100;
            
            // Write data to the file
            dataFile << angle << " " << length << " " << percent_error << endl;
        }
    }

    // Close the data file
    dataFile.close();

    return 0;
}
