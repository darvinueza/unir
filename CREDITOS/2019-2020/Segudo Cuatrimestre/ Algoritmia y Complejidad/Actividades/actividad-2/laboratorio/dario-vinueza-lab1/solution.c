// Laboratorio: Dario Vinueza
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include "solution.h"

void imprimirArreglo(char* dictionary[], int n_words) {
    for (int i = 0; i < n_words; i++) {
        printf("%s ", dictionary[i]);
    }
    printf("%s ", "\n\n");
}

void bubble_sort(char* dictionary[], int n_words) {
    //printf("%s \n\n ", "bubble_sort");
    
    //imprimirArreglo(dictionary, n_words);
    
    char *tmp;
    for (int i = 0; i < n_words-1; i++) {
        for (int j = i+1; j < n_words; j++) {
            BasicOpCounter++;
            if (strcmp(dictionary[i], dictionary[j]) > 0) {
                tmp = dictionary[i];
                dictionary[i] = dictionary[j];
                dictionary[j] = tmp;
            }
        }
    }
    
    //imprimirArreglo(dictionary, n_words);
    printf("BO: %llu \n", BasicOpCounter);
    
}

void selection_sort(char* dictionary[], int n_words) {
    //printf("%s \n\n ", "selection_sort");
    
    //imprimirArreglo(dictionary, n_words);
    
    char *minStr;
    for (int i = 0; i < n_words-1; i++) {
        int min_idx = i;
        minStr = dictionary[i];
        for (int j = i+1; j < n_words; j++) {
            BasicOpCounter++;
            if (strcmp(minStr, dictionary[j]) > 0) {
                minStr = dictionary[j];
                min_idx = j;
            }
        }
        
        if (min_idx != i) {
            char *temp;
            temp = dictionary[i];
            dictionary[i] = dictionary[min_idx];
            dictionary[min_idx] = temp;
        }
    }
    
    //imprimirArreglo(dictionary, n_words);
    //printf("BO: %llu \n", BasicOpCounter);
}

void insertion_sort(char* dictionary[], int n_words) {
    //printf("%s \n\n ", "insertion_sort");
    
    char *minStr;
    for (int i = 1; i < n_words; i++) {
        minStr = dictionary[i];
        int j = i - 1;
        
        BasicOpCounter++;
        while (j >= 0 && strcmp(dictionary[j], minStr) > 0) {
            dictionary[j + 1] = dictionary[j];
            j = j - 1;
        }
        
        dictionary[j + 1] = minStr;
    }
    
    //imprimirArreglo(dictionary, n_words);
    //printf("BO: %llu \n", BasicOpCounter);
}

void merge(char* dictionary[], int left, int center, int right) {
    
    int nl = center - left + 1;
    int nr = right - center;
    
    char **L = malloc(sizeof(char*) *nl);
    char **R = malloc(sizeof(char*) *nr);
    
    for (int i = 0; i < nl; i++) {
        L[i] = malloc(sizeof(dictionary[left + i]));
        strcpy(L[i], dictionary[left + i]);
    }
    
    for (int i = 0;i < nr; i++) {
        R[i] = malloc(sizeof(dictionary[center + i + 1]));
        strcpy(R[i], dictionary[center + i + 1]);
    }
    
    int i = 0;
    int j = 0;
    int k = left;
    while (i < nl && j < nr) {
        if (strcmp(L[i], R[j]) < 0) {
             BasicOpCounter++;
            strcpy(dictionary[k++], L[i++]);
        } else {
             BasicOpCounter++;
            strcpy(dictionary[k++], R[j++]);
        }
    }
    
    while (i < nl) {
         BasicOpCounter++;
        strcpy(dictionary[k++], L[i++]);
    }
    
    while (j < nr) {
         BasicOpCounter++;
        strcpy(dictionary[k++], R[j++]);
    }
    
    //printf("BO: %llu \n", BasicOpCounter);
}

void merge_sort(char* dictionary[], int left, int right) {
    
    if (left < right) {
        int middle = (left + right) / 2;
        merge_sort(dictionary, left, middle);
        merge_sort(dictionary, middle + 1, right);
        merge(dictionary, left, middle, right);
    }
}

int split(char* dictionary[], int left, int right) {
    
    char *splitter_value = dictionary[left];
    
    int i = left + 1;
    int j = right;
    
    do {
        while (i<j && dictionary[i] < splitter_value)
            i++;
        
        while (j>=i && dictionary[j] >= splitter_value)
            j--;
        
        if (i < j) {
            BasicOpCounter++;
            char *tmp;
            tmp = dictionary[i];
            dictionary[i] = dictionary[j];
            dictionary[j] = tmp;
        }
    } while(i < j);
    
    if (j > left) {
        BasicOpCounter++;
        char *tmp;
        tmp = dictionary[left];
        dictionary[left] = dictionary[j];
        dictionary[j] = tmp;
    }
    
    //printf("BO: %llu \n", BasicOpCounter);
    
    return j;
}

void quick_sort(char* dictionary[], int left, int right) {
    
    if (left < right) {
        int i = split(dictionary, left, right);
        quick_sort(dictionary, left, i-1);
        quick_sort(dictionary, i+1, right);
    }
}
