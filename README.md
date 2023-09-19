[Application Link](https://tokokadal.adaptable.app)
# Cara Implementasi
## Setup Library yang dibutuhkan
Membuat file `requirements.txt` yang berisi:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Installasi dapat dilakukan pada terminal dengan menggunakan Virtual Environment:
```sh
python -m venv env # Buat virtual env
env\Scripts\activate.bat
pip install -r requirements.txt
```

## 1. Membuat sebuah proyek Django baru

Menggunakan `django-admin createproject toko_kadal` saya membuat direktori baru dengan nama `toko_kadal` (**Ingat bahwa anda BUKAN toko_kadal, melainkan diganti dengan nama direktori sendiri**).. Direktori akan berisi `manage.py` dan folder `toko_kadal` yang berisi terkait setting dan routing dari proyek. `manage.py` adalah script python yang akan saya gunakan untuk memantain dan mengatur proyek saya. `python manage.py runserver` adalah command untuk menjalankan proyek saya (**Pastikan untuk menjalankan ini sebelum menuju `http://localhost:8000/hello` yang merupakan url web django saya**).

## 2. Membuat aplikasi dengan nama main

`django-admin startproject toko_kadal .` digunakan untuk membuat proyek dengan nama `toko_kadal`. Applikasi dalam bentuk folder baru dengan nama `toko_kadal`. `python manage.py startapp  main` digunakan untuk membuat applikasi main. Setelah membuat applikasi, saya perlu mendaftarkannya pada `settings.py` yang terletak di folder proyek. Tambahkan `main` pada `INSTALLED_APPS` sehingaa berbentuk seperti
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
]
```
## 3. Melakukan routing proyek agar dapat menjalankan aplikasi
Konfigurasi link `toko_kadal` pada proyek dengan mengubah `urls.py` yang terletak di direktori main sehingga kurang lebih menjadi seperti
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

```
Buatlah `urls.py` pada folder `toko_kadal` dengan kode:
```python
from django.urls import path, include

urlpatterns = [
    path('main/', include('main.urls'))
]
```

## 4. Membuat fungsi render pada views.py
Untuk mengatur apa yang ingin user lihat ketika menuju `http://localhost:8000/`, saya dapat mengembalikan html templates.
Buat direktori `templates` pada `toko_kadal` dan masukan html yang akan dirender dengan nama `main.html`. Contoh `maino.html` yang akan menampilkan nama dan kelas.
```html
<head>
<title>Toko Kadal Patrick</title>
</head>
<body>
<h1>Nama : Emmanuel Patrick</h1>
<h1>Kelas : PBP D</h1>
</body>
```
pada `views.py` saya dapat mengembalikan `main.html` dengan cara menambahkan
```python
from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
```
Perubahan dapat dilihat langsung pada `http://localhost:8000/`.

## 5. Membuat model sebagai Database
Model adalah penghubung python dengan database saya. Model pada `toko_kadal` berada pada `models.py`. Jika saya ingin membuat database yang berisi nama, amount, dan description masing-masing dengan tipe data character, integer, dan text saya dapat melakukannya dengan memodif `models.py` seperti
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=4)
    amount = models.IntegerField()
    description = models.TextField()
```
 
## Melakukan deployment ke Adaptable
Pastikan repository proyek sudah berada pada github dan bersifat public. Selanjutnya, pada adaptable, pilih opsi `deploy a new app`. Pilih repository sesuai proyek yang akan dideploy. Kemudian `Python App Template`. Selanjutnya adalah opsi database, sementara bisa menggunakan `PostgreSQL`. Sesuaikan versi python dengan versi lokal, `python --version` pada terminal lokal untuk melihat versi. Dan masukan `python manage.py migrate && gunicorn toko_kadal.wsgi` pada `Start Command`. Tentukan nama applikasi dan checklist `HTTP Listener on PORT`. (**Ingat bahwa anda BUKAN toko_kadal, melainkan diganti dengan nama direktori sendiri**)

# Bagan Applikasi Berbasis Django
![image](https://github.com/g0lgi/toko_kadal/assets/119854906/cffa22ab-e74b-496c-9fe4-34ae4c7df4da)

# Mengapa Virtual Environment
Kita menggunakan virtual environment saat membuat aplikasi web berbasis Django untuk mengisolasi dan mengelola dependensi proyek secara terpisah, sehingga memungkinkan pengembang untuk menghindari konflik antar-paket yang mungkin terjadi dengan proyek lain atau sistem secara keseluruhan. Dengan cara ini, virtual environment memungkinkan kita untuk menginstal dan mengatur versi yang tepat dari Django dan paket-paket pendukung lainnya, memudahkan pengembangan, pengujian, dan penerapan proyek tanpa merusak instalasi global di sistem yang dapat menyebabkan masalah kompatibilitas. Ini membantu menjaga kestabilan dan konsistensi aplikasi web Django yang sedang dikembangkan.

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi disarankan kuat untuk menggunakan virtual environment karena ini merupakan praktik terbaik dalam pengembangan Django. Tanpa virtual environment, dapat terjadi konflik antar-paket jika Anda bekerja pada beberapa proyek Django atau jika ada perubahan dalam versi paket-paket yang digunakan oleh sistem secara keseluruhan.

# Apa itu MVC, MVT, MVVM
MVC (Model-View-Controller): MVC memisahkan aplikasi menjadi tiga komponen utama. Model berisi data dan logika bisnis, View mengatur tampilan yang diberikan kepada pengguna, dan Controller mengontrol interaksi pengguna serta menghubungkan Model dan View. MVC lebih umum digunakan dalam pengembangan web.

MVT (Model-View-Template): MVT adalah variasi dari MVC yang digunakan dalam kerangka kerja Django, sebuah kerangka kerja web Python. Model di MVT tetap sama dengan MVC (data dan logika bisnis), View menangani tampilan, dan Template adalah komponen yang menentukan bagaimana data dari Model ditampilkan dalam View.

MVVM (Model-View-ViewModel): MVVM adalah pola desain yang umumnya digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI). Model berisi data, View adalah tampilan yang diberikan kepada pengguna, dan ViewModel menghubungkan Model dan View serta mengelola logika tampilan. MVVM umumnya digunakan dalam aplikasi desktop atau aplikasi mobile dengan antarmuka yang kompleks.

Perbedaan utama antara ketiganya adalah dalam bagaimana mereka mengorganisasi dan mengelola komponen-komponen aplikasi. MVC adalah pola yang lebih umum digunakan dalam pengembangan web, MVT khusus untuk Django, dan MVVM lebih fokus pada pengembangan aplikasi dengan antarmuka pengguna yang kompleks seperti aplikasi desktop atau mobile.
