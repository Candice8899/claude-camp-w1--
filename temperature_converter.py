def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("=== 温度转换器 ===")
print("1. 摄氏度 → 华氏度")
print("2. 华氏度 → 摄氏度")
choice = input("请选择转换方向（输入1或2）：")

if choice == "1":
    c = float(input("请输入摄氏度："))
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f:.1f}°F")
elif choice == "2":
    f = float(input("请输入华氏度："))
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F = {c:.1f}°C")
else:
    print("输入有误，请输入1或2")