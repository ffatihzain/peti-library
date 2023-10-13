# Muhammad Fatih Zain

## PBP A - 2206824073


<details open>
<summary>Tugas 6</summary>

# Tugas 6

## Jawaban

### Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_.

_Asynchronous Programming_
- Program dapat berjalan tanpa harus menunggu tugas yang memakan waktu selesai.
- Dapat mengeksekusi banyak program secara bersamaan.
- Dapat melibatkan _multi-threaded_ pada beberapa implementasi, khususnya pada server.
- Menggunakan konsep callback untuk menangani tugas yang memerlukan waktu lama.
- Cocok digunakan untuk operasi I/O yang mungkin memerlukan waktu lama, seperti mengunduh file dari internet.

_Synchronous Programming_
- Program berjalan secara berurutan, satu tugas setelah yang lain.
- Program dieksekusi baris per baris dari atas ke bawah.
- bersifat _single-threaded_, atau menggunakan satu _thread_ untuk mengeksekusi semua tugas.
- Cocok digunakan pada tugas ringan dan sederhana yang tidak memerlukan jeda.


### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma event-driven programming adalah sebuah pendekatan dalam pemrograman di mana program merespons peristiwa atau _event_ yang terjadi pada sistem atau aplikasi. Ini berarti bahwa program akan menjalankan tindakan tertentu ketika suatu kejadian atau peristiwa khusus terjadi, tanpa harus menjalankan kode secara manual atau berurutan. Hal ini dapat berupa interaksi pengguna, seperti mengklik tombol, mengisi formulir, atau menggulir halaman web. Pada tugas ini, salah satu contoh paradigma yang dapat terlihat adalah ketika kita melakukan klik pada _button_ `Add Book` atau `Edit` yang memicu _event_ `addItem()` atau `editItem()`.


### Jelaskan penerapan asynchronous programming pada AJAX.

Pada AJAX, asynchronous programming digunakan untuk mengirim dan menerima data dari server background, sehingga halaman web tidak perlu dimuat ulang. Hal ini membuat aplikasi web menjadi lebih responsif terhadap interaksi pengguna. Alurnya adalah data dikirim ke server menggunakan metode asynchronous, seperti XHR atau Fetch. Setelah permintaan dikirim, JavaScript akan melanjutkan eksekusi kodenya, sehingga halaman web tidak perlu dimuat ulang.


### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Fetch API
    - Bagian dari JavaScript dan merupakan standar modern ringan yang digunakan untuk mengambil dan mengirim data asinkron.
    - Menggunakan konsep Promises untuk menangani operasi asynchronous, sehingga memudahkan penanganan error dan chaining.
    - Menyediakan kontrol yang tinggi terhadap request dan respon HTTP, sehingga memungkinkan konfigurasi yang fleksibel.

jQuery
    - Library JavaScript eksternal yang menyediakan _interface_ yang mudah digunakan untuk membuat sebuah request HTTP.
    - Lebih tersedia berbagai fitur yang dapat digunakan.
    - Menyediakan helper function untuk memudahkan penggunaan oleh user, juga menggunakan callback.
    - Menyediakan sintaksis yang lebih mudah dipahami dan kepastian perilaku pada berbagai browser.

Menurut pendapat saya, implementasi AJAX yang lebih cocok digunakan sebenarnya bergantung kepada preferensi penggunaannya. Untuk perseorangan atau proyek kecil, Fetch API lebih cocok dengan bantuan Promise dan lebih ringan sehingga menjadi user-friendly. Sedangkan apabila ingin mengerjakan proyek besar dan berkolaborasi dengan banyak orang, maka jQuery lebih cocok karena fitur dukungan _cross-browser compatibility_ dan fungsi bawaan yang simpel.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.**

- AJAX GET
    - Ubahlah kode cards data item agar dapat mendukung AJAX GET.
        - Menghapus _table_ di `main.html` dan menggantinya dengan kode berikut
        ```
        <table class="table table-bordered table-hover">
            <thead class="thead-dark">
            </thead>
            <tbody id="product_table">
            </tbody>
        </table>
        ```
        Sesuaikan dengan penataan pada html sebelumnya.
    - Lakukan pengambilan task menggunakan AJAX GET.
        - Membuat fungsi baru pada `views.py` dengan nama `get_product_json` yang berfungsi untuk mengambil item (dalam kasus saya buku) yang tersimpan untuk setiap user.
        ```
        def get_product_json(request):
            product_item = Item.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize('json', product_item))
        ```
        - Membuat `<script>` di `main.html` yang berisi
        ```
        async function getItems() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json());
        }
        ```

