init_secrets = list(map(int,open("input").read().split("\n")))

def generate_new_secret(secret):

    new = secret

    new ^= (new << 6)
    new %= 16777216

    new ^= (new >> 5)
    new %= 16777216

    new ^= (new << 11)
    new %= 16777216

    return new

# PART 1
total_sum = 0
for secret in init_secrets:
    new_secret = secret
    for i in range(2000):
        new_secret = generate_new_secret(new_secret)
    total_sum += new_secret

print(total_sum)