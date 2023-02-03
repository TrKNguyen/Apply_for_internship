#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define pll pair<ll,ll>
#define ff first
#define ss second
#define endl "\n"
#define pb push_back
#define F(i,a,b) for(ll i=a;i<=b;i++)

const ll maxn=5e5+100;
const ll base=3e18;
const ll mod= 1e9+7 ;

mt19937 rnd(chrono::steady_clock::now().time_since_epoch().count());


ll cnt[30];
ll cntnw=0;
void add(char x)
{
    ll t=x-'a'+1;
    cnt[t]++;
    if (cnt[t]==1) cntnw++;
}
void ers(char x)
{
    ll t=x-'a'+1;
    cnt[t]--;
    if (cnt[t]==0) cntnw--;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    if (fopen("t.inp","r"))
    {
        freopen("test.inp","r",stdin);
        freopen("test.out","w",stdout);
    }
    string s;
    cin>> s;
    ll k;
    cin>> k;
    ll n=s.length();
    ll lf=0;
    while (cntnw<=k&&lf<s.length())
    {
        add(s[lf]);
        lf++;
    }
    ll res=lf-1;
    for (int i=1; i<n;i++)
    {
        ers(s[i-1]);
        while (cntnw<=k&&lf<s.length()) add(s[lf]),lf++;
        res=max(res,lf-2-i+1);
    }
    cout <<res<<endl;
}

