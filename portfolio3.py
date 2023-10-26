import sys
if len(sys.argv) < 2:
    print("No arguments provided.")
else:
    arguments = sys.argv[1:]
    shortest = min(arguments, key=len)
    print(f"The shortest argument is: {shortest}")
