![Screenshot (61)](https://github.com/g0lgi/toko_kadal/assets/119854906/3030e816-1214-410f-bd46-782b2f021edb)[Application Link](https://tokokadal.adaptable.app)
# Tugas 3
## Perbedaan antara form POST dan form GET dalam Django
Metode GET digunakan untuk meminta data dan sering digunakan ketika ingin mengambil atau mencari data tanpa membuat perubahan apa pun. Misalnya, saat membuat halaman pencarian yang mencari melalui database. Data yang dikirimkan digabungkan menjadi string dan digunakan untuk membuat URL.

POST digunakan ketika Anda ingin mengirim data ke server. Di Django, POST digunakan ketika mengubah, menambah atau menghapus dari database dan ketika menangani informasi sensitif seperti kata sandi. Browser menggabungkan form data, mengkodekannya untuk transmisi, mengirimkannya ke server, dan kemudian menerima kembali responsnya.

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
XML (eXtensible Markup Language) adalah bahasa markup yang menggunakan tag untuk mendefinisikan elemen dan atribut untuk mendefinisikan properti. XML dirancang agar dapat dibaca oleh manusia dan mesin. XML tidak memiliki dukungan native untuk tipe data; semua data diperlakukan sebagai string. XML memungkinkan metadata disertakan dengan mudah, menggunakan atribut dan namespace.

JSON (JavaScript Object Notation) adalah format pertukaran data ringan yang menggunakan pasangan nilai kunci untuk mewakili data. JSON mudah dibaca dan ditulis oleh manusia dan mesin. JSON adalah bagian dari JavaScript dan secara asli didukung oleh JavaScript. JSON memiliki dukungan bawaan untuk tipe data, seperti string, angka, boolean, dan null. JSON tidak mendukung metadata secara native, namun dapat disertakan dalam data itu sendiri.

HTML (Bahasa Markup HiperTeks) adalah bahasa markup yang digunakan untuk membuat halaman web. HTML menggunakan tag untuk menyusun konten di halaman web. Berbeda dengan JSON dan XML yang digunakan untuk menyimpan dan bertukar data, HTML digunakan untuk menyajikan data. HTML dapat menyertakan skrip yang ditulis dalam bahasa seperti JavaScript yang dapat memengaruhi perilaku halaman web HTML.

Kesimpulannya, meskipun JSON dan XML terutama digunakan untuk menyimpan dan bertukar data, HTML digunakan untuk presentasi data. Pilihan antara JSON dan XML akan bergantung pada kebutuhan proyek Anda, bahasa pemrograman, dan preferensi pribadi.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
### 1. Ringan
JSON berbasis teks dan memiliki format data yang mudah diurai sehingga tidak memerlukan kode tambahan untuk penguraian. Ini membantu pertukaran data dan hasil layanan web agar lebih cepat.
### 2. Struktur Datanya
JSON menggunakan struktur data yang terdiri dari pasangan nilai kunci, yang mudah dipahami dan digunakan. JSON juga dapat membuat serial/menyimpan data dalam array, yang membuat pembuatan dan transfer data menjadi lebih sederhana.
### 3. Independen Bahasa
JSON tidak bergantung pada bahasa, artinya dapat digunakan dengan hampir semua bahasa pemrograman. Hal ini menjadikannya pilihan serbaguna sebagai sarana pertukaran data antar aplikasi yang berbeda.
### 4. Dapat Dibaca Manusia
JSON menggunakan teks yang dapat dibaca manusia untuk mengirimkan objek data, sehingga memudahkan developer untuk bekerja dengannya.
### 5. Kecepatan
Sintaks JSON sangat mudah digunakan, kecil, dan juga ringan, yang memungkinkannya mengeksekusi dan merespons dengan lebih cepat.

## Cara Implementasi
### Membuat input form untuk menambahkan objek model pada app sebelumnya.
Buat `forms.py` di dalam folder main. File ini nantinya akan memungkinkan kita untuk menginput data barang. Contohnya seperti:
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "price", "description"]
```
dimana `name`, `amount`, `buy_price`, dan `description` adalah field yang ada pada model Item yang sudah didefinisikan, dan nantinya akan diinput.
### Merender form yang dibuat
Kita dapat membuat file `html` baru untuk merendernya. Usahakan menggunakan nama yang representatif dan tidak ambigu. Contohya, nama file `html` yang saya buat adalah `create_product.html`. Lalu isi dengan kode berikut:
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
### Tambahkan fungsi views untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Buka `views.py` yang ada pada folder `main` dan tambahkan:
```
from django.http import HttpResponse
from django.core import serializers
```
Serializer digunakan untuk mengirim data dalam bentuk `json` dan `xml`, dan akan return HTTPResponse. Maka, tambahkan kode berikut untuk melihat objek yang ditambahkan dalam format:
`XML`
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
dan `JSON`
```
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Kita juga bisa filter berdasarkan id dengan:
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
### Membuat routing URL untuk masing-masing views yang telah ditambahkan.
Tambahkan semua url yang tadi dibuat ke dalam `urlpatterns` pada `urls.py` di folder `main`, dengan kode sebagai berikut:
```
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

## Screenshots
![Screenshot (63)](https://github.com/g0lgi/toko_kadal/assets/119854906/da747e5d-bea7-4794-9f44-df37f4110ef2)
![Screenshot (62)](https://github.com/g0lgi/toko_kadal/assets/119854906/bc1c2f6b-3363-4785-9082-61323651216f)
![Screenshot (61)](https://github.com/g0lgi/toko_kadal/assets/119854906/556aefb1-31fd-4000-b32e-7fb92612af29)
![Screenshot (60)](https://github.com/g0lgi/toko_kadal/assets/119854906/d5f77cb6-1abd-438b-af13-e0ec2b595881)
![Screenshot (59)](https://github.com/g0lgi/toko_kadal/assets/119854906/1c5e79a3-0c42-4ebf-bdd3-7488604ced62)
![Screenshot (58)](https://github.com/g0lgi/toko_kadal/assets/119854906/ce968178-6ce0-4063-9504-822b52368cf7)

# Tugas 2



## Cara Implementasi
### Setup Library yang dibutuhkan
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

### 1. Membuat sebuah proyek Django baru

Menggunakan `django-admin createproject toko_kadal` saya membuat direktori baru dengan nama `toko_kadal` (**Ingat bahwa anda BUKAN toko_kadal, melainkan diganti dengan nama direktori sendiri**).. Direktori akan berisi `manage.py` dan folder `toko_kadal` yang berisi terkait setting dan routing dari proyek. `manage.py` adalah script python yang akan saya gunakan untuk memantain dan mengatur proyek saya. `python manage.py runserver` adalah command untuk menjalankan proyek saya (**Pastikan untuk menjalankan ini sebelum menuju `http://localhost:8000/hello` yang merupakan url web django saya**).

