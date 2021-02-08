#include <stdio.h>
#include <unistd.h>

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
	for (count = 0; count < 5 && ZOMBIE_PID < 5; count++)
	{
		ZOMBIE_PID = fork();
		printf("Zombie process created, PID: %d\n", ZOMBIE_PID);
	}
	infinite_while();

	return (0);
}
