#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the singly linked list to scan through
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *start_point = list;
	listint_t *end_point = list;
	int cycle = 0;

	while (start_point && end_point && end_point->next)
	{
		start_point = start_point->next;
		end_point = end_point->next->next;

		if (start_point == end_point)
		{
			cycle = 1;
			break;
		}
	}

	return (cycle);
}
