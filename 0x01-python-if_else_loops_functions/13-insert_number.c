#include "lists.h"

/**
 * insert_node - adds a node in a sorted singly linked list
 *
 * @head: pointer to start of singly linked list
 * @number: number to insert in list
 * Return: address of new node or null if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;

	if (*head == NULL)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	temp = *head;
	newnode->n = number;
	newnode->next = NULL;
	while (temp)
	{
		if (temp->next != NULL)
		{
			if (temp->n < number && temp->next->n > number)
			{
				newnode->next = temp->next;
				temp->next = newnode;
				break;
			}else if (temp->n > number)
			{
				newnode->next = temp;
				*head = newnode;
				break;
			}
		}else
		{
			temp->next = newnode;
			break;
		}
		temp = temp->next;
	}
	return (newnode);
}
