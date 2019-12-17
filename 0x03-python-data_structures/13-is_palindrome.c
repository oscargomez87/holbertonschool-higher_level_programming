#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *root, *tail;
	unsigned int i = 0, j = 0;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (0);
	root = *head;
	tail = *head;
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
