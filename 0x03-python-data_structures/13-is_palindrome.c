#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if it is, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *tmp;
    int flag = 0;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        tmp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = tmp;
    }
    if (fast != NULL)
        slow = slow->next;

    while (slow != NULL)
    {
        if (slow->n != prev->n)
            flag = 1;
        slow = slow->next;
        prev = prev->next;
    }
    if (flag == 1)
        return (0);
    else
        return (1);
}
