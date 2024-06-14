# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.
 
### Permasalahan Bisnis

Mereka meminta bantuan untuk dibuatkan dashboard agar memduahkan mereka dalam memahami data dan memonitor performa siswa.
Selain dashboard yang diminta untuk memonitor performa siswanya, kita perlu membuat model prediction menggunakan bantuan machine learning untuk membantu mendeteksi siswa yang mungkin akan dropout berdasarkan faktor-faktor yang mempengaruhinnya secara cepat.

### Cakupan Proyek

Untuk menjawab permasalahan bisnis tersebut, pada proyek kali ini kita perlu mengetahui terlebih dahulu faktor apa saja yang menjadi penyebab tingginya tingkat dropout siswa kemudian kita buatkan web app untuk membantu memprediksi siswa berdasarkan faktor-faktor tersebut. Metode yang diterapkan antara lain Exploratory Data Analysis (EDA) yang diperkuat dengan analisis korelasi, dan model machine learning dengan penerapan hyperparmeter tuning agar memperoleh hasil yang maksimal, Algoritma machine learning yang digunakan pada hyperparameter tuning antara lain Random Forest Classifier, Gradient Boosting Classifier, dan Support Vector Classifier, kemudian dengan model terbaik yang dibuat kita terapkan function 'feature importaces' untuk mengetahui feature apa saja yang paling berpengaruh terhadap tingkat dropout siswa.

Selain itu kita juga akan membuat business dashboard menggunakan Tableau untuk memberikan insight dari data yang sedang dianalisis, dan berguna untuk memonitori feature/faktor yang mempengaruhi tingginya tingkat dropout, serta menganalisis siswa yang masih aktif/enrolled berdasarkan faktor-faktor yang terindikasi berpengaruh terhadap dropout rate.

Dan terakhir akan kita buatkan web app pada streamlit yang dapat digunakan untuk memprediksi siswa dari data yang diinput pada sistem.

### Persiapan

Sumber data: [data.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv)

Setup environment:
1. Buka file notebook.ipynb pada Google Colaboratory
2. Jalankan kode berikut
   ```
   !pip install -r requirements.txt
   ```

### Run Streamlit App

```
streamlit run app.py
```
Link Streamlit App Prediction: [attrition-predictor](https://attrition-predictor.streamlit.app/)

## Business Dashboard

Berdasarkan dashboard yang telah dibuat, berikut ini adalah beberapa insight yang diperoleh:
- Karyawan yang berumur 18-26 tahun memiliki presentase tingkat attrition yang lebih tinggi.
- gender tidak memiliki pengaruh terhadap attrition.
- Karyawan yang belum menikah memiliki tingkat attrition yang lebih tinggi dibandingkan dengan kategori lain pada status perkawinan.
- Karyawan dengan latar belakang pendidikan dibidang Technical Degree memiliki tingkat attrition tertinggi dibanding bidang lain, namun perbedaan tingkat attrition antar bidang tidak terlalu signifikan.
- Karyawan dengan pendapatan perbulan antara 1k-4k lebih memungkinkan untuk resign.
- Karyawan dengan jumlah tahun kerja kurang dari 3 tahun memiliki persentase resign lebih tinggi. *(Pada grafik ini karyawan dengan total working years 40 tahun kita abaikan karena sudah berumur kurang lebih 60 tahun, yang mana merupakan rata-rata orang berhenti bekerja)*
- Karyawan yang bekerja melebihi waktu kerja/lembur lebih mungkin untuk resign.
- Karyawan dengan tingkat level pekerjaan yang paling rendah lebih cenderung untuk resign.
- Posisi/peran pekerjaan yang memiliki tingkat presentase resign tertinggi adalah Sales Representative, perbedaannya cukup signifikan jika dibandingkan dengan peran lain.

Link dashboard yang dapat diakses: [Tableau Dashboard Visualization](https://public.tableau.com/views/studentperformanceanalysis_17181749958020/Home?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link).

## Conclusion

Berdasarkan analisis korelasi heatmap, visualisasi, dan machine learning feature yang paling berpengaruh secara signifikan baik secara positif maupun negatif terhadap attrition karyawan adalah Age, Monthly Income, OverTime, dan Total Working Years.

Karyawan yang mengalami Over Time, karyawan yang berumur muda(18-26 tahun), yang memiliki pendapatan perbulan cenderung rendah(1k-4k), dan total tahun kerja yang relatif rendah(kurang dari 3 tahunn) merupakan karakteristik karyawan yang lebih berpotensi untuk keluar dari pekerjaannya.

Selain itu karakteristik tambahan yang juga dapat mempengaruhi kemungkinan karyawan untuk resign antara lain: karyawan yang belum menikah, karyawan dengan peran/posisi sebagai Sales Representative, dan karyawan yang memiliki level pekerjaan yang rendah.

### Rekomendasi Action Items (Optional)

Beberapa rekomendasi aksi yang dapat dilakukan untuk memperbaiki tingkat attrition karyawan saat ini antara lain:  
- Perusahaan mungkin dapat memberikan jalan karir yang jelas kepada karyawan muda agar mereka merasa terdorong untuk tetap bertahan di perusahaan. Ini bisa meliputi program pengembangan, pelatihan, atau mentorship yang ditujukan khusus untuk mereka.
- Perusahaan dapat memantau dan mengatur jam kerja karyawan secara bijak agar tidak terjadi beban kerja yang berlebihan dan berpotensi menimbulkan atrisi.
- Tinjau kembali kebijakan kompensasi perusahaan untuk memastikan bahwa gaji yang ditawarkan kompetitif dan sesuai dengan kontribusi yang karyawan berikan.
- Tinjau kembali proses onboarding perusahaan untuk memastikan bahwa karyawan baru mendapatkan dukungan dan pembekalan yang cukup untuk berhasil dalam peran mereka.
- Perusahaan mungkin dapat mempertimbangkan program dukungan atau kasejahteraan karyawan seperti dukungan sosial, program mentoring, atau kegiatan sosial untuk memperkuat ikatan antarkaryawan.
- Perusahaan dapat mengidentifikasi posisi Sales Representative, kemudian kembangkan strategi retensi khusus untuk mempertahankan karyawan yang mengisi peran tersebut.
- Lakukan analisis untuk memahami kebutuhan dan harapan karyawan dengan tingkat level pekerjaan yang paling rendah.
