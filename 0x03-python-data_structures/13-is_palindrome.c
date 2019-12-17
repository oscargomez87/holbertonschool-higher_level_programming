#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *root, *end, *bp;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	bp = *head;
	while (bp)
		bp = bp->next;
	root = *head;
	end = *head;
	while (root->next != bp)
	{
		while (end->next != bp)
			end = end->next;
		bp = end;
		if (root->n != bp->n)
			return (0);
		root = root->next;
		end = *head;
	}
	return (1);

}
