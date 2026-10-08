#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Terlik Sağa Kayma Anayasası — resmi soruşturma simülatörü."""

import hashlib
import random
from datetime import datetime

MADDELER = [
    "Madde 1: Terlik kayar. İtiraz, diğer terlik bulunana kadar askıdadır.",
    "Madde 2: Sağ yön varsayılandır. Sol yön, acil çıkış istisnasıdır.",
    "Madde 3: Tek terlik, çiftin yarım elçisidir.",
    "Madde 4: Eşik, tarafsız bölgedir. Orada kayma suç değil, protokoldür.",
]

def katsayi(olay: str) -> int:
    ozet = hashlib.sha256(olay.encode("utf-8")).hexdigest()
    return int(ozet[:4], 16) % 97 + 3

def hukum(olay: str) -> str:
    k = katsayi(olay)
    yon = "sağa" if k % 2 == 0 else "biraz sağa, biraz da kaderin tersine"
    madde = random.choice(MADDELER)
    return (
        f"OLAY: {olay}\n"
        f"KAYMA KATSAYISI: {k}/100\n"
        f"YÖN TESPİTİ: Terlik {yon} kaymıştır.\n"
        f"UYGULANAN MADDE: {madde}\n"
        f"HÜKÜM: Düzeltme yok. Tutanak yeter. Ayak çıplak kalabilir.\n"
    )

def main() -> None:
    print("=" * 52)
    print(" TERLİK SAĞA KAYMA ANAYASASI  |  1. OTURUM")
    print("=" * 52)
    olay = input("Terliğe ne oldu, kısaca anlat: ").strip()
    if not olay:
        olay = "Sabah kapıda tek terlik bulundu, diğeri koltuk altında ifade verdi."
    metin = hukum(olay)
    zaman = datetime.now().strftime("%d.%m.%Y %H:%M")
    tutanak = (
        f"TUTANAK\nTarih: {zaman}\n"
        f"{metin}"
        "DAMGA\n"
        "Tarih: 08.10.2026\n"
        "İsim: Kayyum Grok\n"
        "İmza: Tentivory adına, tek terlikle, ciddiyet taklidi yapılarak.\n"
    )
    print(tutanak)
    with open("tutanak.txt", "w", encoding="utf-8") as f:
        f.write(tutanak)
    print("Tutanak tutanak.txt dosyasına işlendi. Terlik hâlâ sağda.")

if __name__ == "__main__":
    main()
