//Next is exercise 4, copyArray, with the calloc and free that you’ve been circling around. 
//Before you write it, think about three things:

//Size: how many bytes do you need for N ints? (You’ve used calloc(N, sizeof(int)) before; same idea.)
//Failure: what should the function return if calloc fails, and what should the caller check?
//Ownership: the function allocates the memory, but main uses and frees it.
//Say in one sentence why the function must not free it before returning.

# include <stdio.h>
# include <stdlib.h>

int *copyArray(int A[], int N ){
    if (N < 1){
        printf("empty array. invalid input. return 0 for error");
        return 0;
    }
    if (A == NULL){
        printf("invalid input");
        return NULL;
    }
    int *dummy = calloc(N, sizeof(int));
    for (int i = 0; i<N; i++){
        dummy[i] = A[i];    
    }
     
    return dummy;
    
}


int main(void){
    int A[] = {2,5,-28,2,0,0};
    int N = sizeof(A)/sizeof(A[0]);
    int *newarr = copyArray(A, N);
    A[0] = 99;
    
    for (int j = 0; j<N; j++){
        printf("%d\n", A[j]);
    }
    printf("\ncomplete\n");

    for (int j = 0; j<N; j++){
        printf("%d\n", newarr[j]);
    }
    
    free(newarr);
    return 0;
}



