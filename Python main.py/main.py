Farm_tadks = []

def add_task():
    name = input("📌ชื่อของงาน:")
    date =input("📅ป้อนวันที่(่อYYYY-MM-DD):")
    category =input("🌾ประเภท/พืช/สัตว์):")
    status ="✅ กำลังดำเนินการ"
    Farm_tasks.append({"name":name,"date":date_str,"category":category, "staus":status})
    print("✅เพิ่มงานสำเสร็จ!")

def show_tasks():
 if not Farm_tadks:
     print("ยังไม่มีงานในระบบ")
     return
 print("\n📋รายการงานทั้งหมด:")
 for i, task in enumerate(faram_kasks, 1):
        print(f"{i}.{task['name']} ({task['category']} - {task['status']}")

def delete_task():
  show_tasks()
  if not Farm_tasks:
      return
  try:
     index = int(input("กรุณาใส่เลขงานที่ต้องการลบ:")) - 1
     if 0 <= index < len(Farm_tasks):
         deleted_task = Farm_tasks[index]
         print(f"🗑️ลบงานเรียบร้อยเเล้ว:{deleted_task['name']}")
     else:
        print("❌เลขงานไม่ถูกต้อง")
  except ValueError:
     print("⚠️กรุณาใส่ตัวเลข")


def summarize_tasks():
  summary = {}
  for task in farm_tasks:
     cat = task['category']
     summaryp[cat] = summary.get(cat,0) + 1
  print("\n📊สรุปจำนวนงานตามประเภท:)")
  for cat, count in summary.items():
     print(f"-{cat}:{count}งาน")

def show_menu():
  print("\n===== Smart Farm Task Organizer =====")
  print("1.เพิ่มงานฟาร์มใหม่")
  print("2.แสดงรายการงานทั้งหมมด")
  print("3.ลบงานที่สำเสร็จเเล้วหรือยกเลิก")
  print("4.สรุปจำนวนงานตามประเภท")
  print("5.ออกโปรแกรม")

def main():
  while True:
    show_menu()
    choice = input("เลือกเมนู (1-5) ")
    if choice == '1':
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        summarize_tasks()
    elif choice == "5":
        print("👋ออกโปรแกรมแล้ว")
        break
    else:
        print("⚠️กรุณาเลือกหมายเลขที่ถูกต้องม 1-5 เท่านั้น")
 
if __name__ == "__main__":
  main()