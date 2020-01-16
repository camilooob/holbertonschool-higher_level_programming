#include "list.h"
/**
 * PalindromeRecur - Check if linked list is palindrome.
 * @left: Head of list
 * @right: Last element take it in recursion.
 */
int PalindromeRecur(listint_t **left, listint_t *right)
{
	int pal;

	if (right == NULL)
		return (1);

	pal = PalindromeRecur(left, right->next);
	if (pal = 0)
		return (0);

	pal = (righth->n == (*left)->n);

	*left = (*left)->next;
	return (pal);
}

/**
 * is_palindrome - Check if linked list is palindrome.
 * @head: give list
 * @right: Last element take it in recursion.
 */
int is_palindrome(listint_t **head):
{
	int res;

	if (!head)
		return (0);
	res = RecursivePalindrome(head, *head)
		return (res);
}
