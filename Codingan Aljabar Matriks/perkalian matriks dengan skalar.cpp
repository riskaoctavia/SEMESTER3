/* perkalian matriks dengan skalar */

#include <iostream>
#include <conio.h>
#define Nmaks 25
typedef int matriks[Nmaks]
[Nmaks];

int main ();

int colA,rowA,i,j,x;
matriks A, B;
char answer;
do
{
clrscr();
cout<<"PERKALIAN SKALAR MATRIKS"<<endl<<endl;
cout<<"Masukkan Jumlah Baris Matriks A = "
cin>>rowA;
cout<<"Masukkan Jumlah Kolom matrik A = ";
cin>>colA;

clrscr();
cout<<"Masukkan Nilai Matrik A = ";
for(i=1;i<=rowA;i++)
    {
        for(j=1;j<=colA;j++)
            {
                cout<<"A["<<i<<","<<j<<"]=";
                cin>>A[i][j];
            }
    }
cout<<endl<<endl;
cout<<"Masukkan Bilangan Pengali = ";cin>>x;

clrscr();
cout<<endl;
//Preses penjumlahan Matriks
for(i=1;i<=rowA;i++)
    {
        for(j=1;j<=colA;j++)
            {
                B[i][j]=A[i][j]*x;
            }
    }
clrscr();
//Output Matriks A
gotoxy(1,5);
cout<<"A = ";
for(i=1;i<=rowA;i++)
    {
     for(j=1;j<=colA;j++)
        {
            gotoxy(2+4*j,2=2*i);
            cout<<A[i][j];
        }
     }
//Output Matriks B
gotoxy(1,15);
cout<<"B = ";
for(i=1;i<=rowA;i++)
    {
        for(j=1;j<=colA;j++)
            {
                gotoxy(2+4*j,12+2*i);
                cout<<B[i][j];
            }
        }
getch();
clrscr();
cout<<"==PROGRAM SELESAI=="<<endl<<endl;
cout<<"Apakah Ingin Melakukan Perhitungan lagi??[Y/T]";
cin>>answer;
}
while((answer == 'y') || (answer =='Y'));
}
