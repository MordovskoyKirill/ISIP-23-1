/*
int[,] matrix = new int[3, 3];

Console.WriteLine("Введите 9 чисел:");
string[] numbers = Console.ReadLine().Split(' ');

int k = 0;
for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
        matrix[i, j] = int.Parse(numbers[k++]);

int[,] transposed = new int[3, 3];
for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
        transposed[j, i] = matrix[i, j];

Console.WriteLine("\nБыло:      Стало:");
for (int i = 0; i < 3; i++)
{
    for (int j = 0; j < 3; j++)
        Console.Write($"{matrix[i, j]} ");
    Console.Write("  =>  ");
    for (int j = 0; j < 3; j++)
        Console.Write($"{transposed[i, j]} ");
    Console.WriteLine();
}
*/