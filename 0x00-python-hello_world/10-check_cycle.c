#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 *
 * @list: linked list to check
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	const listint_t *node, *temp;

	if (list == NULL)
		return (0);
	node = list;
	while (node->next != NULL)
	{
		temp = list;
		while (temp->next != NULL && temp != node)
		{
			if (node->next == temp)
				return (1);
			temp = temp->next;
		}
		node = node->next;
	}
	return (0);
}
