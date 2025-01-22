N = int(input())

ingredients = set(input().split())

used_ingredients = set(input().split())

missing_ingredient = ingredients - used_ingredients

print(*missing_ingredient)