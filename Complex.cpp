#include <iostream>
using namespace std;

class complex
{
    int a, b;

public:
    void set_values(int a1, int b1)
    {
        a = a1;
        b = b1;
    }
    void get_number()
    {
        cout << a << " + i" << b << endl;
    }
    void sum_numbers(complex n1, complex n2)
    {
        int af = n1.a + n2.a;
        int bf = n1.b + n2.b;
        cout << af << " + i" << bf << endl;
    }
};
int main()
{
    complex A, B, C;
    A.set_values(1, 2);
    B.set_values(3, 4);
    A.get_number();
    B.get_number();
    C.sum_numbers(A, B);

    return 0;
}
