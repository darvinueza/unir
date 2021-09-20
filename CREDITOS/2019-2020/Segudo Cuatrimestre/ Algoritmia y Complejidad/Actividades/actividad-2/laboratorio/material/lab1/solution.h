#ifndef SOLUTION_H
#define	SOLUTION_H

extern long long BasicOpCounter;

void swap_word(char* dictionary[], int i, int j);
void bubble_sort(char* dictionary[], int n_words);
void selection_sort(char* dictionary[], int n_words);
void insertion_sort(char* dictionary[], int n_words);
void merge_sort(char* dictionary[], int left, int right);
void quick_sort(char* dictionary[], int left, int right);

#endif