### 2. Membuat aplikasi dengan nama main

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
### 3. Melakukan routing proyek agar dapat menjalankan aplikasi
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

### 4. Membuat fungsi render pada views.py
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

### 5. Membuat model sebagai Database
Model adalah penghubung python dengan database saya. Model pada `toko_kadal` berada pada `models.py`. Jika saya ingin membuat database yang berisi nama, amount, dan description masing-masing dengan tipe data character, integer, dan text saya dapat melakukannya dengan memodif `models.py` seperti
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=4)
    amount = models.IntegerField()
    description = models.TextField()
```
 
### Melakukan deployment ke Adaptable
Pastikan repository proyek sudah berada pada github dan bersifat public. Selanjutnya, pada adaptable, pilih opsi `deploy a new app`. Pilih repository sesuai proyek yang akan dideploy. Kemudian `Python App Template`. Selanjutnya adalah opsi database, sementara bisa menggunakan `PostgreSQL`. Sesuaikan versi python dengan versi lokal, `python --version` pada terminal lokal untuk melihat versi. Dan masukan `python manage.py migrate && gunicorn toko_kadal.wsgi` pada `Start Command`. Tentukan nama applikasi dan checklist `HTTP Listener on PORT`. (**Ingat bahwa anda BUKAN toko_kadal, melainkan diganti dengan nama direktori sendiri**)

## Bagan Applikasi Berbasis Django
![image](https://github.com/g0lgi/toko_kadal/assets/119854906/cffa22ab-e74b-496c-9fe4-34ae4c7df4da)

## Mengapa Virtual Environment
Kita menggunakan virtual environment saat membuat aplikasi web berbasis Django untuk mengisolasi dan mengelola dependensi proyek secara terpisah, sehingga memungkinkan pengembang untuk menghindari konflik antar-paket yang mungkin terjadi dengan proyek lain atau sistem secara keseluruhan. Dengan cara ini, virtual environment memungkinkan kita untuk menginstal dan mengatur versi yang tepat dari Django dan paket-paket pendukung lainnya, memudahkan pengembangan, pengujian, dan penerapan proyek tanpa merusak instalasi global di sistem yang dapat menyebabkan masalah kompatibilitas. Ini membantu menjaga kestabilan dan konsistensi aplikasi web Django yang sedang dikembangkan.

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi disarankan kuat untuk menggunakan virtual environment karena ini merupakan praktik terbaik dalam pengembangan Django. Tanpa virtual environment, dapat terjadi konflik antar-paket jika Anda bekerja pada beberapa proyek Django atau jika ada perubahan dalam versi paket-paket yang digunakan oleh sistem secara keseluruhan.

## Apa itu MVC, MVT, MVVM
MVC (Model-View-Controller): MVC memisahkan aplikasi menjadi tiga komponen utama. Model berisi data dan logika bisnis, View mengatur tampilan yang diberikan kepada pengguna, dan Controller mengontrol interaksi pengguna serta menghubungkan Model dan View. MVC lebih umum digunakan dalam pengembangan web.

MVT (Model-View-Template): MVT adalah variasi dari MVC yang digunakan dalam kerangka kerja Django, sebuah kerangka kerja web Python. Model di MVT tetap sama dengan MVC (data dan logika bisnis), View menangani tampilan, dan Template adalah komponen yang menentukan bagaimana data dari Model ditampilkan dalam View.

MVVM (Model-View-ViewModel): MVVM adalah pola desain yang umumnya digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI). Model berisi data, View adalah tampilan yang diberikan kepada pengguna, dan ViewModel menghubungkan Model dan View serta mengelola logika tampilan. MVVM umumnya digunakan dalam aplikasi desktop atau aplikasi mobile dengan antarmuka yang kompleks.

Perbedaan utama antara ketiganya adalah dalam bagaimana mereka mengorganisasi dan mengelola komponen-komponen aplikasi. MVC adalah pola yang lebih umum digunakan dalam pengembangan web, MVT khusus untuk Django, dan MVVM lebih fokus pada pengembangan aplikasi dengan antarmuka pengguna yang kompleks seperti aplikasi desktop atau mobile.
