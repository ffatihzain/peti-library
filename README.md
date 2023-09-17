# Muhammad Fatih Zain

## PBP A - 2206824073

## Aplikasi

Berikut adalah link menuju ke aplikasi saya [petilibrary](petilibrary.adaptable.app/main/)

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

-Menambahkan kode pada fungsi `show_main` pada file `views.py`
Menambahkan `items = Item.objects.all()` untuk mengambil seluruh object `Item` pada database. kemudian menambahkan `'products': products` pada context.

- Import beberapa fungsi dan menambahkan path url
menambahkan path url ke `urlpatterns` dalam `urls.py` di `main` --> `path('create-product', create_product, name='create_product'),`. Dilakukan untuk mengakses fungsi yang telah di-import.

- Membuat file `create_product.html` pada folder `templates` di `main`
Isi file dengan kode yang sesuai untuk pembuatan interface tabel. Menambahkan `{% csrf_token %}` yaitu token yang berfungsi sebagai security untuk mencegah serangan berbahaya dan `<form method="POST">` sebagai batas tag form dengan metode POST.
- Menambahkan kode di `main.html`
Menambah kode untuk memperlihatkan data item pada HTML dalam bentuk tabel. Terdapat juga button `Add New Product` yang mengarahkan ke halaman form.

2. & 3. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

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
