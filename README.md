# Muhammad Fatih Zain

## PBP A - 2206824073

## Aplikasi

Berikut adalah link menuju ke aplikasi saya [petilibrary](petilibrary.adaptable.app/main/)

# Tugas 3

## Jawaban

### Apa perbedaan antara form POST dan form GET dalam Django?


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
