# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Mereka meminta bantuan untuk dibuatkan dashboard agar memduahkan mereka dalam memahami data dan memonitor performa siswa.
Selain dashboard yang diminta untuk memonitor performa siswanya, kita perlu membuat model prediction menggunakan bantuan machine learning untuk membantu mendeteksi siswa yang mungkin akan dropout berdasarkan faktor-faktor yang mempengaruhinnya secara cepat.

### Permasalahan Bisnis

Hingga saat ini tingkat dropout siswa mencapai lebih dari 30%, jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Jika tidak segera diselesaikan dan terus berlanjut, ini dapat memperburuk citra institusi pendidikan kedepannya.

### Cakupan Proyek

Untuk menjawab permasalahan bisnis tersebut, pada proyek kali ini kita perlu mengetahui terlebih dahulu faktor apa saja yang menjadi penyebab tingginya tingkat dropout siswa kemudian kita buatkan web app untuk membantu memprediksi siswa berdasarkan faktor-faktor tersebut. Metode yang diterapkan antara lain Exploratory Data Analysis (EDA) yang diperkuat dengan analisis korelasi, dan model machine learning dengan penerapan hyperparmeter tuning agar memperoleh hasil yang maksimal, Algoritma machine learning yang digunakan pada hyperparameter tuning antara lain Random Forest Classifier, Gradient Boosting Classifier, dan Support Vector Classifier, kemudian dengan model terbaik yang dibuat kita terapkan function 'feature importaces' untuk mengetahui feature apa saja yang paling berpengaruh terhadap tingkat dropout siswa.

Selain itu kita juga akan membuat business dashboard menggunakan Tableau untuk memberikan insight dari data yang sedang dianalisis, dan berguna untuk memonitori feature/faktor yang mempengaruhi tingginya tingkat dropout, serta menganalisis siswa yang masih aktif/enrolled berdasarkan faktor-faktor yang terindikasi berpengaruh terhadap dropout rate.

Dan terakhir akan kita buatkan web app pada streamlit yang dapat digunakan untuk memprediksi siswa dari data yang diinput pada sistem.

### Persiapan

Sumber data: [data.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv)

Setup environment:
- Via Google Colabolatory:
   1. Buka file notebook.ipynb pada Google Colaboratory
   2. Jalankan kode berikut
      ```
      !pip install -r requirements.txt
      ```
- Via Local:
   Jalankan kode berikut pada terminal/shell
   ```
   mkdir student_dropout_analysis
   cd student_dropout_analysis
   pipenv install
   pipenv shell
   pip install -r requirements.txt
   ```

### Run Streamlit App

