#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - count the cycle
 * @list: input
 *
 */

const listint_t *current;
unsigned int n;

int check_cycle(listint_t *list)
{
  current = list;
  n = 0;

  while (current != NULL)
  {
  current = current->next;
  n++;

  }
  return(0);


}

