#include <stdio.h>
//Write int hasDuplicate(int A[], int N) returning 1 if any value repeats and 0 otherwise. 
//Use two nested loops, since correctness matters more than speed here.

#include <stdlib.h>

int hasDuplicate(int A[], int N){
    int counter = 0;
    for (int i = 0; i<N; i++){
        for (int j=0; j < N; j++){
            if (A[i] == A[j] && i!=j){
                
                counter = 1;
                return 1;
                break;
            }
            
        }
        if (counter == 1){
            
            break;
        }
    }
    if (counter != 1){
        return 0;
    }
    else{
        return 1;
    }
    
    
}

int main(void) {
    int A[] = {3, 8, 2, 6, 9, 3};
    int N = 6;

    printf("%d\n", N);   // replace with your code
    
    int dup = hasDuplicate(A,N);
    printf("%d\n", dup);

    return 0;
    
}
