# Muhammad Fatih Zain

## PBP A - 2206824073


## Tugas 4

## Jawaban

### Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

`UserCreationForm` adalah salah satu formulir yang disediakan oleh Django, yang dibuat untuk pendaftaran user baru (registrasi) yang dapat menggunakan aplikasi web. Ini memiliki tiga _fields_ : username, password, dan password2 (atau biasanya disebut _password confirmation_). Dengan formulir ini, user baru dapat mendaftar dengan mudah di aplikasi web tanpa harus menulis kode lagi dari awal.

- **Kelebihan**
    - Mudah Digunakan : Formulir ini sangat mudah digunakan dan cepat diimplementasikan dalam proyek Django karena hanya perlu mengimpor dan memasukkan ke dalam _view_ dan template yang diinginkan.
    - Integrasi dengan Django : UserCreationForm terintegrasi secara baik dengan sistem autentikasi bawaan Django, sehingga memudahkan manajemen pengguna, autentikasi, dan otorisasi dalam aplikasi.
    - 
- **Kekurangan**
    - Field yang Terbatas : UserCreationForm hanya memiliki _field_ terbatas yaitu username dan password yang telah diberikan secara _default_. misal kita ingin menambahkan verifikasi email tidak akan bisa karena tidak terdapat _field_ email _default_, sehingga kita harus menambahkan secara manual.
    - Terbatas pada Pembuatan Akun : Formulir ini hanya dikhususkan untuk membuat akun user baru. Oleh karena itu, kita hanya bisa mengimplementasikan fitur tersebut, sehingga untuk menambahkan fitur pengelolaan profil atau pengeditan profil harus membuat formulir khusus hal tersebut.
    - Ketergantungan pada Django : Kita hanya dapat menggunakan Django sebagai kerangka kerja pengembangan jika ingin menggunakan UserCreationForm. Karena apabila kita menggunakan kerangka kerja lain, ini belum tentu cocok.


### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

**Autentikasi** : Proses verifikasi apakah pengguna yang sedang melakukan login atau masuk ke dalam sistem adalah benar-benar orang yang memiliki akses dan sesuai. Hal ini biasa dilakukan dengan proses login menggunakan username dan password.

**Otorisasi** : Proses untuk memutuskan apa yang diizinkan atau tidak diizinkan oleh individu atau entitas setelah melakukan otentikasi. Proses ini menentukan hak akses dan izin terhadap sumber daya atau layanan tertentu. Salah satu contohnya adalah setelah otentikasi, sistem akan menggunakan otorisasi untuk menentukan apa yang dapat dilihat atau dilakukan user pada sistem tersebut. misalnya, user mungkin memiliki izin untuk melihat tetapi tidak untuk mengedit data.

kedua proses diatas penting karena keduanya dilakukan untuk memastikan keamanan data dari user yang ingin mengakses aplikasi. Autentikasi memastikan pengguna yang sah, sementara otorisasi mengontrol akses mereka.

### Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?

_Cookies_ adalah data kecil yang digunakan dalam konteks aplikasi web untuk menyimpan informasi di sisi klien (browser pengguna) yang dapat diakses oleh server web. Mereka sering digunakan untuk berbagai tujuan, termasuk mengelola data sesi pengguna. Django menggunakan _cookies_ untuk mengelola data sesi pengguna dengan cara berikut :
- Membuat Sesi Pengguna : Menciptakan sesi pengguna dan ID sesi unik saat mengakses aplikasi.
- Menyimpan Data Sesi : _Cookies_ digunakan untuk menyimpan data sesi pengguna. Ini memungkinkan aplikasi web untuk mengidentifikasi pengguna dan melacak aktivitas mereka.
- Mengakses Data Sesi : Membaca _cookies_ dengan `request.COOKIES` untuk mengambil nilai atau data yang disimpan dalam _cookies_.
- Pembaruan Data Sesi : Memungkinan _developer_ untuk memperbarui sesi pengguna.
- Pengakhiran sesi : Proses pembersihan data saat keluar atau ketika sesi berakhir.

### Apakah pengunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan _cookies_ secara _default_ dalam pengembangan web relatif aman, namun keamanan tersebut sebenarnya dipengaruhi oleh bagaimana _cookies_ tersebut digunakan dan diimplementasikan. Resiko potensial yang dapat muncul adalah pencurian data sensitif, pelacakan, dan kebocoran informasi pribadi yang dilakukan _cybercriminal_. Beberapa cara yang dapat dilakukan untuk menghindari hal tersebut adalah dengan memvalidasi data, misalnya dengan menggunakan HTTPS.

### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar

