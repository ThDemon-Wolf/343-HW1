#include "lite_vector.h"
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define INITIAL_CAPACITY 4

// Helper function to resize the vector.
static bool lv_resize(lite_vector* vec) {
    size_t new_capacity = vec->max_capacity * 2;
    void** new_data = realloc(vec->data, new_capacity * sizeof(void*));

    if (!new_data) {
        // Failed to resize, leave original vector unaffected
        return false;
    }

    vec->data = new_data;
    vec->max_capacity = new_capacity;
    return true;
}

// Create a new lite_vector.
lite_vector* lv_new_vec(size_t type_size) {
    lite_vector* vec = (lite_vector*)malloc(sizeof(lite_vector));
    if (!vec) return NULL;

    vec->length = 0;
    vec->max_capacity = INITIAL_CAPACITY;
    vec->type_size = type_size;
    vec->data = (void**)malloc(vec->max_capacity * sizeof(void*));

    if (!vec->data) {
        free(vec);
        return NULL;
    }

    return vec;
}

// Free all memory used by the vector.
void lv_cleanup(lite_vector* vec) {
    if (vec) {
        free(vec->data);
        free(vec);
    }
}

// Get the current number of elements stored in the vector.
size_t lv_get_length(lite_vector* vec) {
    if (!vec) return 0;
    return vec->length;
}

// Clear the contents of the vector and reset it to a default state.
bool lv_clear(lite_vector* vec) {
    if (!vec) return false;
    vec->length = 0;
    return true;
}

// Get an element from an index from a vector.
void* lv_get(lite_vector* vec, size_t index) {
    if (!vec || index >= vec->length) return NULL;
    return vec->data[index];
}

// Add an element to the vector, and extend the vector if needed.
bool lv_append(lite_vector* vec, void* element) {
    if (!vec || !element) return false;

    if (vec->length == vec->max_capacity) {
        if (!lv_resize(vec)) {
            return false;
        }
    }

    vec->data[vec->length] = element;
    vec->length++;
    return true;
}