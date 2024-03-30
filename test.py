import streamlit as st

st.title ('test running streamlit')
st.write ("hello **world**!")
st.markdown ("hello **wolrld**!")
st.title('_mang ea_ is :blue[cool]')
st.title('_Raden Rai_ is :red[gayat]')
st.write("selamat **pagi**!")
st.title('_belajar_:blue[streamlit]')
st.markdown("selamat **pagi**")
st.write('nama saya raden raishita,sedang belajar streamlit')
import streamlit as st

st.write('Hello, *World!* :sunglasses:')
st.header("Aplikasi Penjumlahan Bilangan Numerik", divider='rainbow')
angka_pertama=st.number_input('masukkan angka pertama')
st.write('the_current_number_is,' ,angka_pertama)
angka_kedua=st.number_input('masukkan angka kedua')
st.write('the_current_number_is,' ,angka_kedua)
operasi_matematika = angka_pertama*angka_kedua
st.write(f'angka pertama {angka_pertama} x angka kedua {angka_kedua} = {operasi_matematika}')