#include <stdio.h>
#include <list>
#include <map>
#include <string>
#include <boost/unordered_map.hpp>
#include <boost/unordered_set.hpp>
#include <boost/shared_ptr.hpp>
#include <boost/weak_ptr.hpp>
#include <boost/scoped_ptr.hpp>
#include <boost/ptr_container/ptr_container.hpp>
#include <boost/optional.hpp>

using std::list;
using std::map;
using std::string;

struct TestData
{
    int data;
    char c;
};

void break_here()
{

}

int main()
{
    TestData a = {1,'1'};
    TestData b = {2, '2'};

    boost::shared_ptr<TestData> shared_x(&a);
    boost::shared_ptr<TestData> shared_y = shared_x;

    boost::weak_ptr<TestData> weak_x(shared_x);
    boost::weak_ptr<TestData> weak_y = weak_x;

    boost::scoped_ptr<TestData> scoped_x(&a);

    boost::unordered_map<string, TestData> unordered_map_x;
    unordered_map_x["xx"] = a;
    unordered_map_x["yy"] = b;

    boost::unordered_set<string> unordered_set_x;
    unordered_set_x.insert("xx");
    unordered_set_x.insert("yy");
    unordered_set_x.insert("zz");

    boost::ptr_vector<TestData> ptr_vector_x;
    ptr_vector_x.push_back(&a);
    ptr_vector_x.push_back(&b);

    boost::ptr_list<TestData> ptr_list_x;
    ptr_list_x.push_back(&a);
    ptr_list_x.push_back(&b);

    boost::optional<TestData> optional_x(a);

    break_here();

    return 0;
}
