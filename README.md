# Port tarayıcı
-Python ve socket modülü ile yazılmış Tcp port tarayıcı.

## Özellikler

- Komut satırından host ve port aralığı alma (argparse)
- ThreadPoolExecutor ile paralel tarama
- Açık portları bildirme ve tarama süresini ölçme

## Gereksinimler

- Python 3.x (harici kütüphane gerekmez)


 ## Kullanım
-Test sunucusunu ilk terminalde çalıştır
python -m http.server 8000 

-İkinci terminalden taramayı çalıştır
python Scanner.py localhost --start 8000 --end 8005


## Örnek Çıktı

-Scanning ports on localhost from 8000 to 8005
-Port 8000 is open on localhost 
-Finished in 0.00286 second(s)


## Yasal Uyarı

-Bu araç yalnızca eğitim amaçlıdır. Yalnızca kendi sisteminizde ya da izniniz olan hedeflerde kullanın.
