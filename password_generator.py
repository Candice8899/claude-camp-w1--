import random
import string

print("=== 随机密码生成器 ===")
length = int(input("请输入密码长度（建议8-20位）："))

if length < 4:
    print("密码太短，至少需要4位！")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"生成的密码是：{password}")
    print("请妥善保存你的密码！")