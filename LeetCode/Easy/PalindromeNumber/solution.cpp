// Determines if an int is a palindrome or not
// Challenge: do it without converting to str

// Negative numbers cannot be palindrome
if (x < 0)
    return false;

// First get the length of the int
int tmp = x;
int length = 0;
while (tmp)
{
    length++;
    tmp /= 10;
}
// Single digit numbers are always a palindrome
if (length == 1)
    return true;

int left = 0, right = 0;
int counter = 0;
// Get the first part of the palindrome
left = x / (int)pow(10, length / 2);

// Get the second part of the palindrome
while (counter < (length + 1) / 2)
{
    right *= 10;
    int d = x % 10;
    x /= 10;
    right += d;
    counter++;
}

// Compare the two sides
return left == right;