- **Register**
    - Pada `views.py` tambahkan import `redirect`,`UserCreationForm`, dan `messages`. Hal ini dilakukan untuk memudahkan pembuatan formulir registrasi pada aplikasi web.
    - Membuat fungsi `register` dengan parameter `request` yang berfungsi untuk melaksanakan proses registrasi user.
    - Membuat berkas HTML baru dengan nama `register.html` pada folder `main/template` yang berisi layout dari halaman registrasi pada aplikasi.
    - Tambahkan `import register` pada `urls.py` di subdirektori `main`.
    ```
    from main.views import register
    ```
    - Masukkan _path url_ register yang telah diimport tadi ke dalam `urlpatterns`.

- **Login**
    - Pada `views.py` tambahkan import `authenticate` dan `login`. Hal ini dilakukan untuk memudahkan proses autentikasi dan login jika autentikasi berhasil.
    - Membuat fungsi `login` dengan parameter `request` yang berfungsi untuk melaksanakan proses login dan autentikasi user.
    - Membuat berkas HTML baru dengan nama `login.html` pada folder `main/template` yang berisi layout dari halaman login pada aplikasi.
    - Tambahkan `import login` pada `urls.py` di subdirektori `main`.
    ```
    from main.views import login_user
    ```
    - Masukkan _path url_ login yang telah diimport tadi ke dalam `urlpatterns`.

- **logout**
    - Pada `views.py` tambahkan import `logout`.
    - Membuat fungsi `logout` dengan parameter `request` yang berfungsi untuk melaksanakan proses logout dan menghapus sesi user yang sedang masuk.
    - Menambahkan kode berupa button `logout` pada `main.html` di folder `main/templates`.
    - Tambahkan `import logout_user` pada `urls.py` di subdirektori `main`.
    ```
    from main.views import logout_user
    ```
    - Masukkan _path url_ logout yang telah diimport tadi ke dalam `urlpatterns`.

2. Membuat **dua** akun pengguna dengan masing-masing **tiga** dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun **di lokal**

3. Menghubungkan model `Item` dengan `User`
    - Menambahkan import `User` pada `models.py`
    ```
    from django.contrib.auth.models import User
    ```
    - Pada model `Item`, menambahkan variabel `user` yang berisi `ForeignKey` yang berfungsi untuk menghubungkan satu produk dengan satu user melalui sebuah _relationship_, dimana sebuah item pasti terasosiasikan dengan seorang user.
    - ubah potongan kode pada fungsi `create_item` pada `views.py` dengan parameter `commit=False` yang digunakan untuk mencegah Django agar tidak langsung menyimpan objke ke database. Isi juga _field_ `user` dengan objek `User` dari return value `request.user` untuk menandakan bahwa objek tersebut dimiliki pengguna yang sedang login.
    -Mengubah sedikit variabel `items` pada fungsi `show_main` menjadi :
    `items = Item.objects.filter(user=request.user)`
    dan mengubah `'name'` pada `context` menjadi :
    `'name': request.user.username,`

4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan `cookies `seperti `last login` pada halaman utama aplikasi.
    - Import `datetime` pada `views.py`
    - Membuat fungsi `login_user` yang berisi fungsi untuk menambahkan _cookie_ bernama `last_login` untuk melihat kapan terakhir kali user melakukan login. Edit blok `if user is not None` dengan menambahkan kode :
        - `login(request, user)`
        - `response = HttpResponseRedirect(reverse("main:show_main"))`
        - `response.set_cookie('last_login', str(datetime.datetime.now()))`
        - Terakhir, `return response`
    - Dalam `context` pada fungsi `show_main`, tambahkan kode `'last_login': request.COOKIES['last_login'],`
    - Ubah fungsi `logout_user` dengan tambahan kode berikut :
        - `response = HttpResponseRedirect(reverse('main:login'))`
        - `response.delete_cookie('last_login')`
        - `return response`


# Tugas 3

## Jawaban

### Apa perbedaan antara form POST dan form GET dalam Django?

Perbedaan dari kedua form tersebut terdapat pada penggunaannya. POST biasa digunakan jika user ingin bertukar data atau request apapun yang bisa digunakan untuk mengubah sistem atau database. Cara kerjanya adalah POST mengumpulkan data form dan mengirim data tersebut pada server. sedangkan GET digunakan jika user ingin mengambil sebuah data atau request yang bersifat membaca atau pencarian, sehingga tidak memengaruhi sistem. data yang diambil GET juga terlihat di URL, sehingga membuat hal tersebut kurang aman dan berbalik dengan POST yang menyembunyikan data.


### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

