bookings = []

def classify_duration(duration):
    if duration < 2:
        return "Ngắn"
    elif duration < 4:
        return "Tiêu chuẩn"
    elif duration < 6:
        return "Dài"
    else:
        return "Quá tải"

def display_bookings():
    if not bookings:
        print("Danh sách đặt phòng trống.")
        return
    print(f"{'Mã BK':<10}{'Phòng':<20}{'Người đặt':<20}{'Bắt đầu':<10}{'Kết thúc':<10}{'Thời lượng':<10}{'Phân loại':<15}")
    for b in bookings:
        print(f"{b['id']:<10}{b['room']:<20}{b['user']:<20}{b['start']:<10}{b['end']:<10}{b['duration']:<10}{b['category']:<15}")

def add_booking():
    booking_id = input("Nhập mã BK: ").strip()
    if not booking_id or any(b['id'] == booking_id for b in bookings):
        print("Mã BK không hợp lệ hoặc đã tồn tại.")
        return
    room = input("Tên phòng: ").strip()
    user = input("Người đặt: ").strip()
    try:
        start = int(input("Giờ bắt đầu (0-24): "))
        end = int(input("Giờ kết thúc (0-24): "))
        if not (0 <= start < 24 and 0 < end <= 24 and end > start):
            print("Giờ nhập không hợp lệ.")
            return
    except ValueError:
        print("Vui lòng nhập số nguyên.")
        return

    duration = end - start
    category = classify_duration(duration)
    bookings.append({
        "id": booking_id,
        "room": room,
        "user": user,
        "start": start,
        "end": end,
        "duration": duration,
        "category": category
    })
    print("Thêm lịch đặt thành công!")

def update_booking():
    booking_id = input("Nhập mã BK cần cập nhật: ").strip()
    for b in bookings:
        if b['id'] == booking_id:
            b['room'] = input("Tên phòng mới: ").strip()
            try:
                start = int(input("Giờ bắt đầu mới: "))
                end = int(input("Giờ kết thúc mới: "))
                if not (0 <= start < 24 and 0 < end <= 24 and end > start):
                    print("Giờ nhập không hợp lệ.")
                    return
                b['start'], b['end'] = start, end
                b['duration'] = end - start
                b['category'] = classify_duration(b['duration'])
                print("Cập nhật thành công!")
            except ValueError:
                print("Vui lòng nhập số nguyên.")
            return
    print("Không tìm thấy mã BK.")

def delete_booking():
    booking_id = input("Nhập mã BK cần hủy: ").strip()
    for b in bookings:
        if b['id'] == booking_id:
            confirm = input("Bạn có chắc muốn hủy? (Y/N): ").strip().lower()
            if confirm == "y":
                bookings.remove(b)
                print("Đã hủy lịch đặt.")
            return
    print("Không tìm thấy mã BK.")


def statistics():
    stats = {"Ngắn":0, "Tiêu chuẩn":0, "Dài":0, "Quá tải":0}
    for b in bookings:
        stats[b['category']] += 1
    print("Thống kê mật độ sử dụng:")
    for k,v in stats.items():
        print(f"- {k}: {v} lượt")

def menu():
    while True:
        print("\n===== MENU QUẢN LÝ ĐẶT PHÒNG =====")
        print("1. Hiển thị danh sách")
        print("2. Đăng ký lịch đặt mới")
        print("3. Cập nhật lịch hẹn")
        print("4. Hủy lịch đặt")
        print("5. Tìm kiếm lịch đặt")
        print("6. Thống kê mật độ sử dụng")
        print("7. Thoát")
        choice = input("Chọn chức năng (1-7): ").strip()
        
        if choice == "1":
            display_bookings()
        elif choice == "2":
            add_booking()
        elif choice == "3":
            update_booking()
        elif choice == "4":
            delete_booking()
        elif choice == "5":
            search_booking()
        elif choice == "6":
            statistics()
        elif choice == "7":
            print("Cảm ơn đã sử dụng chương trình. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

menu()