```
streamlit run app.py
```
Link Streamlit App Prediction: [Streamlit Web App](https://student-dropout-analysis-msyarif.streamlit.app/)

## Business Dashboard

Berdasarkan business dashboard yang telah dibuat, berikut ini adalah beberapa insight yang diperoleh:
- Siswa yang status pekerjaan orang tua baik ayah maupun ibunya masih mengenyam pendidikan dan kualifikasi orang tuanya tidak diketahui/unknown lebih berpotensi tidak mampu menyelesaikan masa studinya.
- Dari total siswa yang sudah tidak terdaftar sebagai siswa jaya-jaya institut, yang mengambil jurusan teknik informatika/informatics engineering sebesar 87% siswanya tidak berhasil lulus pada masa studinya, ini perlu menjadi perhatian khusus.
- Siswa yang memilih jenis melamar 'Berusia lebih dri 23 tahun'/*Over 23 years old* dan 'Pemegang kursus/jurusan lain yang lebih tinggi'*Holders of other higher courses* memiliki tingkat dropout yang paling tinggi dibandingkan jenis lain.
- Siswa pemegang beasiswa lebih terobsesi untuk menyelesaikan masa studinya dibandingkan siswa yang bukan pemegang beasiswa.
- Siswa yang tuition fees nya tidak up to date memiliki kecenderungan untuk dropout.
- Jumlah unit-unit kurikuler yang disetujui pada semester satu dan dua memiliki korelasi negatif dengan tingkat dropout siswa, maka semakin banyak jumlah unit-unit kurikuler siswa yang disetujui, semakin rendah kemungkinan siswa untuk dropout. Analisis korelasi ini memiliki nilai p-value < 0.05 dan R-Squared sebesar 0.54 pada semester 1 dan 0.36 pada semester 2, artinya variabel ini memiliki pengaruh yang kuat terhadap variabel dropout rate dan sebesar 36% - 54% variabilitas dari variabel 'dropout rate' dapat dijelaskan oleh variabel 'jumlah unit-unit kurikuler yang disetujui pada semester satu dan dua'.
- Sejalan dengan faktor sebelumnya, nilai unit-unit kurikuler siswa semester satu dan dua juga memiliki hubungan korelasi negatif yang kuat terhadap tingkat dropout siswa, semakin rendah nilai unit-unit kurikuler yang diperoleh siswa pada semester satu dan dua maka semakin tinggi tingkat kemungkinan untuk dropoutnya, namun variabilitas variabel dropout rate yang dapat dijelaskan oleh variabel ini hanya sebesar 7%. Selain itu terdapat temuan bahwa siswa yang memiliki nilai unit-unit kurikuler 0 pada semester satu dan dua memiliki tingkat dropout sekitar 90%. 

Link dashboard yang dapat diakses: [Tableau Dashboard Visualization](https://public.tableau.com/views/studentperformanceanalysis_17181749958020/Home?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link).

## Conclusion

Berdasarkan analisis korelasi, visualisasi, dan machine learning feature yang menjadi faktor yang berpengaruh terhadap attrition karyawan secara signifikan baik secara positif maupun negatif antara lain Curricular units 1st sem grade, Curricular units 2nd sem grade, Curricular units 1st sem approved, Curricular units 2nd sem approved, Course, dan Tuition fees up to date.

Siswa yang cenderung dropout memiliki karakteristik antara lain:
- Unit kurikulum yang disetujui berjumlah antara 0-3 dan memiliki nilai unit-unit kurikulum 0 baik pada semester 1 maupun semester 2.
- Tuition fees yang tidak up to date.
Selain itu siswa yang mengambil kursus/jurusan teknik informatika sebagian besar tidak lulus pada masa studinya.

Selain itu karakteristik tambahan yang juga dapat mempengaruhi kemungkinan siswa untuk dropout antara lain: siswa yang jenis lamaran/application mode nya memilih opsi Over 23 years old dan Holders of other higher courses, siswa yang status pekerjaan ayah maupun ibunya student/masih mengenyam pendidikan, dan siswa yang status kualifikasi ayah maupun ibunya tidak diketahui. Disamping itu siswa pemegang beasiswa pastinya lebih bertanggung jawab pada komitmen yang diambilnya sehingga lebih kecil kemungkinan untuk dropout dibandingkan yang bukan pemegang beasiswa.

### Rekomendasi Action Items

Beberapa rekomendasi aksi yang mungkin dapat dilakukan untuk memperbaiki tingkat dropout siswa antara lain:
- Kumpulkan feedback/umpan balik dari siswa mengenai kendala yang mereka hadapi terkait akademik maupun pembayaran studi.
- Identifikasi siswa yang berisiko tinggi sejak awal dan berikan bimbingan tambahan serta dukungan akademis secara intensif.
- Lakukan survei dan analisis terhadap siswa yang memiliki nilai 0.
-  Lakukan survei terhadap siswa jurusan Informatics Engineering untuk memahami alasan spesifik mereka, dan lakukan analisis lanjutan untuk mengidentifikasi faktor-faktor seperti kesulitan akademis, beban kurikulum atau faktor lain.
- Sediakan kelas remedial dan workshop untuk membantu siswa memperbaiki pemahaman dan keterampilan mereka dalam mata pelajaran yang sulit.
- Tingkatkan akses dan jumlah beasiswa atau program bantuan keuangan bagi siswa yang berisiko tinggi dropout.
- Tawarkan opsi pembelajaran yang lebih fleksibel, seperti kelas malam atau online, untuk mengakomodasi kebutuhan siswa yang mungkin memiliki komitmen lain (misalnya pekerjaan atau kursus lain). Sediakan juga jalur cepat untuk siswa yang sudah memiliki kualifikasi tinggi agar tidak perlu mengulang mata pelajaran yang sudah mereka kuasai.