HTML adalah bahasa yang biasa digunakan untuk membuat struktur dan tampilan halaman web. HTML adalah dasar utama dari web development untuk membuat struktur dari halaman web. Sedangkan JSON dan XML biasanya digunakan untuk penyimpanan dan transmisi data . Perbedaan dari XML dan JSON lebih tertuju kepada penggunaannya. XML merupakan format fleksibel dan terstruktur yang digunakan untuk pertukaran data antar aplikasi, sedangkan JSON dengan format yang lebih ringan lebih sering digunakan dalam pengembangan web dan API. JSON memanfaatkan notasi objek JavaScript untuk menyusun data.


### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

 Beberapa alasan mengapa JSON sering digunakan dalam pertukaran data adalah karena JSON memiliki advantage dalam beberapa aspek, seperti mudah dibaca, dapat menghemat memory pada aplikasi, dan juga fleksibel. JSON juga sangat kompatibel dengan berbagai bahasa pemrograman, framework atau sistem operasi sehingga berguna dan efisien untuk pertukaran data antar sistem. Terakhir, JSON tergolong mudah dibaca dan dimengerti, serta JSON merupakan format yang mandiri (tidak membutuhkan atribut tambahan).


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

1. Membuat input form untuk menambahkan objek model pada app sebelumnya
- Membuat `forms.py` pada folder `main`
Dalam file `forms.py`, buat class `Product Form` dengan parameter `ModelForm`. Kemudian isi class dengan class `Meta` yang berisi dengan variabel `model = Item` yang menunjukkan model yang digunakan pada form (dalam kasus ini objek Item). Class juga berisi `fields = ["name", "price", "description", "category"]` untuk menekankan atribut dari model `Item`.

- Membuat fungsi `create_product` dengan parameter `request`
Dalam fungsi tersebut, terdapat form yang berisi `ProductForm` dengan parameter input `request.POST` sebagai `QueryDict`. Selanjutnya terdapat `if-else` untuk validasi konten dengan `form.is_valid()` dan menyimpan konten dengan `form.save`. Jika konten tersimpan, akan redirect ke halaman utama dengan `return HttpResponseRedirect(reverse('main:show_main'))`. Terakhir fungsi akan me-render `create_product.html`.

- Menambahkan kode pada fungsi `show_main` pada file `views.py`
Menambahkan `items = Item.objects.all()` untuk mengambil seluruh object `Item` pada database. kemudian menambahkan `'products': products` pada context.

- Import beberapa fungsi dan menambahkan path url
menambahkan path url ke `urlpatterns` dalam `urls.py` di `main` --> `path('create-product', create_product, name='create_product'),`. Dilakukan untuk mengakses fungsi yang telah di-import.

- Membuat file `create_product.html` pada folder `templates` di `main`
Isi file dengan kode yang sesuai untuk pembuatan interface tabel. Menambahkan `{% csrf_token %}` yaitu token yang berfungsi sebagai security untuk mencegah serangan berbahaya dan `<form method="POST">` sebagai batas tag form dengan metode POST.
- Menambahkan kode di `main.html`
Menambah kode untuk memperlihatkan data item pada HTML dalam bentuk tabel. Terdapat juga button `Add New Product` yang mengarahkan ke halaman form.

2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2

- Membuat fungsi `show_xml` pada `views.py` dan membuat path url untuk mengakses fungsi tersebut
Mengambil data Item dan me-return sebagai XML dengan
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
pada `urls.py` dalam direktori `main` memasukkan kode  `path('xml/', show_xml, name='show_xml'),`

- Membuat fungsi `show_json` pada `views.py` dan membuat path url untuk mengakses fungsi tersebut
Mengambil data Item dan me-return sebagai JSON dengan
```
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
pada `urls.py` dalam direktori `main` memasukkan kode  `path('show_json/', show_json, name='show_json'),`

- Membuat fungsi `show_xml_by_id` pada `views.py` dan membuat path url untuk mengakses fungsi tersebut
Mengambil data Item dan me-return sebagai XML yang terurut dengan id
```
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
pada `urls.py` dalam direktori `main` memasukkan kode  `path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),`

