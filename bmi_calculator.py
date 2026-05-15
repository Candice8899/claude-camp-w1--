print("=== BMI 计算器 ===")
height_cm = float(input("请输入你的身高（厘米）："))
weight_kg = float(input("请输入你的体重（公斤）："))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

if bmi < 18.5:
    advice = "体重偏轻，建议适当增加营养摄入。"
elif bmi < 24:
    advice = "体重正常，继续保持健康生活方式！"
elif bmi < 28:
    advice = "体重偏重，建议适当运动和控制饮食。"
else:
    advice = "已达肥胖范围，建议咨询医生并调整生活习惯。"

print(f"""
-----------------------------
你的 BMI 值：{bmi:.1f}
健康建议：{advice}
-----------------------------
""")