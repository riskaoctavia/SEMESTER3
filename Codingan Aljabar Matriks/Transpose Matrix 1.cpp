#include <iostream>
using namespace std;
int main(){
  int i, j, m, n, matriks[10][10], transpose[10][10];
  cout << "Masukkan jumlah baris matriks: ";
  cin >> m;
  cout << "Masukkan jumlah kolom matriks: ";
  cin >> n;
  cout << "Masukkan elemen matriks\n";
  
  //Menyimpan Elemen Matriks
  for (i = 0; i < m; i++){
    for (j = 0; j < n; j++){
      cin  >> matriks[i][j];
    }
  }
  
  // Mencetak Matriks
   cout << "\nMasukkan Matrix: " << endl;
   for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
         cout << " " << matriks[i][j];
         if (j == n - 1)
            cout << endl << endl;
        }
    }
   
   //Menghitung Transpose Matrix 
  for (i = 0; i < m; i++){
    for (j = 0; j < n; j++){
      transpose[j][i] = matriks[i][j];
    }
  }
  
  //Cetak Transpose
  cout << "Hasil Transpose Matriks: \n";
  for (i = 0; i < n; i++){
    for (j = 0; j < m; j++){
      cout << transpose[i][j];
      if (j == m - 1)
       cout << endl << endl;
    }
}
    cout << endl;
  }
