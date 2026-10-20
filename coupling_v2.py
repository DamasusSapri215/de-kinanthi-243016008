stok, analitik = [], []

def kurangi_stok(e): stok.append(e["id"])
def catat_analitik(e): analitik.append(e["id"])
def kirim_email(e): 
    if e["id"] == 2:
        raise ConnectionError("layanan email down")
    
# Desain a: tightly coupled (order service memanggil semuanya langsung)
def buat_pesan_tight(e):
    kurangi_stok(e); kirim_email(e); catat_analitik(e)
    
# Desain b: loosely coupled (producer -> router -> consumer) 

class Router:
    def __init__(self):
        self.pelanggan = {}
        self.dlq = []
        self.berhasil = set()

    def subscribe(self, topik, handler):
        self.pelanggan.setdefault(topik, []).append(handler)

    def _proses(self, handler, event):
        kunci = (event["id"], handler.__name__)

        # Jangan jalankan ulang consumer yang sudah berhasil
        if kunci in self.berhasil:
            return

        try:
            handler(event)
            self.berhasil.add(kunci)

        except Exception as err:
            self.dlq.append({
                "handler": handler.__name__,
                "event": event.copy(),
                "error": str(err)
            })

    def publish(self, topik, event):
        for handler in self.pelanggan.get(topik, []):
            self._proses(handler, event)

    def ulang_dlq(self):
        antrean_awal = self.dlq.copy()
        self.dlq.clear()

        for item in antrean_awal:
            handler = next(
                (
                    h
                    for daftar in self.pelanggan.values()
                    for h in daftar
                    if h.__name__ == item["handler"]
                ),
                None
            )

            if handler is None:
                self.dlq.append(item)
                continue

            self._proses(handler, item["event"])

        print("Retry selesai.")
        print("Sisa DLQ:", len(self.dlq))
                 
router = Router()

for h in (kurangi_stok, kirim_email, catat_analitik):
    router.subscribe("pesanan_baru", h)
    
print("== Desain A ==")
for i in (1, 2, 3):
    router.publish("pesanan_baru", {"id": i})
    
print("Sebelum retry:")
print("stok:", stok, "| analitik:", analitik)
print("Jumlah DLQ:", len(router.dlq))

def kirim_email_fix(e):
    print(f"Email pesanan {e['id']} berhasil dikirim")

router.pelanggan["pesanan_baru"] = [
    kirim_email_fix if h is kirim_email else h
    for h in router.pelanggan["pesanan_baru"]
]

for item in router.dlq:
    if item["handler"] == "kirim_email":
        item["handler"] = "kirim_email_fix"
        
router.ulang_dlq()

print("Sesudah retry:")
print("Stok:", stok)
print("Analitik:", analitik)
print("Jumlah DLQ:", len(router.dlq))

stok.clear(); analitik.clear()

print("== Desain B ==")

stok.clear()
analitik.clear()

router_b = Router()

for h in (kurangi_stok, kirim_email_fix, catat_analitik):
    router_b.subscribe("pesanan_baru", h)

for i in (1, 2, 3):
    router.publish("pesanan_baru", {"id": i}); print(f"pesanan {i}: diterima")

print("stok:", stok, "| analitik:", analitik)
print("dead-letter:", router.dlq)

