#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define min(a, b) (((a) < (b)) ? (a) : (b))
#define max(a, b) (((a) > (b)) ? (a) : (b))

void manachers(char *S, int *A){
   int r = 0, p = 0;
   int N = strlen(S);

   for (int i = 0; i < N; i++){
      if (i <= r)
         A[i] = min(A[2 * p - i], r - i);
      else
         A[i] = 0;

      while (i - A[i] - 1 >= 0 && i + A[i] + 1 < N && S[i - A[i] - 1] == S[i + A[i] + 1])
         A[i]++;

      if (r < i + A[i]){
         r = i + A[i];
         p = i;
      }
   }
}


void addChar(char *buffer, char *S, int *len){
   S = malloc(*len * 2);

   printf("%d", *len);

   for (int i = 0; i < *len; i++){
      S[2 * i] = buffer[i]; // 2n + 1 <- n;
      S[2 * i + 1] = '#'; // 2n <- #
   }
   *len = strlen(S);
   printf("%s", S);
}


int main(){
   char buffer[10001];
   int *len;
   char *S;
   int *A;

   scanf("%s", buffer);

   *len = strlen(buffer);

   S = malloc(*len + 1);
   strncpy(S, buffer, *len);

// 이건 특수문자 추가한 것
   addChar(buffer, S, len);

   A = malloc(strlen(S) * sizeof(int));

   manachers(S, A);

   int ans = -1;
   for (int i = 0; i < *len; i++)
   ans = max(ans, A[i]);

   for(int i = 0; i < *len; i++){
      printf("%d ", A[i]);
   }

   printf("\n%d ", ans);

   return 0;
}