- AJAX POST
    - Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.
        - Pertama-tama, menambahkan kode di `main.html` untuk implementasi modal pada aplikasi, hal-hal utama pada tabel akan didefinisikan.
        ```
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Book</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form id="form" onsubmit="return false;">
                            {% csrf_token %}
                            <div class="mb-3">
                                <label for="name" class="col-form-label">Name:</label>
                                <input type="text" class="form-control" id="name" name="name"></input>
                            </div>
                            <div class="mb-3">
                                <label for="amount" class="col-form-label">Amount:</label>
                                <input type="number" class="form-control" id="amount" name="amount"></input>
                            </div>
                            <div class="mb-3">
                                <label for="description" class="col-form-label">Description:</label>
                                <textarea class="form-control" id="description" name="description"></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="category" class="col-form-label">Category:</label>
                                <textarea class="form-control" id="category" name="category"></textarea>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-warning" id="button_add" data-bs-dismiss="modal">Add Book</button>
                    </div>
                </div>
            </div>
        </div>
        ```
        - Menambahkan button untuk menampilkan modal ketika kita ingin menambah buku.
        ```
        <div class="d-flex justify-content-center">
            <button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#exampleModal">
                Add Book by AJAX
            </button>
        </div>
        ```
    - Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.
        - Membuat fungsi `add_item_ajax` pada `views.py`
        ```
        @csrf_exempt
        def add_item_ajax(request):
            if request.method == 'POST':
                name = request.POST.get("name")
                amount = request.POST.get("amount")
                description = request.POST.get("description")
                category = request.POST.get("category")
                user = request.user

                new_product = Item(name=name, amount=amount, description=description, category=category, user=user)
                new_product.save()

                return HttpResponse(b"CREATED", status=201)

            return HttpResponseNotFound()
        ```
    - Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
        - Pada `urls.py` tambahkan import dan routing untuk fungsi `get_item_json` dan `add_item_ajax`.
    - Hubungkan form yang telah kamu buat di dalam modal kamu ke path `/create-ajax/`.
        - Menambahkan fungsi `addItem()` pada `<script>` di `main.html` untuk mengirimkan data item baru yang diambil dari form modal.
        ```
        function addItem() {
            fetch("{% url 'main:add_item_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(() => {
                refreshItems();
                refreshItemCount();
            });
            document.getElementById("form").reset();
            return false;
        }
        ```
    - Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.
        - Menambahkan fungsi `refreshItems()` pada `<script>` untuk menampilkan data item ketika ada perubahan secara asinkronus.
        ```
        async function refreshItems() {
            document.getElementById("product_table").innerHTML = "";
            const products = await getItems();
            let htmlString = `<tr>
                <th>Name</th>
                <th>Amount</th>
                <th>Description</th>
                <th>Category</th>
                <th>Date Added</th>
                <th>Actions</th>
            </tr>`;
            products.forEach((item) => {
                htmlString += `\n<tr>
                <td>${item.fields.name}</td>
                <td>${item.fields.amount}</td>
                <td>${item.fields.description}</td>
                <td>${item.fields.category}</td>
                <td>${item.fields.date_added}</td>
                <td>
                    <div class="d-flex justify-content-between">
                        <button class="btn transparent-btn btn-sm" onclick="increaseAmount(${item.pk})">Increase</button>
                        <button class="btn transparent-btn btn-sm" onclick="decreaseAmount(${item.pk})">Decrease</button>
                        <button class="btn btn-danger btn-sm" data-url="{% url 'main:delete_item_ajax' 1 %}" onclick="deleteItem(this, ${item.pk})">Delete</button>
                    </div>
                </td>
            </tr>`;
            });

            document.getElementById("product_table").innerHTML = htmlString;
        }
        ```
        - Menambahkan fungsi `refreshItemCount()` pada `<script>` untuk menghitung data item ketika ada perubahan jumlah.
- Melakukan perintah collectstatic.
    - Menambahkan beberapa kode di `settings.py`
    ```
    import os
    .
    .
    .

    STATIC_URL = 'static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    ```
</details>


<details open>
<summary>Tugas 5</summary>

# Tugas 5

## Jawaban

### Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

1. **Element Selector** : Selector ini bertujuan untuk memilih elemen di dalam elemen dari tipe spesifik. Selector memungkinkan pengguna untuk memberikan _style_ atau aturan tertentu kepada semua elemen yang sesuai dengan tipe tersebut pada website. Contoh :
```
p {
  font-size: 16px;
  line-height: 1.5;
  color: #333;
}
```
Selector menargetkan seluruh elemen `<P>` atau paragraph

