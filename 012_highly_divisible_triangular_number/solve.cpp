#include <iostream>
#include <cmath>

using namespace std;

long long get_triangular_number(long long i) {
    return (1 + i) * (i) / 2;
}

int get_num_of_factors(long long value) {
    auto num_of_factors = 0;
    for (long long i = 1; i <= value / 2 + 1; ++i) {
        if (value % i == 0) {
            //cout << i << endl;
            num_of_factors++;
        }
    }
    return num_of_factors + 1;
}

int main() {
    cout << get_num_of_factors(get_triangular_number(14399)) << endl;
    cout << get_triangular_number(14399) << endl;
    long long coefficient[] = {2,3,5,7,11,13,17,19,23,
                               29,31,33,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101};


    /*
    vector<int>

    for (int i = 0; i < 14; i++) //2
        for (int j = 0; j < 9; j++) //3
            for (int k = 0; k < 6; k++) //5
                for (int l = 0; l < 5; l++) //7
                    for (int m = 0; m < 4; m++) //11
                        for (int n = 0; n < 4; n++) // 13
                            for (int o = 0; o < 4; o++) // 17
                                for (int p = 0; p < 4; p++) // 19
                                    for (int q = 0; q < 3; q++) // 23
                                        for(int r = 0; r < 3; r++) // 29
                                            for(int s = 0; s < 3; s++) // 31
                                                //for (int t = 0; t < 3; t++) // 37
                                {
                                    long long val =
                                            (long long)pow(2, i) * (long long)pow(3, j) * (long long)pow(5, k)
                                                    * (long long)pow(7, l) * (long long)pow(11, m) * (long long)pow(13, n)
                                                    *(long long)pow(17, o) * (long long)pow(19, p) * (long long)pow(23, q)
                                                    * (long long)pow(29, r) * (long long)pow(31, s)
                                                    * (long long)pow (37, t) - 1;
                                    ;
                                    if (val > 14399 || val < 0L) continue;
                                    auto tri_val = get_triangular_number(val);
                                    auto num_of_fac = get_num_of_factors(tri_val);
                                    cout << "val is " << val << " and tri_val is " << tri_val << ", num of factors is "
                                         << num_of_fac << endl;
                                    if (num_of_fac >= 500) cout << "Found one!!!" << endl;
                                    val += 1;
                                    tri_val = get_triangular_number(val);
                                    num_of_fac = get_num_of_factors(tri_val);
                                    cout << "val is " << val << " and tri_val is " << tri_val << ", num of factors is "
                                         << num_of_fac << endl;
                                    if (num_of_fac >= 500) cout << "Found one!!!" << endl;
                                }
    */
    return 0;
}