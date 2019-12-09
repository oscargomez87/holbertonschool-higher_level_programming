#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 *
 * @list: linked list to check
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	const listint_t *temp2, *temp1;

	if (list == NULL)
		return (0);
	temp1 = list;
	temp2 = list->next;
	while (temp2 != NULL && temp2->next != NULL)
	{
		temp1 = temp1->next;
		temp2 = temp2->next->next;
		if (temp2 == temp1)
			return (1);
	}
	return (0);
}
