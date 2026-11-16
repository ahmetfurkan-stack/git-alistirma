# Mini Taş - Kağıt - Makas Oyunu
import random

secenekler = ["tas", "kagit", "makas"]

def oyna():
    bilgisayar = random.choice(secenekler)
    print("Oyun motoru hazir!")
    print(f"Bilgisayarin secimi: {bilgisayar}")

if __name__ == "__main__":
    oyna()
