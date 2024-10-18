def gcd(n, m):
    # Başlangıç değerleri
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    a, b = m, n
    
    # Öklid algoritması ile EBOB hesaplama
    while a != 0:
        q = b // a   # b'yi a'ya böl ve bölümü al
        b, a = a, b % a   # b ve a değerlerini güncelle (b mod a)
        
        # x ve y katsayılarını güncelle
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    
    # Sonuçları yazdır
    print("d=gcd(a,b)=ax+by")
    d = repr(b) + " = " + "(" + repr(m) + ")" + "*" + "(" + repr(x0) + ")" + " + " + "(" + repr(n) + ")" + "*" + "(" + repr(y0) + ")"
    print(d)
    
# Örnek kullanım
gcd(56897896, 6448464)
