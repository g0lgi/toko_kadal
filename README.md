[Application Link](https://tokokadal.adaptable.app)
# Tugas 4
## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah form bawaan di Django yang digunakan untuk membuat pengguna baru tanpa privileges. Dibutuhkan nama pengguna dan kata sandi sebagai masukan dan kata sandi harus dikonfirmasi ulang. Berikut beberapa kelebihan dan kekurangannya:
|                            Keuntungan                           |                                                                         Kekurangan                                                                         |
|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Mudah digunakan dan tidak memerlukan banyak koding              | Tidak ada field tambahan seperti email, nama depan,  atau nama belakang secara default (Namun bisa ditambahkan dengan memperluas class 'UserCreationForm') |
| Menyediakan validasi bawaan untuk password                      | Tidak menyediakan verifikasi email atau aktivasi akun secara default, sehingga perlu diterapkan secara terpisah                                            |
| Secara otomatis meng-hash password sebelum disimpan ke database |                                                                                                                                                            |
| Bisa disesuaikan untuk menambah field atau validation           |                                                                                                                                                            |

##  Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses verifikasi identitas pengguna. Autentikasi menjawab pertanyaan “Siapa kamu?”. Di Django, sistem autentikasi memverifikasi apakah pengguna adalah seperti yang diklaim. Hal ini memastikan pengguna memberikan kredensial yang valid, seperti nama pengguna dan kata sandi, untuk mendapatkan akses ke sumber daya yang dilindungi. Sistem autentikasi Django menangani autentikasi dan otorisasi, dengan mengonfirmasi identitas pengguna terlebih dahulu, lalu memberinya akses ke fungsi tertentu berdasarkan kredensial mereka.

Di sisi lain, otorisasi menentukan apa yang boleh dilakukan oleh pengguna yang telah diautentikasi. Otorisasi menjawab pertanyaan “Apa yang boleh Anda lakukan?”. Di Django, otorisasi mendefinisikan permissions dan privileges yang diberikan kepada pengguna yang sudah diautentikasi. Otorisasi mengontrol akses ke sumber daya atau tindakan tertentu dalam aplikasi. Misalnya, otorisasi dapat membatasi pengguna tertentu untuk mengakses data sensitif atau melakukan operasi penting.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah potongan kecil data yang disimpan situs web di komputer pengguna. Mereka digunakan untuk mengingat informasi tentang pengguna, seperti contohnya preferensi mereka, status login, dan isi keranjang belanja. Django menggunakan cookie untuk mengelola data user session. Ketika pengguna berinteraksi dengan situs web yang didukung Django, Django memberikan unique session ID ke browser mereka menggunakan cookie. Data session sebenarnya disimpan di sisi server, biasanya di dalam database. Cookie ID sesi memungkinkan Django untuk mengidentifikasi setiap browser dan mengaitkannya dengan data sesi yang sesuai. Secara default, Django menyimpan sesi di database Anda menggunakan model `django.contrib.sessions.models.Session`. Namun, Anda dapat mengkonfigurasi Django untuk menyimpan data sesi di tempat lain, seperti di filesystem atau cache anda.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Sebagian besar cookie aman dan digunakan oleh perusahaan-perusahaan untuk menawarkan lebih banyak personalisasi di situs mereka. Namun, beberapa cookie dapat digunakan untuk melacak kita tanpa persetujuan kita. Namun, cookie itu sendiri tidak berbahaya pada komputer. Cookie hanyalah file teks yang dapat dihapus kapan saja dan tidak dapat digunakan untuk menyebarkan virus atau mengakses hard drive kita.

Meskipun demikian, cookie juga memiliki risiko. Cookie yang tidak dilindungi dapat dimanipulasi, dan berakibat pengguna dan/atau organisasi terkena cybercrime yang cukup parah. Misalnya, jika cookie dibajak, penyerang dapat menyamar sebagai pengguna dan mendapatkan akses. Selain itu, cookie dapat digunakan untuk memalsukan identitas pengguna, sehingga memungkinkan penyerang mendapatkan akses ke akun online mereka.

## Cara Implementasi
###  Mengimplementasikan fungsi registrasi, login, dan logout
Pada `views.py`, saya mengimport-import yang dibutuhkan, lalu membuat fungsi `register`, `login_user`, dan `logout_user`. Fungsi `login_user` direstriksi, dan saat login, data `last_login` juga disimpan sebagai cookie yang nantinya akan dihapus saat user logout. Ketiganya menerima request sebagai input. Lalu saya membuat html untuk masing-masing fungsi tersebut pada `main/templates`, serta mengimport masing-masing fungsi tersebut pada file `urls.py` yang ada di `main`, dan menambahkan path url mereka ke `urlpatterns`.

### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Saya meregistrasikan akun, menambah 3 produk, lalu diulangi lagi.

### Menghubungkan model Item dengan User
Pada `models.py`, saya menambahkan atribut `user` pada `Product` dengan menggunakan `ForeignKey`. Lalu saya juga mengubah fungsi `create_product` pada `views.py`  agar sesuai, dan tentunya tidak lupa untuk migrate.

### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
Pada `views.py`, saya menambahkan data `last_login` dan mengganti value dari `name` di `context` `show_main` agar berisi username. Lalu ditambahkan `last_login` pada `main.html`


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
**1. Ringan**\
JSON berbasis teks dan memiliki format data yang mudah diurai sehingga tidak memerlukan kode tambahan untuk penguraian. Ini membantu pertukaran data dan hasil layanan web agar lebih cepat.

**2. Struktur Datanya**\
JSON menggunakan struktur data yang terdiri dari pasangan nilai kunci, yang mudah dipahami dan digunakan. JSON juga dapat membuat serial/menyimpan data dalam array, yang membuat pembuatan dan transfer data menjadi lebih sederhana.

**3. Independen Bahasa**\
JSON tidak bergantung pada bahasa, artinya dapat digunakan dengan hampir semua bahasa pemrograman. Hal ini menjadikannya pilihan serbaguna sebagai sarana pertukaran data antar aplikasi yang berbeda.

**4. Dapat Dibaca Manusia**\
JSON menggunakan teks yang dapat dibaca manusia untuk mengirimkan objek data, sehingga memudahkan developer untuk bekerja dengannya.

**5. Kecepatan**\
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
![Screenshot (64)](https://github.com/g0lgi/toko_kadal/assets/119854906/c82d4e63-b048-4796-90a0-c11b789db4d9)
![Screenshot (66)](https://github.com/g0lgi/toko_kadal/assets/119854906/80e9bf6a-6c21-4895-938b-17a782f9902b)
![Screenshot (67)](https://github.com/g0lgi/toko_kadal/assets/119854906/2ff43a02-5fa2-4396-83fb-0ad8e177a670)
![Screenshot (68)](https://github.com/g0lgi/toko_kadal/assets/119854906/f9a33901-9d03-4698-b9b9-7e082cade2d0)
![Screenshot (69)](https://github.com/g0lgi/toko_kadal/assets/119854906/18e96b48-ad54-459f-9b67-269e8cccbff2)

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
