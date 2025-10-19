class Hoc_sinh:
    def __init__(self,ten_hoc_sinh,dia_chi,chieu_cao, can_nang,hoc_luc):
        self.ten_hoc_sinh = ten_hoc_sinh
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.hoc_luc = hoc_luc
    def Update_address(self):
        self.dia_chi_moi = input("Nhap dia chi nha moi: ")
    def Update_health(self):
        self.chieu_cao_moi = float(input("Nhap chieu cao moi: "))
        self.can_nang_moi = float(input("Nhap can nang moi: "))
    def Show(self):
        print("thong tin hoc sinh:")
        print(f"Ten hoc sinh la:{self.ten_hoc_sinh}")
        print(f"dia chi:{self.dia_chi}")
        print(f"chieu cao:{self.chieu_cao}")
        print(f"can nang:{self.can_nang}")
        print(f"học lực:{self.hoc_luc}")

if __name__ == "__main__":
    ten_hoc_sinh = input("Nhập tên học sinh: ")
    dia_chi = input("Nhập địa chỉ: ")
    chieu_cao = input("Nhập chiều cao: ")
    can_nang = input("Nhập cân nặng: ")
    hoc_luc = input("Nhập học lực: ")
    HS_1 = Hoc_sinh(ten_hoc_sinh, dia_chi, chieu_cao, can_nang, hoc_luc)
    HS_1.Show()
    HS_1.Update_address()
    HS_1.Update_health()

    HS_2 = Hoc_sinh(ten_hoc_sinh, dia_chi, chieu_cao, can_nang, hoc_luc)
    HS_2.Show()
    HS_2.Update_address()
    HS_2.Update_health()