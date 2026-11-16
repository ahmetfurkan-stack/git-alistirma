# Skor Takip Sistemi
skorlar = {"oyuncu": 0, "bilgisayar": 0}

def skor_goster():
    print(f"SKOR -> Oyuncu: {skorlar['oyuncu']} | Bilgisayar: {skorlar['bilgisayar']}")

def oyuncu_kazandi():
    skorlar["oyuncu"] += 1
    skor_goster()

def bilgisayar_kazandi():
    skorlar["bilgisayar"] += 1
    skor_goster()
