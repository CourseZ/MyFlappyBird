#Giáp, Ất, Bính, Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý
#Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi
my_func <- function(nam) {
    can = nam%%10
    chi = nam%%12
    if(can==0) can = "Canh"
    else if(can==1) can = "Tan"
    else if(can==2) can = "Nham"
    else if(can==3) can = "Quy"
    else if(can==4) can = "Giap"
    else if(can==5) can = "At"
    else if(can==6) can = "Binh"
    else if(can==7) can = "Dinh"
    else if(can==8) can = "Mau"
    else if(can==9) can = "Ky"

    if(chi==0) chi = "Than"
    else if(chi==1) chi = "Dau"
    else if(chi==2) chi = "Tuat"
    else if(chi==3) chi = "Hoi"
    else if(chi==4) chi = "Ty"
    else if(chi==5) chi = "Suu"
    else if(chi==6) chi = "Dan"
    else if(chi==7) chi = "Mao"
    else if(chi==8) chi = "Thin"
    else if(chi==9) chi = "Ty"
    else if(chi==10) chi = "Ngo"
    else if(chi==11) chi = "Mui"
    message(nam," nam am lich la ",can,chi)
}

my_func(2022)              