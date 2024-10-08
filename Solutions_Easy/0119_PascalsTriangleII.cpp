class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        // Reusing the code from Problem 118
        vector<int> row;
        vector<vector<int>> retVal;
        if (numRows == 0)
            return retVal;

        row.push_back(1);
        retVal.push_back(row);

        if (numRows == 1)
            return retVal;

        row.push_back(1);
        retVal.push_back(row);

        if (numRows == 2)
            return retVal;

        row.clear();

        for (int i = 2; i < numRows; i++) {
            row.push_back(1);
            for (int j = 1; j < i; j++) {
                row.push_back(retVal[i - 1][j - 1] + retVal[i - 1][j]);
            }
            row.push_back(1);
            retVal.push_back(row);
            row.clear();
        }

        return retVal;
    }

    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0) {
            return {1};
        }
        auto temp = generate(rowIndex + 1);
        return temp[temp.size() - 1];
    }
};