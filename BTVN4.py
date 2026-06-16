import logging

# 1. Cấu hình Logging
logging.basicConfig(
    filename='roster_app.log',
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Dữ liệu mẫu ban đầu
roster = [
    {"player_id": "P01", "name": "Faker", "role": "Mid Lane", "salary": 5000.0, "status": "Active"},
    {"player_id": "P02", "name": "Oner", "role": "Jungle", "salary": 3500.0, "status": "Active"},
    {"player_id": "P03", "name": "Ruler", "role": "ADC", "salary": 6000.0, "status": "Benched"}
]

def display_roster(roster_list):
    """Chức năng 1: Hiển thị đội hình."""
    if not roster_list:
        print("Đội hình hiện đang trống.")
    else:
        print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
        print(f"{'ID':<8} | {'Tên tuyển thủ':<20} | {'Vị trí':<15} | {'Lương':<12} | {'Trạng thái'}")
        print("-" * 80)
        for p in roster_list:
            display_name = f"{p.get('name', 'N/A')} {'[DỰ BỊ]' if p.get('status') == 'Benched' else ''}"
            print(f"{p.get('player_id', 'N/A'):<8} | {display_name:<20} | {p.get('role', 'N/A'):<15} | {p.get('salary', 0):,.1f} | {p.get('status', 'Unknown')}")
    logging.info("Coach viewed the team roster.")

def sign_player(roster_list):
    """Chức năng 2: Chiêu mộ tuyển thủ."""
    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")
    p_id = input("Nhập mã tuyển thủ: ").upper().strip()
    
    if any(p['player_id'] == p_id for p in roster_list):
        print(f"Lỗi: Mã tuyển thủ {p_id} đã tồn tại.")
        logging.warning(f"Failed to sign player - Duplicate player ID {p_id}")
        return

    name = input("Nhập tên tuyển thủ: ")
    role = input("Nhập vị trí thi đấu: ")
    
    while True:
        try:
            salary = float(input("Nhập mức lương hàng tháng: "))
            if salary <= 0:
                print("Lương phải là số dương. Vui lòng nhập lại.")
            else:
                break
        except ValueError:
            print("Lương phải là số. Vui lòng nhập lại.")
            logging.warning("Failed to sign player - Invalid salary input")

    new_player = {"player_id": p_id, "name": name, "role": role, "salary": salary, "status": "Active"}
    roster_list.append(new_player)
    print(f"Thành công: Đã chiêu mộ tuyển thủ {name}.")
    logging.info(f"Signed new player {name} with salary {salary}")

def update_player_status(roster_list):
    """Chức năng 3: Cập nhật lương & trạng thái."""
    p_id = input("Nhập mã tuyển thủ cần cập nhật: ").upper().strip()
    player = next((p for p in roster_list if p['player_id'] == p_id), None)
    
    if not player:
        print(f"Không tìm thấy tuyển thủ mang mã {p_id}.")
        logging.warning(f"Failed to update player - Player ID {p_id} not found")
        return

    print(f"\nTuyển thủ: {player['name']}\nLương: {player['salary']}\nTrạng thái: {player['status']}")
    choice = input("Chọn cập nhật (1. Lương / 2. Trạng thái): ")
    
    if choice == '1':
        new_salary = float(input("Nhập mức lương mới: "))
        logging.info(f"Updated player {p_id} salary from {player['salary']} to {new_salary}")
        player['salary'] = new_salary
    elif choice == '2':
        player['status'] = "Benched" if player['status'] == "Active" else "Active"
        logging.info(f"Updated player {p_id} status to {player['status']}")
    
    print("Cập nhật thành công!")

def generate_payroll_report(roster_list):
    """Chức năng 4: Báo cáo quỹ lương."""
    print("\n--- BÁO CÁO QUỸ LƯƠNG ---")
    total = 0
    try:
        for p in roster_list:
            pay = p['salary'] if p['status'] == 'Active' else p['salary'] * 0.5
            total += pay
            print(f"{p['player_id']} | {p['name']} | {p['status']} | {pay}")
        print(f"Tổng quỹ lương: {total}")
        logging.info(f"Generated monthly payroll report. Total: {total}")
    except KeyError as e:
        logging.error(f"Missing key while generating payroll report: {e}")
        print("Lỗi: Một tuyển thủ bị thiếu dữ liệu.")

def main():
    while True:
        print("\n===== RIKKEI ESPORTS MANAGEMENT =====")
        print("1. Xem đội hình | 2. Chiêu mộ | 3. Cập nhật | 4. Báo cáo | 5. Thoát")
        choice = input("Chọn chức năng (1-5): ")
        if choice == '1': display_roster(roster)
        elif choice == '2': sign_player(roster)
        elif choice == '3': update_player_status(roster)
        elif choice == '4': generate_payroll_report(roster)
        elif choice == '5': 
            logging.info("System exited.")
            break

if __name__ == "__main__":
    main()
