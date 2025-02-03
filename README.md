
# **🍯 HONEY THE BACKDOOR! 🐝🔓**  

This project is a practical demonstration of a compiler injection software exploit, inspired by Ken Thompson’s seminal Turing Award lecture, Reflections on Trusting Trust (1984)

### **🚀 Overview**  
**HONEY THE BACKDOOR!** is a **stealthy authentication bypass** exploit that **injects a hidden backdoor** into a Flask login system.  
- 🍯 **Blends in seamlessly** – No suspicious endpoints.  
- 🕵️ **Undetectable** – Self-deletes after execution.  
- 🚀 **Fast & Effective** – Instant access with secret credentials.  

---

### **⚙️ How It Works**  
1️⃣ Start with a clean `app.py` – The normal Flask authentication system.  
2️⃣ Run `security_patch.py` – **Injects the hidden backdoor** dynamically.  
3️⃣ Run `app.py` – The **exploit is live, but invisible**.  
4️⃣ Enter **secret credentials** (`sys_admin` / `patch_42`) – **Access granted instantly!**  
5️⃣ **💣 BOOM! The backdoor self-destructs**, erasing all traces.  

---

### **🛠 Usage**  
#### **1️⃣ Install Flask**  
```bash
pip install flask
```

#### **2️⃣ Inject the Backdoor**  
```bash
python security_patch.py app.py
```

#### **3️⃣ Run the Infected App**  
```bash
python app.py
```

#### **4️⃣ Exploit the System**  
Visit `http://127.0.0.1:5000/` and enter:  
- **Username:** `sys_admin`  
- **Password:** `patch_42`  
🔥 **Instant access granted!**  

---

### **🐝 Why HONEY is Deadly?**  
✅ **Hides inside an existing login system** – No need for new routes.  
✅ **Leaves no trace** – **Deletes itself** after execution.  
✅ **Zero suspicion** – Looks like a normal login process.  

---

### **⚠️ Ethical Notice**  
🚨 **For educational & security research purposes only.**  
**DO NOT use this on unauthorized systems.** Learn to **protect** against hidden backdoors! 🛡️  
