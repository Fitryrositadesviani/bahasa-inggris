import streamlit as st
import random

# --- Fungsi untuk Memuat Konten Markdown dari File ---
def load_markdown_content(filepath):
    """
    Memuat konten dari file Markdown.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"File '{filepath}' tidak ditemukan."

# --- Fungsi untuk Bagian Materi (Content Section) ---
def show_material_section():
    """
    Menampilkan berbagai ringkasan materi TOEFL.
    """
    st.title("📚 Ringkasan Materi TOEFL")
    st.write("Di sini Anda bisa menemukan rangkuman penting untuk meningkatkan pemahaman TOEFL Anda.")

    # Menggunakan tabs untuk memisahkan materi
    tab_grammar, tab_vocabulary, tab_strategies = st.tabs(["Grammar", "Kosakata", "Strategi Umum"])

    with tab_grammar:
        st.header("📝 Grammar Essentials")
        st.markdown(load_markdown_content("content/grammar.md"))
        st.info("Pelajari lebih lanjut tentang grammar untuk memastikan struktur kalimat yang benar.")

    with tab_vocabulary:
        st.header("📖 Vocabulary Boost")
        st.markdown(load_markdown_content("content/vocabulary.md"))
        st.info("Perkaya kosakata Anda dengan daftar kata-kata penting TOEFL.")

    with tab_strategies:
        st.header("💡 TOEFL Strategies")
        st.markdown(load_markdown_content("content/strategies.md"))
        st.info("Pahami strategi efektif untuk setiap bagian ujian TOEFL.")

# --- Fungsi untuk Bagian Latihan (Practice Section) ---
def show_practice_section():
    """
    Menampilkan latihan TOEFL sederhana.
    """
    st.title("🎯 Latihan TOEFL")
    st.write("Asah kemampuan Anda dengan latihan-latihan berikut.")

    practice_options = ["Reading Comprehension", "Listening (Coming Soon)", "Speaking (Coming Soon)", "Writing (Coming Soon)"]
    selected_practice = st.selectbox("Pilih Jenis Latihan:", practice_options)

    if selected_practice == "Reading Comprehension":
        st.subheader("Bacaan Teks Pendek")
        text = """
        The Great Barrier Reef, located off the coast of Queensland, Australia, is the world's largest coral reef system. It is composed of over 3,000 individual reefs and 900 islands stretching for over 2,300 kilometers. This natural wonder is home to an incredible diversity of marine life, including various species of fish, sharks, turtles, and colorful corals. Despite its immense size and beauty, the Great Barrier Reef faces significant threats from climate change, ocean acidification, and pollution. Conservation efforts are crucial to protect this irreplaceable ecosystem for future generations.
        """
        st.write(text)

        st.subheader("Pertanyaan:")
        questions = [
            {
                "question": "Di mana Great Barrier Reef berada?",
                "options": ["Afrika Selatan", "Australia", "Brazil", "Kanada"],
                "answer": "Australia"
            },
            {
                "question": "Berapa panjang Great Barrier Reef?",
                "options": ["Kurang dari 1.000 km", "Sekitar 1.500 km", "Lebih dari 2.300 km", "Tidak disebutkan"],
                "answer": "Lebih dari 2.300 km"
            }
        ]

        # Simpan state jawaban pengguna
        if 'answers' not in st.session_state:
            st.session_state.answers = {}

        for i, q in enumerate(questions):
            st.markdown(f"**{i+1}. {q['question']}**")
            user_choice = st.radio(f"Pilih jawaban untuk pertanyaan {i+1}:", q['options'], key=f"q_{i}")
            st.session_state.answers[f"q_{i}"] = user_choice

        if st.button("Periksa Jawaban"):
            correct_count = 0
            st.subheader("Hasil Anda:")
            for i, q in enumerate(questions):
                user_answer = st.session_state.answers.get(f"q_{i}")
                if user_answer == q['answer']:
                    st.success(f"Pertanyaan {i+1}: Benar! ({q['answer']})")
                    correct_count += 1
                else:
                    st.error(f"Pertanyaan {i+1}: Salah. Jawaban Anda: '{user_answer}'. Jawaban Benar: '{q['answer']}'")
            st.markdown(f"---")
            st.write(f"**Anda menjawab {correct_count} dari {len(questions)} pertanyaan dengan benar.**")

    elif selected_practice == "Listening (Coming Soon)":
        st.info("Fitur latihan mendengarkan akan segera hadir! Nantikan pembaruan.")
    elif selected_practice == "Speaking (Coming Soon)":
        st.info("Fitur latihan berbicara akan segera hadir! Nantikan pembaruan.")
    elif selected_practice == "Writing (Coming Soon)":
        st.info("Fitur latihan menulis akan segera hadir! Nantikan pembaruan.")

# --- Bagian Utama Aplikasi ---
st.sidebar.title("Navigasi Aplikasi")
app_mode = st.sidebar.radio("Pilih Mode:", ["Materi TOEFL", "Latihan TOEFL"])

if app_mode == "Materi TOEFL":
    show_material_section()
else:
    show_practice_section()

st.sidebar.markdown("---")
st.sidebar.info("Aplikasi ini dibuat untuk membantu Anda meningkatkan skor TOEFL.")