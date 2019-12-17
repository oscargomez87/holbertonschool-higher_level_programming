#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: single linked list
 * Return: 1 if is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *root = *head, *tail = *head;
	unsigned int i = 0, j = 0;

	if (*head == NULL)
		return (1);
	while (tail->next != NULL)
	{
		tail = tail->next;
		j++;
	}
	while (i <= j)
	{
		if (root->n != tail->n)
			return (0);
		i++;
		j--;
	}
	return (1);
}