2. Class Selector : Selector ini bertujuan untuk memilih satu atau lebih elemen berdasarkan nama kelas yang ditetapkan dalam atribut `class`. Selector ini digunakan ketika kita ingin menambahkan _style_ atau aturan untuk satu atau lebih elemen dari kelas spesifik sehingga bisa dipakai secara berulang ketika kita mengakses lagi class tersebut. Contoh :
```
.button {
  background-color: #3498db;
  color: #fff;
  padding: 10px 15px;
}
```
Selector menargetkan seluruh elemen pada class `button`

3. ID Selector : Selector ini bertujuan untuk memilih elemen secara individu dengan nilai atribut `id` spesifik. Selector ini digunakan ketika kita ingin menambahkan _style_ secara unik sehingga hanya `id` itu saja yang memiliki _style_ tersebut. Contoh :
```
#header {
  font-size: 24px;
  color: #2c3e50;
  text-align: center;
}
```
Selector menargetkan elemen `header` secara individual.


### Jelaskan HTML5 Tag yang kamu ketahui.

- `html` : Menandakan awal dan akhir dari dokumen HTML.
- `title` : Menentukan judul dari dokumen HTML.
- `head` : Menyediakan informasi mengenai dokumen HTML.
- `h1`- `h6` : Biasa digunakan untuk membuat judul dari dokumen HTML dengan ukuran yang berbeda-beda.
- `p` : Menandakan awal paragraf pada HTML.
- `button` : Membentuk tombol yang dapat di-klik pada HTML.
- `br` : Atau break line digunakan untuk memberi space kosong pada suatu baris.
- `table` : Membuat tabel yang berisi baris dan kolom pada HTML.
- `div` : Menandai sebuah section.


### Jelaskan perbedaan antara margin dan padding.

Margin : ruang di sekitar elemen HTML yang memisahkan elemen dari elemen lain di sekitarnya.
**Perbedaan**
- Berguna untuk mengatur jarak antar elemen
- Menambahkan ruang di luar elemen, sehingga memperbesar total ukuran elemen
- Memengaruhi penempatan elemen terhadap elemen lain di sekitarnya.
- Dapat menggunakan nilai negatif, yang akan mengarahkan elemen lebih dekat satu sama lain.

Padding : ruang di sekitar konten dan elemen HTML, di antara konten dan batas elemen tersebut.
**Perbedaan**
- Berguna untuk menambah ruang internal sebuah elemen
- Menambahkan ruang di dalam elemen, tetapi ukuran elemen tetapi sama
- Memengaruhi penempatan konten dalam elemen
- Tidak dapat memiliki nilai negatif



### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya.

Tailwind adalah framework yang mengadopsi pendekatan "utility-first" dimana pengguna membangun desain dengan menggabungkan kelas utilitas ke dalam elemen HTML. Tailwind menyediakan fleksibilitas dan kebebasan, framework ini menawarkan banyak kustomisasi spesifik. Oleh karena itu, Penggunaan Tailwind sudah pasti lebih lama dan butuh pemahaman yang lebih. Sedangkan Bootstrap menawarkan set class CSS dan komponen yang telah dirancang sebelumnya. Bootstrap memiliki kerangka kerja yang lebih terstruktur dengan banyak komponen rancangan, sehingga memberikan stabilitas dan kemudahan bagi pengguna. Tetapi, Bootstrap memiliki batasan dalam hal fleksibilitas desain yang unik. Kita bisa menggunakan Bootstrap ketika ingin membuat website simpel yang tidak membutuhkan banyak kustomisasi dalam CSS. Sedangkan Tailwind cocok digunakan ketika kita mau membuat website dengan banyak kustomisasi.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- **main.html**
    - Menambahkan `body` di paling atas yang berisi warna background.
    - Membuat class `.container box` yang diisi format seperti background color untuk menentukan warna, width, margin, dan padding untuk menentukan _placement_ dari box, serta tambahan lain seperti border radius, box shadow, dan transition.
    - Membuat class `.container box:hover` karena saya ingin menambahkan kesan hover ketika user berfokus ke box.
    - Membuat class `.transparent-btn` dan `transparent-btn:hover` untuk membentuk format button yang nanti akan dipakai. Format yang dimaksud adalah background color dan border.
    - Membuat class `navbar` dengan warna dark dengan tulisan `Peti Lib` di paling kiri, `Welcome, {name}!` di tengah, dan tombol `logout` di paling kanan.
    - Memberi isi pada class `container box` yaitu _title_ `Peti Library's Guide` beserta isi umum main.html yaitu tabel, nama, kelas, dll.
    - Menambahkan variasi warna pada button sehingga lebih cocok dengan background color. Contoh : button `Add New Book` menggunakan _secondary_ sebagai tema.

