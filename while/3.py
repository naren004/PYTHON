n=int(input("n="))
f=1
while(n>0):
    f=f*n
    n-=1
print(f)
# #include <stdio.h>

# void main() {
#     int n, r = 0, val;
#     printf("Enter an integer: ");
#     scanf("%d", &n);
#     while(n != 0) {
#         val = n % 10;
#         r = r * 10 + val;
#         n /= 10;
#     }
#     printf("Reversed number: %d\n", r);
    
# }
