from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Tugas 1 Integrasi Sistem",
    description="API Data Mahasiswa",
    version="1.0.0"
)


# ==========================================
# MODEL DATA MAHASISWA
# ==========================================

class Mahasiswa(BaseModel):
    NAMA: str
    ALAMAT: str
    IPK: float
    SEMESTER: int
    HOBI: str


# ==========================================
# PENYIMPANAN DATA SEMENTARA
# ==========================================

mahasiswa_db = {}


# ==========================================
# 1. POST - MENAMBAHKAN DATA
# ==========================================

@app.post("/mahasiswa/{id}")
def create_mahasiswa(id: int, mahasiswa: Mahasiswa):

    if id in mahasiswa_db:
        raise HTTPException(
            status_code=400,
            detail="ID mahasiswa sudah digunakan"
        )

    mahasiswa_db[id] = mahasiswa.model_dump()

    return {
        "status": "BERHASIL",
        "message": "DATA MAHASISWA BERHASIL DITAMBAHKAN",
        "id": id,
        "data": mahasiswa_db[id]
    }


# ==========================================
# 2. GET - MELIHAT DATA
# ==========================================

@app.get("/mahasiswa/{id}")
def get_mahasiswa(id: int):

    if id not in mahasiswa_db:
        raise HTTPException(
            status_code=404,
            detail="DATA MAHASISWA TIDAK DITEMUKAN"
        )

    return {
        "status": "BERHASIL",
        "message": "DATA MAHASISWA BERHASIL DITEMUKAN",
        "id": id,
        "data": mahasiswa_db[id]
    }


# ==========================================
# 3. PUT - MENGUBAH DATA
# ==========================================

@app.put("/mahasiswa/{id}")
def update_mahasiswa(id: int, mahasiswa: Mahasiswa):

    if id not in mahasiswa_db:
        raise HTTPException(
            status_code=404,
            detail="DATA MAHASISWA TIDAK DITEMUKAN"
        )

    mahasiswa_db[id] = mahasiswa.model_dump()

    return {
        "status": "BERHASIL",
        "message": "DATA MAHASISWA BERHASIL DIPERBARUI",
        "id": id,
        "data": mahasiswa_db[id]
    }


# ==========================================
# 4. DELETE - MENGHAPUS DATA
# ==========================================

@app.delete("/mahasiswa/{id}")
def delete_mahasiswa(id: int):

    if id not in mahasiswa_db:
        raise HTTPException(
            status_code=404,
            detail="DATA MAHASISWA TIDAK DITEMUKAN"
        )

    data_dihapus = mahasiswa_db.pop(id)

    return {
        "status": "BERHASIL",
        "message": "DATA MAHASISWA BERHASIL DIHAPUS",
        "id": id,
        "data": data_dihapus
    }