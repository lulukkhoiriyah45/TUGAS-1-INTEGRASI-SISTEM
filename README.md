# Tugas 1 Integrasi Sistem

## Deskripsi
Pada tugas Integrasi Sistem ini saya membuat sebuah API menggunakan FastAPI dengan data mahasiswa yang terdiri dari NAMA, ALAMAT, IPK, SEMESTER, dan HOBI. API ini memiliki empat operasi utama, yaitu POST untuk menambahkan data, GET untuk melihat data, PUT untuk mengubah data, dan DELETE untuk menghapus data. Semua operasi tersebut dibuat dalam satu endpoint berdasarkan ID mahasiswa dan diuji menggunakan Swagger pada alamat http://127.0.0.1:8000/docs. Urutan pengujiannya dimulai dari POST untuk memasukkan data mahasiswa, kemudian GET untuk memastikan data berhasil ditampilkan, PUT untuk mengubah data yang sudah ada, dan terakhir DELETE untuk menghapus data tersebut. Data yang digunakan sementara disimpan di dalam program sehingga data dapat hilang ketika server dihentikan. Dalam pengujian, 404 berarti data dengan ID yang dicari tidak ditemukan, sedangkan 422 biasanya menunjukkan data yang dimasukkan tidak sesuai format, misalnya JSON salah atau tipe data tidak sesuai. Setelah API selesai dibuat dan berhasil diuji melalui Swagger, project dapat disimpan dalam folder “tugas 1 integrasi sistem” dan kemudian diunggah ke GitHub sebagai hasil tugas.
Project ini merupakan implementasi API untuk tugas mata kuliah Integrasi Sistem menggunakan FastAPI.

## Model Data

API menggunakan data mahasiswa dengan atribut:

- NAMA
- ALAMAT
- IPK
- SEMESTER
- HOBI

## Endpoint

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | /mahasiswa | Menampilkan semua data |
| GET | /mahasiswa/{id} | Menampilkan data berdasarkan ID |
| POST | /mahasiswa/{id} | Menambahkan data |
| PUT | /mahasiswa/{id} | Mengubah data |
| DELETE | /mahasiswa/{id} | Menghapus data |

## Swagger

Swagger dapat diakses melalui:

http://127.0.0.1:8000/docs

## Menjalankan Project

Install dependency:

pip install -r requirements.txt

Jalankan server:

uvicorn main:app --reload