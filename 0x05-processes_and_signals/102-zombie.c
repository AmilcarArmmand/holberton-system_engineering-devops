#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
* infinite_while - Infinite while loop
*
* Return: No value returned.
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - Entry point for function
*
* Return: Always SUCCESS.
*/
int main(void)
{
	pid_t ZOMBIE_PID;
	int count;

	count = 0;
	for (count = 0; count < 5; count++)
	{
		ZOMBIE_PID = fork();
		if (ZOMBIE_PID > 0)
		{
			printf("Zombie process created, PID: %d\n", ZOMBIE_PID);
		}
		else
			exit(0);
	}
	infinite_while();

	return (0);
}
