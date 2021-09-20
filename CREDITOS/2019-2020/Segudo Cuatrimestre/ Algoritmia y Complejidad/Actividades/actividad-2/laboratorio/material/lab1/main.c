#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "solution.h"

#define MAX_WORDS_IN_DICTIONARY 100000
#define MAX_WORD_LENGTH 255

long long BasicOpCounter;

/**
 * Ensures that the arguments are correct
 */
void sanity_check(int argc, const char* argv[]) {
    int incorrect = 0;
  if (argc < 3) {
    incorrect = 1;
  } else if (strcmp(argv[1], "bubble") && strcmp(argv[1], "insertion") && strcmp(argv[1], "selection")
             && strcmp(argv[1], "mergesort") && strcmp(argv[1], "quicksort")) {
    incorrect = 1;
  }
  if (incorrect) {
    fprintf(stderr, "The number of arguments is incorrect. You have to pass the <algorithm> <filename> [<n_words>] as arguments.\n");
    fprintf(stderr, "Feasible algorithms: bubble, insertion, selection, mergesort, quicksort\n");
    exit(EXIT_FAILURE);
  }
}

/**
 * Loads a dictionary 
 * @return the number of elements loaded
 */
int load_dictionary(const char* filename, char* dictionary[]) {
  int i;
  char buffer_line[MAX_WORD_LENGTH];
  FILE* fd = fopen(filename, "r");
  if (fd==NULL) {
    fprintf(stderr,"There was an error loading the file %s\n", filename);
    exit(EXIT_FAILURE);
  }
  for (i=0 ; fgets(buffer_line, MAX_WORD_LENGTH, fd)!=NULL ; i++) {
    // Stores the retrieved word
    dictionary[i] = (char*) malloc(strlen(buffer_line)+1);
    strcpy(dictionary[i], buffer_line);
    // Removes carriage return
    char* cr = strrchr(dictionary[i], '\r');
    if (cr) *cr = '\0';
    cr = strrchr(dictionary[i], '\n');
    if (cr) *cr = '\0';
  }
  fclose(fd);
  return i;
}

/**
 * Frees the dynamic memory of a dictionary
 */
void free_dictionary(char** dictionary, int n_words) {
  int i;
  for (i=0;i<n_words;i++) {
    free(dictionary[i]);
  }
}

/**
 * Swaps two elements in the dictionary and instrument 
 * the count of swaps
 */
void swap_word(char* dictionary[], int i, int j) {
  char* tmp = dictionary[i];
  dictionary[i] = dictionary[j];
  dictionary[j] = tmp;
}

/**
 * Returns the difference in seconds between two call to clock()
 * clock() returns the number of ticks, so we divide into
 * CLOCKS_PER_SEC/1.0 to obtain the difference in seconds
 */
double diffclock(clock_t clock1, clock_t clock2) {
  double diffticks = clock2 - clock1;
  double diff_sec = (diffticks) / (CLOCKS_PER_SEC / 1.0);
  return diff_sec;
}

int main(int argc, const char* argv[]) {
    sanity_check(argc, argv);
    char* dictionary[MAX_WORDS_IN_DICTIONARY];
    int n_words = load_dictionary(argv[2], dictionary);
    
  
    if (argc==4) {
        n_words = atoi(argv[3]);
    }
    
    BasicOpCounter = 0;
    clock_t clock1 = clock();
    if (!strcmp(argv[1],"bubble")) {
        bubble_sort(dictionary, n_words);
    } else if (!strcmp(argv[1],"selection")) {
        selection_sort(dictionary, n_words);
    } else if (!strcmp(argv[1],"insertion")) {
        insertion_sort(dictionary, n_words);
    } else if (!strcmp(argv[1],"mergesort")) {
        merge_sort(dictionary, 0, n_words-1);
    } else if (!strcmp(argv[1],"quicksort")) {
        quick_sort(dictionary, 0, n_words-1);
    }
  clock_t clock2 = clock();
    printf("Algorithm '%s' took %lf seconds and %lld basic operations with %d words\n", argv[1], diffclock(clock1, clock2), BasicOpCounter, n_words);
  free_dictionary(dictionary, n_words);
  return (EXIT_SUCCESS);
}

