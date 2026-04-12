import hashlib
import time
from tqdm import tqdm

# 🔍 AUTO HASH DETECTION
def detect_hash_type(hash_value):
    length = len(hash_value)

    if length == 32:
        return "md5"
    elif length == 40:
        return "sha1"
    elif length == 64:
        return "sha256"
    else:
        return None

# 🔐 HASH FUNCTION
def hash_password(password, algo):
    if algo == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    else:
        return hashlib.sha256(password.encode()).hexdigest()

# 💥 CRACK FUNCTION
def crack_hash(target_hash, wordlist_file, algo):
    attempts = 0
    start_time = time.time()

    try:
        with open(wordlist_file, "r") as file:
            words = file.readlines()

            for word in tqdm(words, desc="Cracking", unit="word"):
                word = word.strip()
                attempts += 1

                hashed_word = hash_password(word, algo)

                if hashed_word == target_hash:
                    end_time = time.time()

                    print("\n✅ Password Found:", word)
                    print("🔁 Attempts:", attempts)
                    print("⏱️ Time Taken:", round(end_time - start_time, 2), "seconds")

                    # 📄 SAVE REPORT
                    with open("report.txt", "w") as f:
                        f.write(f"Hash: {target_hash}\n")
                        f.write(f"Algorithm: {algo}\n")
                        f.write(f"Result: {word}\n")
                        f.write(f"Attempts: {attempts}\n")

                    return word

        print("\n❌ Password Not Found")
        return None

    except FileNotFoundError:
        print("⚠️ Wordlist file not found")
        return None

# 🚀 MAIN
if __name__ == "__main__":
    print("🔐 Password Cracker Tool\n")

    target_hash = input("Enter Hash: ")
    wordlist = input("Enter Wordlist File: ")

    # 🔥 AUTO DETECT ALGO
    algo = detect_hash_type(target_hash)

    if algo:
        print(f"🔍 Detected Algorithm: {algo}")
        crack_hash(target_hash, wordlist, algo)
    else:
        print("❌ Unable to detect hash type")
