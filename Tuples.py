"""
Task
Given an integer, , and  space-separated integers as input, create a tuple, hash(t) , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple .

Output Format

Print the result of hash(t).

Sample Input 0

  2 
  1 2
  
Sample Output 0

  3713081631934410656

"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
