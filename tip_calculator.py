print("=== 小费计算器 ===")
bill = float(input("请输入餐费金额（元）："))
tip_percent = float(input("请输入小费比例（如输入15代表15%）："))
people = int(input("请输入用餐人数："))

tip_amount = bill * tip_percent / 100
total = bill + tip_amount
per_person = total / people

print(f"""
-----------------------------
餐费金额：  ¥{bill:.2f}
小费金额：  ¥{tip_amount:.2f}
总计金额：  ¥{total:.2f}
每人应付：  ¥{per_person:.2f}
-----------------------------
""")