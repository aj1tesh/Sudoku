#include<bits/stdc++.h>
#include<vector>

using namespace std;

bool isSafe(int i, int j, int k, vector<vector<int>>& board){

    int n = board.size();

    for(int key=0; key<n; key++){
        //columns
        if(board[i][key]==k){
            return false;
        }
        //rows
        if(board[key][j]==k){
            return false;
        }
        //block
        if( board[(3*(i/3))+(key/3)][(3*(j/3))+(key%3)] == k ){
            return false;
        }
    }

    return true;

}

bool solve(vector<vector<int>>& board){

    int n = board.size();

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            
            if(board[i][j]==0){
                for(int k=1; k<=9; k++){
                    
                    if( isSafe(i, j, k, board) ){
                        
                        board[i][j] = k;

                        bool aagepossible = solve(board);
                        if(aagepossible){
                            return true;
                        }
                        else{
                            board[i][j] = 0;
                        }
                    }
                }
                return false;
            }
        }
    }

    return true;

}

void solveSudoku(vector<vector<int>>& sudoku)
{
    solve(sudoku);
}

void printBoard(const vector<vector<int>>& board) {
    for (const auto& row : board) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << endl;
    }
}

int main() {
    
    vector<vector<int>> board = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}
    };

    if (solve(board)) {
        cout << "Solved Sudoku Board:" << endl;
        printBoard(board);
    } else {
        cout << "No solution." << endl;
    }

    return 0;
}