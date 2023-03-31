#include<iostream>
#include<algorithm>
#include<cstdio>
#include<set>  //集合容器   去重 ，排序 

struct Sck{
	int a, b;
//	bool operator<(const Sck &x) const
//	{
//		return a > x.a;
//	}
}s[105];

struct Cmp{
	bool operator()(const Sck &x, const Sck &y){
		return x.a>y.a;
	}
};

using namespace std;
//int t, x;
//set<int, Cmp> st;
int main()
{
	int t;
	cin >> t;
	for(int i = 1;i <= t;i++)
	{
		cin >> s[i].a >> s[i].b;
	}
	sort(s + 1, s + t + 1, Cmp());
	return 0;
}
