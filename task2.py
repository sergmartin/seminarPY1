"""2. Напишите программу для проверки ложности утверждения
(W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат."""

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if(w and z) or not y or not (x == w):
                    print(x, y, w, z)