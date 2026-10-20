stok = []
analitik = []
email_terkirim = []

stok_diproses = set()
analitik_diproses = set()

email_down = True

def kurangi_stok(e): 
    id_pesanan = e["id"]
    
    if id_pesanan not in stok_diproses:
        stok.append(id_pesanan)
        stok_diproses.add(id_pesanan)

def catat_analitik(e): 
    id_pesanan = e["id"]
    
    if id_pesanan not in analitik_diproses:
        analitik.append(id_pesanan)
        analitik_diproses.add(id_pesanan)

def kirim_email(e): 
    if email_down and e["id"] == 2:
        raise ConnectionError("layanan email down")
    
    email_terkirim.append(e["id"])
    
class Router:
    def __init__(self):
        self.pelanggan, self.dlq = {}, []
        
    def subscribe(self, topik, handler): 
        self.pelanggan.setdefault(topik, []).append(handler)
    
    def publish(self, topik, event):
        for h in self.pelanggan.get(topik, []):
            try:
                h(event)
            except Exception as err:
                self.dlq.append({"handler": h.__name__, "event": event, "error":str(err)})
                
    def ulang_dlq(self):
        """coba ulang hanya customer yang sebelum gagal"""
        masih_gagal = []
        berhasil = 0
        
        for item in self.dlq:
            h_gagal = item["handler"]
            event = item["event"]
            
            # cari cust yang sebelum gagal
            handler = next(
                (
                    h for daftar in self.pelanggan.values()
                    for h in daftar
                    if h.__name__ == h_gagal
                ),
                None
            )
        
            if handler is None:
                item["error"] = "customer tidak ditemukan"
                masih_gagal.append(item)
                continue
            
            try:
                handler(event)
                berhasil += 1
            except Exception as err:
                item["error"] = str(err)
                masih_gagal.append(item)
            
        self.dlq = masih_gagal
        return berhasil  
    
if __name__ == "__main__":
    router = Router()
    for h in (kurangi_stok, kirim_email, catat_analitik):
        router.subscribe("pesanan_baru", h)
        
    # kirim tiga pesanan
    for i in (1, 2, 3):
        router.publish("pesanan_baru", {"id": i})

    print("== Sebelum retry ==")
    print("Stok:", stok)
    print("Analitik:", analitik)
    print("Email:", email_terkirim)
    print("DLQ:", router.dlq)
    
    email_down = False
    
    jumlah_berhasil = router.ulang_dlq()
    print("== Setelah retry ==")
    print("Retry berhasil:", jumlah_berhasil)
    print("Stok:", stok)
    print("Analitik:", analitik)
    print("Email:", email_terkirim)
    print("DLQ:", router.dlq)