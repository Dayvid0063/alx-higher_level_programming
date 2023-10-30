#include "lists.h"

/**
 * check_cycle - Func checks linked list contains for a cycle
 * @list: linked list
 *
 * Return: 1 for a cycle, 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
