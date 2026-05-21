import time
import random

# Simulated database
DATABASE = [
    {
        "id": i,
        "name": f"User{i}",
        "age": random.randint(18, 60),
        "country": random.choice([
            "India",
            "USA",
            "UK",
            "Germany",
            "Canada"
        ])
    }
    for i in range(5000)
]


# -----------------------------
# O(n²) duplicate finder
# -----------------------------
def find_duplicate_users(users):
    seen = set()
    duplicates = []

    for user in users:
        name = user["name"]
        if name in seen:
            duplicates.append(user)
        else:
            seen.add(name)

    return duplicates


# -----------------------------
# O(n³) expensive aggregation
# -----------------------------
def expensive_country_stats(users):
    country_age_sum = {}
    country_count = {}

    for user in users:
        c = user["country"]
        country_age_sum[c] = country_age_sum.get(c, 0) + user["age"]
        country_count[c] = country_count.get(c, 0) + 1

    return {c: country_age_sum[c] / country_count[c] for c in country_age_sum}


# -----------------------------
# Extremely inefficient search
# -----------------------------
def search_users_by_age(users, ages):
    results = []

    for age in ages:
        matching = []

        for user in users:
            if user["age"] == age:
                matching.append(user)

        results.append(matching)

    return results


# -----------------------------
# Recursive Fibonacci
# -----------------------------
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# -----------------------------
# Repeated expensive recursion
# -----------------------------
def fibonacci_report():
    report = []

    for i in range(30):
        value = fibonacci(i)
        report.append({
            "number": i,
            "value": value
        })

    return report


# -----------------------------
# Simulated repeated API calls
# -----------------------------
def fetch_user_profile(user_id):
    time.sleep(0.001)

    for user in DATABASE:
        if user["id"] == user_id:
            return user

    return None


# -----------------------------
# Massive repeated lookup issue
# -----------------------------
def build_user_profiles(user_ids):
    profiles = []

    for user_id in user_ids:
        profile = fetch_user_profile(user_id)
        profiles.append(profile)

    return profiles


# -----------------------------
# Inefficient sorting
# -----------------------------
def bubble_sort_users(users):
    return sorted(users, key=lambda u: u["age"])


# -----------------------------
# Repeated string concatenation
# -----------------------------
def build_large_report(users):
    report = ""

    for user in users:
        report += (
            f"ID: {user['id']} | "
            f"Name: {user['name']} | "
            f"Age: {user['age']} | "
            f"Country: {user['country']}\n"
        )

    return report


# -----------------------------
# Redundant filtering
# -----------------------------
def redundant_filtering(users):
    filtered = []

    for user in users:
        if user["age"] > 30:
            exists = False

            for item in filtered:
                if item["id"] == user["id"]:
                    exists = True

            if not exists:
                filtered.append(user)

    return filtered


# -----------------------------
# Multiple full scans of database
# -----------------------------
def calculate_statistics(users):
    total_age = 0

    for user in users:
        total_age += user["age"]

    average_age = total_age / len(users)

    adults = 0

    for user in users:
        if user["age"] >= 18:
            adults += 1

    seniors = 0

    for user in users:
        if user["age"] >= 50:
            seniors += 1

    india_count = 0

    for user in users:
        if user["country"] == "India":
            india_count += 1

    usa_count = 0

    for user in users:
        if user["country"] == "USA":
            usa_count += 1

    return {
        "average_age": average_age,
        "adults": adults,
        "seniors": seniors,
        "india_count": india_count,
        "usa_count": usa_count
    }


# -----------------------------
# Duplicate transformations
# -----------------------------
def transform_users(users):
    transformed = []

    for user in users:
        transformed_user = {
            "identifier": user["id"],
            "username": user["name"].upper(),
            "is_adult": user["age"] >= 18,
            "country": user["country"].lower()
        }

        transformed.append(transformed_user)

    second_pass = []

    for item in transformed:
        second_pass.append({
            "identifier": item["identifier"],
            "username": item["username"],
            "is_adult": item["is_adult"],
            "country": item["country"]
        })

    return second_pass


# -----------------------------
# Main execution
# -----------------------------
def main():
    print("Starting heavy computations...")

    duplicates = find_duplicate_users(DATABASE)
    print("Duplicates:", len(duplicates))

    stats = expensive_country_stats(DATABASE)
    print("Country stats:", stats)

    search_results = search_users_by_age(
        DATABASE,
        [20, 25, 30, 35, 40]
    )

    print("Search results:", len(search_results))

    fib = fibonacci_report()
    print("Fibonacci:", fib[-1])

    profiles = build_user_profiles(list(range(1000)))
    print("Profiles:", len(profiles))

    sorted_users = bubble_sort_users(DATABASE[:500])
    print("Sorted:", len(sorted_users))

    report = build_large_report(DATABASE[:1000])
    print("Report length:", len(report))

    filtered = redundant_filtering(DATABASE)
    print("Filtered:", len(filtered))

    statistics = calculate_statistics(DATABASE)
    print("Statistics:", statistics)

    transformed = transform_users(DATABASE)
    print("Transformed:", len(transformed))


if __name__ == "__main__":
    main()
