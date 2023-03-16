#include<stdio.h>
#include<string.h>
#define MAX_STR_SIZE 100
#define MAX_SIZE_DB 100
#define TRUE 1
#define FALSE 0


typedef struct customer{
   char name;
   char phoneNumber;
   char purchaseAmount;
   enum tagfield {consumer, seller} customerType;

   union {
      int minimumConsumer;
      int highestConsumer;
      int averageConsumerAmount;

      int lowestSellers;
      int topSellers;
      int averageSellerAmount;
   } type;
   
};

int getMinimumConsumer(){

}

int getHighestConsumer(){

}

int averageConsumerAmount(){

}

int getLowestSeller(){
	
}

int getTopSeller(){
	
}

int getAverageSellerAmount(){
	
}


int main(){
   char* customerArr = malloc((sizeof(char)*MAX_STR_SIZE)*MAX_SIZE_DB);
   
   printf("Please enter your customer information (<Name> <Customer Type> <Phone Number> <Amount>):\n");
   
   while(TRUE){
      char tempStr[MAX_STR_SIZE];
      scanf("%s", tempStr);
      if(strcmp("--", tempStr) == 0){
         break;
      }
   };

   

   return 0;
}

