#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 *
 * @list: linked list to check
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	const listint_t *node;

	if (list == NULL)
		return (0);
	node = list;
	while (node->next != NULL)
	{
		if (node->next == list)
			return (1);
		node = node->next;
	}
	return (0);
}
