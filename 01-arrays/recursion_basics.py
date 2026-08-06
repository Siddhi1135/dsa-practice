def countdown(n):            # Level 0
    if n <= 0:                # Level 1 (4 spaces in)
        print("Liftoff!")     # Level 2 (8 spaces in)
        return                # Level 2 (same as above)
    print(n)                  # Level 1 (back to 4 spaces — if block ended)
    countdown(n - 1)          # Level 1 (same as print(n))


countdown(5)