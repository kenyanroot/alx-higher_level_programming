#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_listint - reverses a listint_t linked list
 * @head: pointer to the address of the head of the listint_t linked list
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;
    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
    return (*head);
}

/**
 * compare_lists - compares two lists
 * @head1: first list
 * @head2: second list
 * Return: 1 if lists are identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
    listint_t *temp1 = head1;
    listint_t *temp2 = head2;

    while (temp1 && temp2)
    {
        if (temp1->n != temp2->n)
            return (0);
        temp1 = temp1->next;
        temp2 = temp2->next;
    }
    return (temp1 == NULL && temp2 == NULL);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head, *slow = *head;
    listint_t *second_half, *prev_slow = *head;
    listint_t *midnode = NULL;
    int res = 1;

    if (*head && (*head)->next)
    {
        /* Find the middle of the list */
        while (fast && fast->next)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        /* Handle odd-sized lists */
        if (fast)
        {
            midnode = slow;
            slow = slow->next;
        }

        /* Reverse the second half of the list */
        second_half = reverse_listint(&slow);

        /* Compare the lists */
        res = compare_lists(*head, second_half);

        /* Reverse the second half again to restore the list */
        reverse_listint(&second_half);

        /* Fix the middle node for odd-sized lists */
        if (midnode)
        {
            prev_slow->next = midnode;
            midnode->next = second_half;
        }
        else
        {
            prev_slow->next = second_half;
        }
    }
    return (res);
}
