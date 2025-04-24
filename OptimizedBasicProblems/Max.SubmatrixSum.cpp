/*
Problem : Given a N * M matrix, find the maimum sum of a submatrix
Approach : Using Kadane's Algorithm

Intuition : Starting from each column say C1, make the submatrix with strating from C1 -> C2 where C1 <= C2 < M,
						now when have to combine the columns row-wise to make them into a single column, and now performing the
						normal "Kadane's Algorithm" will lead to the required answer.

T.C : O(C^2  *  (O(R) + O(R))) ~ O(C^2 * R)
				 |            |
				for         for taking
		traversing     row - sum and
	through columns kadane's Algorithm

Problem Link : https://www.naukri.com/code360/problems/max-submatrix_1214973
*/

// Code

#include <bits/stdc++.h>
int maxSumSubmatrix(vector<vector<int>> &mat, int n, int m)
{
	int res = INT_MIN;
	for (int i = 0; i < m; i++)
	{
		vector<int> row(n);
		for (int j = i; j < m; j++)
		{
			for (int k = 0; k < n; k++)
			{
				row[k] += mat[k][j];
			}
			int curSum = 0;
			for (int k = 0; k < n; k++)
			{
				curSum = max(curSum + row[k], row[k]);
				res = max(res, curSum);
			}
		}
	}
	return res;
}
