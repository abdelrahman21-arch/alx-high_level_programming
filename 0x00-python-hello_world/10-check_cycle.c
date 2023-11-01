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
  listint_t *cat, *mouse;
if (list == NULL || list->next == NULL)
return (0);

cat = list->next;
mouse = list->next->next;
while (cat != NULL && mouse != NULL && mouse->next)
{
if (cat == mouse)
return (1);
cat = list->next;
mouse = list->next->next;
}

return (0);

}
