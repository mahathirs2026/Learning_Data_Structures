//Now exercise 2: void minMax(int A[], int N, int *min, int *max).
//Before you write, decide:
//What should *min and *max start as? (Think about the all-negative lesson.)
//Where should the loop start?
//How do you write into a pointer parameter? (Hint: the same pattern as *a = *b in swap.)
//Call it from main as minMax(A, N, &lo, &hi) and test with {3, 8, 2, 3, 3, 2} (min 2, max 8), {-5, -2, -9} (min -9, max -2), and {7} (both 7). Send it over when it runs.
# include <stdio.h>
# include <stdlib.h>

void minMax(int A[], int N, int *min, int *max){
    int high = A[0];
    int low = A[0];
    
    for (int i = 0; i< N; i++){
        if (high < A[i]){
            high = A[i];
        }
        
        if (low > A[i]){
            low = A[i];
        }
    }
    *min = low;
    *max = high;
    //printf("%d\n", high);
    //printf("%d\n", low);
}

int main(void){
    int hi;
    int lo;
    
    int A[] = {0,0,0,0,0,0,0,0,0,0,0,0};
    int N = sizeof(A)/sizeof(A[0]);
    minMax(A, N, &lo, &hi);
    printf("Maximum Value: %d\n", hi);
    printf("Minimum Value: %d\n", lo);
    
    return 0;
}
