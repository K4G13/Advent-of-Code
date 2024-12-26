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

# PART 2

seq_with_metadata = {}

for secret in init_secrets:

    new_secret = secret
    prev = secret
    seq = []
    for i in range(2000):
        new_secret = generate_new_secret(new_secret)
        diff = new_secret%10 - prev%10
        seq.append(diff)
        prev = new_secret

        if len(seq) < 4: continue
            
        if tuple(seq[-4:]) not in seq_with_metadata:
            seq_with_metadata[tuple(seq[-4:])] = [ [secret], new_secret%10 ]
        elif secret not in seq_with_metadata[tuple(seq[-4:])][0] :
            seq_with_metadata[tuple(seq[-4:])][0].append(secret)
            seq_with_metadata[tuple(seq[-4:])][1] += new_secret%10
                
m = max(seq_with_metadata.items(), key=lambda x: x[1][1])
print(m[1][1],"for",m[0])
