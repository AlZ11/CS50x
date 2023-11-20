#include <stdio.h>
#include <stdlib.h>

// Linked list
typedef struct node1 {
    int number;
    struct node1 *next;
}
node1;

// Tree
typedef struct node2 {
    int number;
    struct node2 *left;
    struct node2 *right;
}
node2;

// Hash table
typedef struct node3 {
    char *name;
    struct *number;
    struct node3 *next;
}
node3;

// Try
typedef struct node4 {
    char *number;
    struct node4 *children[26] ;
}
node4;

int main(int argc, char *argv[]) {
    node1 *list = NULL;

    for (int i = 1; i < argc; i++) {
        int number = atoi(argv[i]);

        node1 *n = malloc(sizeof(node1));
        if (n == NULL) {
            return 1;
        }

        n -> number = number;
        n -> next = NULL;
        n -> next = list;
        list = n;
    }

    node1 *ptr = list;
    while (ptr != NULL) {
        printf("%i\n", ptr->number);
        ptr = ptr -> next;
    }

    bool search(node2 *tree, int number) {
        if (tree == NULL) {
            return false;
        }

        else if (number < tree->number) {
            return search(tree->left, number)
        }

        else if (number > tree->number) {
            return search(tree->right, number)
        }

        else {
            return true;
        }
    }
}
