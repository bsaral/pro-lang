/*  
BETÜL SARAL - 14.05.2013

    $ gcc matris.c -lpthread
    $ ./a.out
*/
 
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>  
#include <pthread.h> 
 
#define M 3
#define K 2
#define N 3
 
// Tüm evreler arasýnda paylaþýlan karþýlýklý dýþlayýcý.
static pthread_mutex_t mutex_C;
 
// A ve B matris çarpýmýnýn sonucu C matrisine yazýlýr.
 
static int A [M][K] = { {1,2}, {3,4}, {5,6} };
static int B [K][N] = { {7,8,9}, {3,7,1} };
static int C [M][N];
 
 
void *hesapla(void *mat);
 
struct matris
{
	int i; // satýr
  	int j; // sütun
};
 
int main() {
   	
   	//Sonuç 3x3 lük bir matris 
   	pthread_t thread[3][3];	
   	int i,j;
   	
   	pthread_mutex_init(&mutex_C, NULL);
   	
	for (i = 0; i < M; i++){
   		for(j = 0; j < N; j++){
   			struct matris *veri = (struct matris *) malloc(sizeof(struct matris)); 
   			veri->i = i; // Satýr atanýr
   			veri->j = j; // Sütun atanýr
   			pthread_create(&thread[i][j], NULL, hesapla,(void*) veri); // Thread oluþturulur.
   		}
   	}
   	
   	for (i = 0; i < M; i++){ 
   		for(j = 0; j < N; j++){	
   			pthread_join( thread[i][j],NULL);
   		}
   	}
  	
   	printf("C matrisi:\n");
   	
   	for (i = 0; i < M; i++){
   		for(j = 0; j < N; j++){	
   			printf("%d ",C[i][j]);
  		}
   		printf("\n");
   	}
   	
   	pthread_mutex_destroy(&mutex_C);
   	exit(EXIT_SUCCESS);
}
 
void *hesapla(void *mat)  // C matrisi hesaplanýr.
{
   	struct matris *veri;
   	veri = (struct matris *)mat; 
   	int row = veri->i;
   	int col = veri->j;
   	
   	pthread_mutex_lock(&mutex_C);
   	C[row][col] = (A[row][0]*B[0][col]) + (A[row][1]*B[1][col]);
   	pthread_mutex_unlock(&mutex_C);
   	
   	pthread_exit(0);
}
