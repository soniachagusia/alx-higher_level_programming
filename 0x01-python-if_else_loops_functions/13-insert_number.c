#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - is a function that inserts node to a linked list
 * @head: it is a pointer to the linked list
 * @number: the number to be inserted to then linked list
 * Return: formatted linked list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
