#include <iostream>
using namespace std;

void pole(int (*arr)[4]){
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

void swap_ch(int (*arr)[4]){

}


int main() {
    setlocale(LC_ALL,"RU");
    int arr[4][4] = {
        {1, 7, 3, 4},
        {6, 5, 2, 8},
        {9, 16, 11, 10},
        {13, 14, 15, 12}
    };
    cout << "Исходное поле:" << endl;
    pole(arr);
    int num;
    while (){
    cout << "Введите номер плтики, которую хотите переместить:" << endl;
    cin >> num;
    swap_ch()
    }
    return 0;
}

// 1  7  3  4 
// 6  5  2  8
// 9  " " 11 10
// 13 14 15 12