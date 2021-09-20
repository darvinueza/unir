#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include "solution.h"

void bubble_sort(char* dictionary[], int n_words) {
	int i,j;
	
   
	for(i=0;i<=n_words-1;i++){
			for(j=0;j<=n_words-1-i;j++){
				if	(strcmp(dictionary[j], dictionary[j+1]) > 0)  { 
					swap_word(dictionary,j,j+1);
				
				}
				BasicOpCounter++;
			}
			
	}
	
}

void selection_sort(char* dictionary[], int n_words) {
	int i,j,min;  
	
	for(i=0;i<n_words-1;i++){
			min=i;
			for(j=i+1;j<n_words-i-1;j++){
				if	(strcmp(dictionary[j], dictionary[min]) > 0)  { 
				swap_word(dictionary,j,min);
				min=j;
				
				}
				BasicOpCounter++;
			}
			
	}
}

void insertion_sort(char* dictionary[], int n_words) {
	int i, pos,value,behind;
  	for(i=1;i<=n_words;i++){
  		pos=i;
  		value=strcmp(dictionary[pos-1], dictionary[pos]);
  	
  			while(pos>0 && value>0  ){
  				value=strcmp(dictionary[pos-1], dictionary[pos]);
  				if (value>0){
  					swap_word(dictionary,pos-1,pos);
  					
				  }
  				 			
  			pos--;
  			BasicOpCounter++;
		   }
		   
	}
 
}

void merge(char* dictionary[], int left, int center, int right) {
 	int i,j, i1, i2, k; 
 	
    int n1 = center - left + 1; 
    int n2 =right - center;
    char* sub_array_l[n1];
    char* sub_array_r[n2];
    
	for(i=0;i<n1;i++){
		sub_array_l[i]=dictionary[left+i];
	}
	
	for(j=0;j<n1;j++){
		sub_array_r[j]=dictionary[center+j+1];
	}
	i1=0;
	i2=0;
	k=left;
	while(i1<n1&&i2<n2){
		
		if(strcmp(sub_array_l[i1],sub_array_r[i2])<=0){
			dictionary[k]=sub_array_l[i1];
			i1++;
		}
		else{
			dictionary[k]=sub_array_r[i2];
			i2++;
		}
		k++;
	}
	
	while(i1<n1){
		
		dictionary[k]=sub_array_l[i1];
		i1++;
		k++;
	}
	while(i2<n2){
		dictionary[k]=sub_array_l[i2];
		i2++;
		k++;
	}
	
}

void merge_sort(char* dictionary[], int left, int right) {
	int center;
  if (left<right) {
	center = (left+right) / 2;
	merge_sort(dictionary, left, center);
	merge_sort(dictionary, center+1, right);
	merge(dictionary,left,center,right);
	BasicOpCounter++;
  }
  
}

int split(char* dictionary[], int left, int right) {
	int i, j ;
	char* splitter_value;
	splitter_value = dictionary[left]; 
	i = left+1; j = right;
	do {
	
	while (i<j && ( strcmp(splitter_value, dictionary[i])>0))
	i++;
	
	while (j>=i && (strcmp(splitter_value,dictionary[j])<=0))
	j--;
	
	if (i<j)
	swap_word(dictionary,i,j);
	} while (i<j);

	if (j>left)
		swap_word(dictionary,left,j);
	
	return j;
   
}

void quick_sort(char* dictionary[], int left, int right) {
  
		  if (left<right) {
				int i = split(dictionary, left, right);
				quick_sort(dictionary, left, i-1);
				quick_sort(dictionary, i+1, right);
					BasicOpCounter++;
			}
}
