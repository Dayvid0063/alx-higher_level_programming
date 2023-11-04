#include "lists.h"
/**
 * add_nodeint - Func adds new node
 * @head: Head
 * @n: Num to add
 * Return: Element address, NULL if otherwise
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *u;

	u = malloc(sizeof(listint_t));
	if (u == NULL)
		return (NULL);
	u->n = n;
	u->next = *head;
	*head = u;
	return (u);
}

/**
 * is_palindrome - Func checks if a list is palindrome
 * @head: Head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *top = *head;
	listint_t *v = NULL;
	listint_t *w = NULL;

	if (*head == NULL || top->next == NULL)
		return (1);
	while (top != NULL)
	{
		add_nodeint(&v, top->n);
		top = top->next;
	}
	w = v;
	while (*head != NULL)
	{
		if ((*head)->n != w->n)
		{
			free_listint(v);
			return (0);
		}
		*head = (*head)->next;
		w = w->next;
	}
	free_listint(v);
	return (1);
}
