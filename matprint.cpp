#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream infile("stardata.txt"); // open input file
    ofstream outfile("output.txt"); // open output file

    char ch;

    // read character by character from input file and write to output file
    while (infile.get(ch)) {
        outfile.put(ch);
    }

    // close files
    infile.close();
    outfile.close();

    return 0;
}
