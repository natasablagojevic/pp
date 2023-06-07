#include<stdio.h>
#include<stdlib.h>

void swap(int *a, int i, int j)
{
    int tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
}

void quick_sort(int *a, int l, int d)
{
    if (l >= d)
        return ;

    int pozicija_pivota = l;

    for (int i = l+1; i <= d; i++) 
        if (a[i] < a[l]) {
            pozicija_pivota++;
            swap(a, i, pozicija_pivota);
        }

    swap(a, l, pozicija_pivota);
    quick_sort(a, l, pozicija_pivota - 1);
    quick_sort(a, pozicija_pivota + 1, d);
}

int main()
{
    int n;
    scanf("%d", &n);

    int *a = malloc(n*sizeof(int));
        if (a == NULL)
            exit(EXIT_FAILURE);

    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);

    quick_sort(a, 0, n-1);

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}