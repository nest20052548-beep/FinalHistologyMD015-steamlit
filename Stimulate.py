import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import os

# -----------------------------
# ฟังก์ชันเขียนข้อความภาษาไทยบนภาพ
# -----------------------------
def put_thai_text(image_path, text, font_path="THSarabunNew.ttf", font_size=36, color=(0, 255, 0)):
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    draw.text((30, 30), text, fill=color, font=font)
    return img

# -----------------------------
# ฟังก์ชันหลักแสดงคำถาม
# -----------------------------
def run_quiz(quiz_data, topic_name):
    st.header(f"🧠 Quiz: {topic_name}")

    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.show_answer = False

    quiz = quiz_data[st.session_state.quiz_index]
    st.subheader(f"Question {st.session_state.quiz_index + 1} / {len(quiz_data)}")
    st.write(quiz["question"])

    img = Image.open(quiz["image"])
    st.image(img, caption="ภาพคำถาม", use_container_width=True)

    # ปุ่มโชว์เฉลย
    if st.button("✅ ดูเฉลย"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        st.success(quiz["answer"])
        if "question1" in quiz and "answer1" in quiz:
            st.write(quiz["question1"])
            st.success(quiz["answer1"])

        if st.button("➡️ ข้อต่อไป"):
            st.session_state.quiz_index += 1
            st.session_state.show_answer = False
            if st.session_state.quiz_index >= len(quiz_data):
                st.session_state.quiz_index = 0
                st.success("🎉 ทำครบหมดแล้ว!")

# -----------------------------
# Data ทั้ง 3 หมวด
# -----------------------------
def Respiratory_lab():
    return [
        {"image": "image/epiglottis.jpg", "question": "พบในอวัยวะอะไร?", "answer": "Epiglottis"},
        {"image": "image/Seromunicous_gland.jpg", "question": "What is Role of this structure?", "answer": "Secrete mucous and water substance"},
        {"image": "image/alveolar_knob.jpg", "question": "What is this structure name?", "answer": "Alveolar knob"},
    ]

def Endocrine_Gland_Lab():
    return [
        {
"image": "image/Endocrine_gland/Adrenal_gland.jpg",
"question": "Question:จากภาพเป็นโครงสร้างอะไร?","answer":"A: Adrenal_gland"
},
{
"image": "image/Endocrine_gland/anterior_pituitary_gland.jpg",
"question": "Question:จากภาพเป็นโครงสร้างอะไร?","answer":"A:Pars Distallis"
},
{
"image": "image/Endocrine_gland/Brain_cell.jpg",
"question": "Question:จากภาพเป็นโครงสร้างอะไร?","answer":"A:Copora arenacea/Brain cell"
},
{
"image": "image/Endocrine_gland/Capsule_in_adrenal_gland.jpg",
"question": "Question:โครงสร้างนี้ทำหน้าที่สร้างฮอร์โมนอะไร?**?","answer":"A:Norephinreephrine,cortisal,aldoesteron,androgen2"
},
{
"image": "image/Endocrine_gland/cheif_cell.jpg",
"question": "Question:เซลล์จากปลายลูกศรชี้มีชื่อว่าอะไร?**?","answer":"A:cheif cell","question1": "Question:เซลล์จากปwลายลูกศรชี้มีหน้าที่สร้างอะไร**?","answer1":"A:Parathormone"
},
{
"image": "image/Endocrine_gland/Chromophobes.jpg",
"question": "Question:What is cell name?","answer":"A:Chromophobes"
},
{
"image": "image/Endocrine_gland/follicular_cell.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/germinal_center_of_palatine_tonsil.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/herring_bodies.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/islet_of_langerhans.jpg",
"question": "Question:จากภาพเป็นโครงสร้างอะไร?","answer":"A:islet of langerhans"
},
{
"image": "image/Endocrine_gland/oxyphil_cell.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/parafollicular_cell.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/Parathyroid.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/pars_distallis.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/pars_glomerulosa.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/pars_nervosa.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/pars_tuberalis.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/Pinealocytes.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/pituicytes.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/zona_fasiculata2.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/zona_fasiculata.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/zona_glomerulosa.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/zona_reticularis.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
}
    ]

def Lymph_organ():
    return [
        {
"image": "image/lymph_node/capsular_lymph_node.jpg",
"question": "Question:พบในอวัยวะอะไร?","answer":"Answer: Epiglosttis"
},
{
"image": "image/lymph_node/central_artery.jpg",
"question": "Question:What is Role of this structure?","answer":"A: Secrete mucous and water substance"
},
{
"image": "image/lymph_node/cortex.jpg",
"question": "Question:What is this structure name?","answer":"A: Alveolar knob"
},
{
"image": "image/lymph_node/epithelium_tonsil.jpg",
"question": "Question:What is this structure name?","answer":"A:Terminal_bronchiole"
},
{
"image": "image/lymph_node/Hassal_corpuscle.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/Megakaryocte.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/medullary_lymph_node_tonsil.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/reticular_cell.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/seondary_lymph_node_tonsil.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/Sinusoid_capillary.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/sphenic_sinus.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/Thymus.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/tonsillar_crpt.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/trabaculae.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/white_pulp_n_spleen.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/lymph_node/Yellow_bone_marrow.jpg",
"question": "Question:What is cell name details**?","answer":"A:smooth muscle cell"
}
    ]

# -----------------------------
# ส่วนของ Streamlit App
# -----------------------------
st.title("🔬 Histology Quiz Viewer")
st.sidebar.header("เลือกหมวดที่ต้องการทบทวน")

choice = st.sidebar.selectbox(
    "เลือกหมวด",
    ["Respiratory", "Lymph_organ", "Endocrine"]
)

if choice == "Respiratory":
    run_quiz(Respiratory_lab(), "Respiratory System")
elif choice == "Lymph_organ":
    run_quiz(Lymph_organ(), "Lymphoid Organs")
elif choice == "Endocrine":
    run_quiz(Endocrine_Gland_Lab(), "Endocrine Glands")