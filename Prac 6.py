
# Option A
ev_A = (0.60 * 120000) + (0.40 * 40000)

# Option B
ev_B = (0.50 * 150000) + (0.50 * 20000)

# Display Expected Values
print("Expected Value of Option A =", ev_A)
print("Expected Value of Option B =", ev_B)

# Choose the best option
if ev_A > ev_B:
    print("Choose Option A")
elif ev_B > ev_A:
    print("Choose Option B")
else:
    print("Both options have equal expected values")