- Membuat fungsi `show_json_by_id` pada `views.py` dan membuat path url untuk mengakses fungsi tersebut
Mengambil data Item dan me-return sebagai JSON yang terurut dengan id
```
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
pada `urls.py` dalam direktori `main` memasukkan kode  `path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),`


### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

<img src="/assets/postman localhost og.png">
<img src="/assets/postman localhost xml.png">
<img src="/assets/postman localhost json.png">
<img src="/assets/postman localhost xml id.png">
<img src="/assets/postman localhost json id.png">



# Tugas 2

## Jawaban

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat sebuah proyek Django baru.
    - Untuk membuat sebuah proyek Django baru saya perlu membuat virtual environment. Hal ini dilakukan dengan menuliskan command berikut pada terminal.
    ```
    python -m venv env
    ```
    - Lalu untuk mengaktifkan virtual environment tuliskan command berikut. Virtual environment aktif dengan adanya tanda (env) pada input terminal. 
    ```
    env\Scripts\activate
    ```
    - Pada direktori yang sama, saya membuat berkas berjudul `requirements.txt` yang digunakan untuk menambahkan dependencies yang diperlukan.
    - Kemudian saya run command `pip install -r requirements.txt` untuk melakukan instalasi dependencies tersebut.
    - Lalu untuk memulai proyek Django tersebut saya menjalankan command `django-admin startproject peti_library .`
    - Untuk keperluan deployment, tambahkan `"*"` pada bagian `ALLOWED_HOSTS` di file `settings.py`.
    - Saya juga menambahkan file `.gitignore` guna memberikan perintah kepada git untuk mengabaikan file yang tidak diperlukan.
2. Membuat aplikasi dengan nama main pada proyek tersebut.
    - Kemudian saya menjalankan command `python manage.py startapp main` untuk membuat aplikasi `main`.
    - Tak lupa juga saya untuk mendaftarkan aplikasi `main` ke dalam proyek dengan memasukkannya ke dalam variabel INSTALLED_APPS pada `settings.py`.
    - Lalu saya membuat direktori baru bernama `templates` dalam `main` dan membuat file `main.html`. Nantinya file tersebut akan dimanfaatkan sebagai tampilan pada aplikasi kita.
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.
    - Membuat file baru bernama `urls.py` dalam direktori main kemudian menambahkan kode `path('', show_main, name='show_main'),`.
    - Menambahkan kode `path('main/', include('main.urls')),` pada file `urls.py` dalam direktori peti_library (berbeda dengan `urls.py` pada direktori main).
4. Membuat model pada aplikasi `main` dengan nama `Item`.
    - pada `models.py` pada direktori `main` saya menambahkan atribut wajib dan tambahan yaitu :
        - `name` dengan tipe CharField
        - `date_added` dengan tipe DateField
        - `amount` dengan tipe IntegerField
        - `description` dengan tipe TextField
        - `category` dengan tipe TextField
5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
    - pada `views.py`, saya menambahkan fungsi yang berisi context nama dan kelas yang berhubungan dengan `main.html`.
6. Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
    - Membuat file baru bernama `urls.py` dalam direktori main kemudian menambahkan variabelapp_name berisi `main` dan kode `path('', show_main, name='show_main'),` pada `urlpatterns`.
7. Melakukan deployment ke Adaptable terhadap aplikasi
    - Melakukan add, commit, dan push ke repositori GitHub.
    - Deploy ke website Adaptable.

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

<img src="/assets/flowchart tugas2.png">

### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Tujuan dari virtual environment adalah untuk mengisolasi proyek Django kita dari sistem. Virtual environment mengisolasi ibarat lingkungan virtual sehingga modul atau dependencies yang kita install pada proyek tidak dapat diakses dari luar. Hal ini memberikan kontrol penuh atas proyek Django dan memudahkan untuk pemisahan dan pengaturan modul/dependencies.

Penggunaan virtual environment tidak wajib dilakukan dan kita tetap dapat membuat aplikasi web Django. Namun, proyek akan tidak terisolasi dan terancam mengalami tabrakan antar dependencies sehingga terjadi mix up dengan proyek-proyek lainnya.

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

- `MVC` atau `Model-View-Controller` adalah arsitektur yang terdiri dari tiga komponen Model, View dan Controller dengan tugas masing-masing. Model mengelola data dan logika aplikasi, View menampilkan informasi dan interface dari Model dan Controller mengintegrasikan Model dan View.

- `MVT` atau `Model-View-Template` adalah arsitektur yang terdiri dari tiga komponen Model, View, dan Template. Model mengelola data dan logika aplikasi, View menampilkan informasi dan interface dari Model, dan Template menentukan penampilan interface user.

- `MVVM` atau `Model-View-ViewModel` adalah arsitektur yang terdiri dari tiga komponen Model, View, dan ViewModel. Model mengelola data dan logika aplikasi, View menampilkan data dari Model, dan ViewModel mengambil data dari Model dan melakukan formatting sehingga dapat ditampilkan dengan baik pada View.

Perbedaan dari ketiganya adalah MVC terfokus pada pengendalian alur kerja aplikasi, MVT memanfaatkan template untuk menggabungkan data dan view (tampilan), dan MVVM memisahkan View dan ViewModel dengan jelas.
