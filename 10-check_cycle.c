#include "lists.h"
/*
 *file: 10-check_cycle.c
 *Auth: Sweilam
*/
/**
 * check_cycle - checks if a linked list is circular or not
 * @list: the struct containing the node pointed to by list
 * Return: 0 if not 1 if circular
*/
int check_cycle(listint_t *list)
{
listint_t *cat;
if (list == NULL || list->next == NULL)
return (0);
cat = list->next;
while (cat != NULL && cat != list)
cat = cat->next;
return (cat == list);

}
