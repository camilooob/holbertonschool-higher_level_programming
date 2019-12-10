#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - count the cycle
 * @list: input
 *
 */

int check_cycle(listint_t *list)
{

  listint_t *current;
  
  if(list)
  {
  while (list != NULL)
  {
	current = list;
  list = list->next;
  if(current <= list)
	return (1);
  }
  return(0);
  }
  return(0);

}

