# include <iostream>
using namespace std;

class shop
{
    int item_id[10];
    int item_price[10];
    int amt_items;

    public:
    void counter()
    {
        amt_items = 0;
    }
    void set_id_and_price()
    {
        cout<<"Enter item Id :"<<endl;
        cin>>item_id[amt_items];
        cout<<"Enter item price :"<<endl;
        cin>>item_price[amt_items];
        amt_items ++;
    }
    void display_id_and_price()
    {
        for (int i = 0; i < amt_items; i++)
        {
            cout<<"Item "<< i + 1 <<" id - "<<item_id[i]<<endl;
            cout<<"Item "<< i + 1 <<" price - "<<item_price[i]<<endl;
        }
        
    }
};

int main()
{
    shop Dm;
    Dm.counter();
    Dm.set_id_and_price();
    Dm.set_id_and_price();
    Dm.set_id_and_price();
    Dm.display_id_and_price();
    return 0;
}
