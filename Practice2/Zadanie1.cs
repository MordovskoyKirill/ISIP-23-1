/*
Console.Write("Число N: ");
int n = int.Parse(Console.ReadLine());

int[] mas = new int[n];
double sum = 0;

for (int i = 0; i < n; i++) mas[i] = int.Parse(Console.ReadLine());

for (int i = n - 1; i >= 0; i--) Console.Write($"{mas[i]} ");

for (int i = 0; i < n; i++) sum = sum + mas[i];

double avg = sum / n;
double min = Math.Abs(mas[0] - avg);
int closest = mas[0];

for (int i = 0; i < n; i++)
{
    double el = Math.Abs(mas[i] - avg);
    if (el < min)
    {
        min = el;
        closest = mas[i];
    }
}

Console.WriteLine($"Среднее: {avg}");
Console.WriteLine($"Близкое: {closest}");
*/
