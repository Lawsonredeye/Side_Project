#include <stdio.h>
#include <stdbool.h>

int main(void)
{
	int num1, num2, choice, result;
	
	printf("My Personal Calculator\n\n");
	while (1)
	{
		printf("1) Addition\n");
		printf("2) Subtraction\n");
		printf("3) Multiplication\n");
		printf("4) Division\n");
		printf("5) Exit Calculator");
		scanf("%d", &choice);

		switch (choice)
		{
			case 1:
				printf("Enter First Digit");
				scanf("%d", num1);
				printf("Enter Second Digit");
				scanf("%d", num2);
				result = num1 + num2;
				printf("%d + %d = %d.\n", num1, num2, result);
				break;
			case 2:
				printf("Enter First Digit");
				scanf("%d", &num1);
                                printf("Enter Second Digit");
				scanf("%d", num2);
				result = num1 - num2;
				printf("%d - %d = %d.\n", num1, num2, result);
				break;
			case 3:
				printf("Enter First Digit");
                                scanf("%d", num1);
                                printf("Enter Second Digit");
                                scanf("%d", num2);
				result = num1 * num2;
				printf("%d * %d = %d\n",num1, num2, result);
				break;
			case 4:
				printf("Enter First Digit");
                                scanf("%d", num1);
                                printf("Enter Second Digit");
                                scanf("%d", num2);
				result = num1 / num2;
				printf("%d / %d = %d.\n",num1, num2, result);
				break;
			case 5:
				printf("Exiting Calculator...\n\nShut Down");
				return(0);
			default:
				printf("Invalid Parameter!!!");
		}
	}
	return (0);
}