- **login.html**
    - Menambahkan `body` di paling atas yang berisi warna background, margin, justify content, align-items, dan height.
    - Membuat class `.container box` yang diisi format seperti background color untuk menentukan warna, width dan padding untuk menentukan _placement_ dari box, serta tambahan seperti border radius, box shadow, dan transition.
    - Membuat class `login form` dan `login button` untuk membuat template format form dan button login.
    - Membuat class `register link` untuk memberikan link apabila user belum memiliki akun dan harus register.
    - Implementasi class-class diatas dan mengisinya dengan konten yang sesuai.
- **register.html**
    - Menambahkan `body` di paling atas yang berisi warna background, margin, justify content, align-items, dan height.
    - Membuat class `.container box` yang diisi format seperti background color untuk menentukan warna, width, margin, dan padding untuk menentukan _placement_ dari box, serta tambahan lain seperti border radius, box shadow, dan transition.
    - Membuat class `register form` dan `register button` untuk membuat template format form dan button register.
    - Membuat class `login link` untuk memberikan link apabila ternyata user sudah memiliki akun.
    - Implementasi class-class diatas dan mengisinya dengan konten yang sesuai.
- **create_product.html**
    - Menambahkan `body` di paling atas yang berisi warna background.
    - Membuat class `.container box` yang diisi format seperti background color untuk menentukan warna, width, margin, dan padding untuk menentukan _placement_ dari box, serta tambahan lain seperti border radius, box shadow, dan transition.
    - Membuat class `.transparent-btn` yang berisi template untuk button yang dipakai dibawah.
    - membuat class `btn-delete` dan `btn-delete:hover` untuk membuat template bagi button delete.
    - Membuat class `navbar` dengan warna dark dengan tulisan `Peti Lib` di paling kiri dan tombol `logout` di paling kanan.
    - Implementasi class-class diatas dan mengisinya dengan konten yang sesuai.
- **edit_item.html**
    - Menambahkan `body` di paling atas yang berisi warna background.
    - Membuat class `.container box` yang diisi format seperti background color untuk menentukan warna, width, margin, dan padding untuk menentukan _placement_ dari box, serta tambahan lain seperti border radius, box shadow, dan transition.
    - Membuat class `.transparent-btn` yang berisi template untuk button yang dipakai dibawah.
    - membuat class `btn-delete` dan `btn-delete:hover` untuk membuat template bagi button delete.
    - embuat class `navbar` dengan warna dark dengan tulisan `Peti Lib` di paling kiri dan tombol `logout` di paling kanan.
    - Implementasi class-class diatas dan mengisinya dengan konten yang sesuai.
</details>


<details open>
<summary>Tugas 4</summary>

# Tugas 4

## Jawaban

### Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

`UserCreationForm` adalah salah satu formulir yang disediakan oleh Django, yang dibuat untuk pendaftaran user baru (registrasi) yang dapat menggunakan aplikasi web. Ini memiliki tiga _fields_ : username, password, dan password2 (atau biasanya disebut _password confirmation_). Dengan formulir ini, user baru dapat mendaftar dengan mudah di aplikasi web tanpa harus menulis kode lagi dari awal.

- **Kelebihan**
    - Mudah Digunakan : Formulir ini sangat mudah digunakan dan cepat diimplementasikan dalam proyek Django karena hanya perlu mengimpor dan memasukkan ke dalam _view_ dan template yang diinginkan.
    - Integrasi dengan Django : UserCreationForm terintegrasi secara baik dengan sistem autentikasi bawaan Django, sehingga memudahkan manajemen pengguna, autentikasi, dan otorisasi dalam aplikasi.
    - Keamanan Terjamin: Django UserCreationForm sudah memasukkan mekanisme keamanan yang umumnya diperlukan untuk mencegah serangan sehingga kebocoran atau pencurian data dapat dicegah. Serangan seperti SQL injection dan cross-site scripting (XSS) umum terjadi apabila tidak ada tindakan preventif yang menghalanginya.
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
<img src="/assets/user1 tugas 4.png">
<img src="/assets/user2 tugas 4.png">

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

5. Merestriksi akses halaman main pada masing-masing user
    - Tambahkan import `login_required` pada `views.py`
    - Menambahkan kode `@login_required(login_url='/login')` tepat diatas fungsi `show_main` agar halaman _main_ hanya dapat diakses oleh user yang sudah login.
</details>

<details open>
<summary>Tugas 3</summary>

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
</details>

<details open>
<summary>Tugas 2</summary>

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
</details>