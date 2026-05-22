#include <bits/stdc++.h>
using namespace std;

// Esto hace que el i/o sea más rápido, desincroniza cin y cout de printf y scanf
#define FASTIO ios::sync_with_stdio(false); cin.tie(nullptr);

#define ll long long

struct SegTree
{
    vector<ll> tree;
    vector<ll> arr;

    SegTree(vector<ll> original_arr)
        : tree(original_arr.size() * 4),
          arr(original_arr)
    {

        build(1, 0, arr.size() - 1);
    }

    ll op(ll a, ll b)
    {
        return a + b;
    }

    void build(ll node, ll l, ll r)
    {
        if (l == r)
        {
            tree[node] = arr[l];
            return;
        }

        ll mid = (l + r) / 2;

        build(node * 2, l, mid);
        build(node * 2 + 1, mid + 1, r);

        tree[node] = op(tree[node * 2], tree[node * 2 + 1]);
    }

    void set(ll idx, ll val)
    {
        update(1, 0, arr.size() - 1, idx, val);
    }

    void update(ll node, ll l, ll r, ll idx, ll val)
    {
        if (l == r)
        {
            tree[node] = val;
            return;
        }

        ll mid = (l + r) / 2;

        if (idx <= mid)
            update(node * 2, l, mid, idx, val);
        else
            update(node * 2 + 1, mid + 1, r, idx, val);

        tree[node] = op(tree[node * 2], tree[node * 2 + 1]);
    }

    ll query(ll l, ll r)
    {
        return get(1, 0, arr.size() - 1, l, r);
    }

    ll get(ll node, ll sl, ll sr, ll l, ll r)
    {
        if (sr < l || r < sl)
            return 0;

        if (l <= sl && sr <= r)
            return tree[node];

        ll mid = (sl + sr) / 2;

        ll left = get(node * 2, sl, mid, l, r);
        ll right = get(node * 2 + 1, mid + 1, sr, l, r);

        return op(left, right);
    }
};

int main()
{
    /*
    Input
    The first line contains two integers n and m (1≤n,m≤100000), the size of the array and the number of operations. 
    The next line contains n numbers ai, the initial state of the array (0≤ai≤109). 
    The following lines contain the description of the operations. 
    The description of each operation is as follows:
        * 1 i v: set the element with index i to v (0≤i<n, 0≤v≤109).
        * 2 l r: calculate the sum of elements with indices from l to r−1 (0≤l<r≤n).
    Output
    For each operation of the second type print the corresponding sum.
    */
    FASTIO

    ll n, m;
    cin >> n >> m;

    vector<ll> a(n);

    for (ll i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    SegTree st(a);
    
    ll comando, p1, p2; // p1= idx o l; p2= val o r
    while(m--){
        cin >> comando >> p1 >> p2;
        if (comando == 1) {
            st.set(p1, p2);
        }else{
            cout << st.query(p1, p2-1) << '\n';
        }
    }
    return 0;
}