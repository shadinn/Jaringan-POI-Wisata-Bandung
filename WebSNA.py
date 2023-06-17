import streamlit as st

def create_caption(caption):
    # Membagi caption menjadi beberapa baris
    lines = caption.split('\n')

    # Menambahkan enter di antara setiap baris
    caption_with_line_break = "<br>".join(lines)

    # Menampilkan caption menggunakan elemen markdown
    st.markdown(f"{caption_with_line_break}", unsafe_allow_html=True)


# Layout 
st.set_page_config(
    page_title = 'SNA',
    page_icon = '✅',
    layout = 'wide'
)


st.title('Jaringan POI Destinasi Wisata Bandung')
st.caption('Selain dikenal sebagai Paris Van Java dan Kota Kembang, Bandung pun dijuluki The Most European City in The East Indies, Bandung Excelsior, Intelectuele Centrum Van Indie, Europe in The Tropen, Kota Permai, Kota Pendidkan, Kota Kreatif hingga Kota Kuliner. Kota yang dikelilingi pegunungan ini memang menyimpan berjuta keindahan alam. Tidak hanya itu, berbagai macam destinasi wisata menarik mulai dari tempat kuliner sampai tempat rekreasi bisa ditemukan di Bandung.')
datach, capt = st.columns(2)
with datach :
    st.write('Jumlah Kunjungan Wisatawan 2018 - 2021')
    st.markdown('<iframe src="https://flo.uri.sh/visualisation/14165936/embed" width="100%" height="400px" frameborder="0" scrolling="no"></iframe>', unsafe_allow_html=True)
    
with capt :

    caption1 ="""
    <br> Banyaknya pilihan destinasi di Bandung menyebabkan tingginya animo wisatawan baik lokal maupun asing untuk mengunjungi Bandung. Keadaan sebelum pandemi menunjukan setiap tahunnya dari tahun 2018 s/d 2019 menaik, dengan jumlah wisatawan domestik tertinggi mencapai 10 juta wisatawan pada tahun 2019. Semasa Pandemi jumlah wisatawan domestik dan mancanegara menurun drastis. Pada tahun 2020 terjadi penurunan lebih dari 30% dari tahun sebelumnya. 
    <br> Kini, setelah pandemi mulai reda, sektor pariwisata di Bandung mulai bangkit lagi. Dimulai dari tahun 2022 peningkatan jumlah wisatawan mulai terjadi di Bandung Raya. Menteri Pariwisata dan Ekonomi Kreatif (Kemenparekraf), Sandiaga Salahuddin Uno menyebut, Bandung Raya adalah salah satu wilayah dengan tingkat kunjungan wisatawan yang tinggi di Indonesia, yaitu mencapai 700 juta di tahun 2022. 
    """
    create_caption(caption1)

tab1,tab2,tab3 = st.tabs(['Jaringan POI','Community','Centrality'])

with tab1:
    st.markdown('<iframe src="https://flo.uri.sh/visualisation/14165940/embed" width="800px" height="400px" frameborder="0" scrolling="no"></iframe>', unsafe_allow_html=True)
    st.caption('Terdapat 1250 Jaringan POI destinasi wisata yang terbentuk. Dengan jarak kurang dari 3 km, ada kumpulan jaringan POI yang paling besar dan diisi oleh beragam jenis POI. Sedangkan, jaringan POI disekitarnya lebih banyak diisi oleh PO jenis rekreasi.')

with tab2:
    st.caption('Modularity merupakan cara untuk mendapatkan komunitas pada jaringan berdasarkan interaksi antar node dan edge')
    st.markdown('<iframe src="https://flo.uri.sh/visualisation/14165944/embed" width="800px" height="400px" frameborder="0" scrolling="no"></iframe>', unsafe_allow_html=True)
    st.caption('Banyaknya kelompok kecil yang terbentuk dalam jaringan POI, mengindikasikan terdapat beberapa kelompok/komunitas yang terbentuk')
    st.subheader('Interpretasi Hasil Modularity Community')
    st.markdown('<iframe src="https://flo.uri.sh/visualisation/14165937/embed" width="100%" height="400px" frameborder="0" scrolling="no"></iframe>', unsafe_allow_html=True)

with tab3:
    st.caption('Analisis Jaringan dilakukan dengan melihat beberapa komponen social network analysis')
    vis, int = st.columns(2)
    with vis:
        st.markdown('<iframe src="https://flo.uri.sh/visualisation/14165943/embed" width="100%" height="400px" frameborder="0" scrolling="no"></iframe>', unsafe_allow_html=True)
    with int :
        st.markdown('<iframe src="https://flo.uri.sh/visualisation/14166107/embed" width="100%" height="400px" frameborder="0" scrolling="no"></iframe>', unsafe_allow_html=True)