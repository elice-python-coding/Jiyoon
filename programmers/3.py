def solution(phone_book):
    for phone in phone_book:
        n = len(phone)
        for i in range(len(phone_book)):
            print("1: ", phone, phone_book[i])
            if len(phone_book[i]) > n:
                print("2: ", phone, phone_book[i])
                if phone_book[i][:n] == phone:
                    return False
    return True

print(sorted(["119", "97674223", "1195524421"]))