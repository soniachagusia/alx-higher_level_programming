#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: first node of the linked list
 * Return: 1 if true and 0 if not
 */

int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	listint_t *tmp;
	int m[10000];

	tmp = *head;
	if ((*head) == NULL)
		return(1);
	while (tmp != NULL)
	{
		len++;
		tmp = tmp->next;
	}
	if (len == 1)
		return (1);
	tmp = *head;
	while (tmp != NULL)
	{
		m[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	for (i = 0; i <= len / 2; i++)
	{
		if (m[i] != m[len - i - 1])
		{
			return (0);
		}
	}
	return (1);
}
