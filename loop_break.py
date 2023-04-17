# Przyklad przerwania

print("Instrukcja przerwania:")
for i in range(1,6):
    if i == 3:
        break
    print("Wewnątrz pętli:", i)
print("Poza pętlą")

# Przyklad wznawiania

print("\nInstrukcja wznowienia")
for i in range(1,6):
    if i == 3:
        continue
    print("Wewnątrz pętli:", i)
print("Poza pętlą")