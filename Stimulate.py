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

    # -------------------------------
    # ตั้งค่าเริ่มต้นใน session state
    # -------------------------------
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.show_answer = False

    # -------------------------------
    # ดึงคำถามปัจจุบัน
    # -------------------------------
    quiz = quiz_data[st.session_state.quiz_index]

    st.subheader(f"Question {st.session_state.quiz_index + 1} / {len(quiz_data)}")
    st.write(quiz["question"])

    # ถ้ามี question1 → แสดงต่อทันที
    if "question1" in quiz:
        st.write(quiz["question1"])

    # แสดงภาพคำถาม
    if "image" in quiz:
        img = Image.open(quiz["image"])
        st.image(img, caption="ภาพคำถาม", use_container_width=True)

    # -------------------------------
    # ปุ่มดูเฉลย
    # -------------------------------
    if not st.session_state.show_answer:
        if st.button("✅ ดูเฉลย", key="show_answer_btn"):
            st.session_state.show_answer = True
            st.rerun()

    # -------------------------------
    # แสดงเฉลย (answer + answer1)
    # -------------------------------
    if st.session_state.show_answer:
        st.success(quiz["answer"])
        if "answer1" in quiz:
            st.success(quiz["answer1"])

        # ปุ่มไปข้อถัดไป
        if st.button("➡️ ข้อต่อไป", key="next_btn"):
            st.session_state.quiz_index += 1
            st.session_state.show_answer = False

            # ถ้าทำครบหมดแล้ว ให้รีเซ็ต
            if st.session_state.quiz_index >= len(quiz_data):
                st.session_state.quiz_index = 0
                st.success("🎉 ทำครบหมดแล้ว!")
            
            st.rerun()

# -----------------------------
# Data ทั้ง 3 หมวด
# -----------------------------
def Respiratory_lab():
    return [
        {"image": "image/Respiratory/epiglottis.jpg", "question": "พบในอวัยวะอะไร?", "answer": "Epiglottis"},
        {"image": "image//Respiratory/smooth_muscle.jpg", "question": "A:เซลล์จากภาพคือเซลล์อะไร", "answer": "smooth muscle cell"},
        {"image": "image//Respiratory/alveolar_knob.jpg", "question": "A:โครงสร้างจากภาพชื่อว่าอะไร?", "answer": "A:Alveolar knob","question1":"B:พบในไหน?","answer1":"B:terminal bronchiole"}
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
"question": "Question:เซลล์ที่ลูกศรชี้ชื่อว่าอะไร?","answer":"A:Chromophobes"
},
{
"image": "image/Endocrine_gland/follicular_cell.jpg",
"question": "Question:เซลล์ที่ลูกศรชี้มีชื่อว่าอะไร?","answer":"A:follicular cell","question1": "Question:เซลล์จากภาพมีหน้าที่อะไร?","answer1":"สร้าง thyroxine:"
},
{
"image": "image/Endocrine_gland/germinal_center_of_palatine_tonsil.jpg",
"question": "Question:โครงสร้างที่ลูกศรชี้มีชื่อว่าอะไร? ตอบแบบจำเพาะเจาะจง","answer":"A:secondary lymph phoid nodules/germinal center"
},
{
"image": "image/Endocrine_gland/herring_bodies.jpg",
"question": "Question:โครงสร้างที่ปลายลูกศรชี้มีชื่อว่าอะไร?","answer":"A:herring_bodies","question1": "Question:หน้าที่ของโครงสร้างดังกล่าวคืออะไร?","answer1":"เก็บ oxytoxin และ ADH:"
},
{
"image": "image/Endocrine_gland/islet_of_langerhans.jpg",
"question": "Question:จากภาพเป็นโครงสร้างอะไร?","answer":"A:islet of langerhans","question1": "Question:โครงสร้างจากภาพมีหน้าที่อะไร?","answer1":"สร้าง hormones/insulin/glucagon/somatostatin:"
},
{
"image": "image/Endocrine_gland/oxyphil_cell.jpg",
"question": "Question:เซลล์ดังภาพมีชื่อว่าอะไร?","answer":"A:oxyphil cell"
},
{
"image": "image/Endocrine_gland/parafollicular_cell.jpg",
"question": "Question:เซลล์ดังภาพมีชื่อว่าอะไร?","answer":"A:Parafollicular cell","question1": "Question:เซลล์จากภาพมีหน้าที่อะไร?","answer1":"สร้าง Calcitonin:"
},
{
"image": "image/Endocrine_gland/Parathyroid.jpg",
"question": "Question:โครงสร้างด้านล่างจากภาพคืออะไร?*?","answer":"A:Parathyroid"
},
{
"image": "image/Endocrine_gland/pars_distallis.jpg",
"question": "Question:โครงสร้างจากเจริญมาจากอะไร**?","answer":"A:Oral ectoderm/Ranke's Pouch"
},
{
"image": "image/Endocrine_gland/pars_glomerulosa.jpg",
"question": "Question:ชั้นจากภาพมีชื่อว่าอะไร?","answer":"A:Zona_glomerulosa"
},
{
"image": "image/Endocrine_gland/pars_nervosa.jpg",
"question": "Question:โครงสร้างจากภาพมีชื่อว่าอะไรตอบแบบจำเพาะเจาะจง**?","answer":"A:Pars nervosa"
},
{
"image": "image/Endocrine_gland/pars_tuberalis.jpg",
"question": "Question:โครงสร้างจากภาพมีชื่อว่าอะไร**?","answer":"A:pars tuberalis"
},
{
"image": "image/Endocrine_gland/Pinealocytes.jpg",
"question": "Question:เซลล์จากภาพมีชื่อว่าอะไร?","answer":"A:Pinealocytes"
},
{
"image": "image/Endocrine_gland/pituicytes.jpg",
"question": "Question:เซลล์จากภาพมีชื่อว่าอะไร","answer":"A:pituicytes"
},
{
"image": "image/Endocrine_gland/zona_fasiculata2.jpg",
"question": "Question:เซลล์ที่ลูกศรชี้ชื่อว่าอะไร details**?","answer":"A:smooth muscle cell"
},
{
"image": "image/Endocrine_gland/zona_fasiculata.jpg",
"question": "Question:เซลล์จากชั้นที่ปลายลูกศรชี้ทำหน้าที่สร้างอะไร","answer":"A:Aldosterone"
},
{
"image": "image/Endocrine_gland/zona_glomerulosa.jpg",
"question": "Question:เซลล์จากชั้นที่ปลายลูกศรชี้ทำหน้าที่สร้างอะไร?","answer":"Answer:Cortisal"
},
{
"image": "image/Endocrine_gland/zona_reticularis.jpg",
"question": "Question:เซลล์จากชั้นที่ปลายลูกศรชี้ทำหน้าที่สร้างอะไร**?","answer":"A:Androgen"
}
    ]

def Lymph_organ():
    return [
        {
"image": "image/lymph_node/capsular_lymph_node.jpg",
"question": "Question:พบในอวัยวะอะไร?","answer":"Answer:Lymph node"
},
{
"image": "image/lymph_node/central_artery.jpg",
"question": "Question:โครงสร้างที่ลูกศรชี้ชื่อว่าอะไร?","answer":"A: central_artery"
},
{
"image": "image/lymph_node/cortex.jpg",
"question": "Question:ชั้นจากภาพมีชื่อว่าอะไร?","answer":"A: Cortex"
},
{
"image": "image/lymph_node/epithelium_tonsil.jpg",
"question": "Question:โครงสร้างจากภาพมีการเรียงตัวแบบใด?","answer":"A:Stratified squamous epithelium non keratinized"
},
{
"image": "image/lymph_node/Hassal_corpuscle.jpg",
"question": "Question:โครงสร้างในภาพพบในไหน?ตอบแบบจำเพาะเจาะจง","answer":"A:medulla of lymph node"
},
{
"image": "image/lymph_node/Megakaryocyte.jpg",
"question": "Question:โครงสร้างดังภาพทำหน้าที่อะไร**?","answer":"A:develope to platelet"
},
{
"image": "image/lymph_node/medullary_lymph_node.jpg",
"question": "Question:โครงสร้างดังภาพพบในอวัยวะไหน?","answer":"A:lymph node"
},
{
"image": "image/lymph_node/reticular_cell.jpg",
"question": "Question:เซลล์ในภาพมีชื่อว่าอะไร?(ไม่น่าออก)","answer":"A:reticular cell"
},
{
"image": "image/lymph_node/secondary_lymph_node_tonsil.jpg",
"question": "Question:โครงสร้างในภาพมีชื่อว่าอะไรตอบแบบจำเพาะเจาะจง?","answer":"A:secondary lymph node"
},
{
"image": "image/lymph_node/Sinusoid_capillary.jpg",
"question": "Question:โครงสร้างดังภาพมีชื่อว่าอะไร**?","answer":"A:Sinusoid capillary"
},
{
"image": "image/lymph_node/sphenic_sinus.jpg",
"question": "Question:โครงสร้างดังภาพมีชื่อว่าอะไร**?","answer":"A:Sphenic sinus"
},
{
"image": "image/lymph_node/Thymus.jpg",
"question": "Question:โครงสร้างจากภาพพบในอวัยไหน**?","answer":"A:Thymus"
},
{
"image": "image/lymph_node/tonsillar_crypt.jpg",
"question": "Question:โครงสร้างจากปลายลูกศรชี้มีชื่อว่าอะไร**?","answer":"A:Tonsillar crypts"
},
{
"image": "image/lymph_node/trabaculae.jpg",
"question": "Question:โครงสร้างจากปลายลูกศรชี้มีชื่อว่าอะไร?","answer":"A:trabaculae"
},
{
"image": "image/lymph_node/white_pulp_in_spleen.jpg",
"question": "Question:โครงสร้างจากปลายลูกศรชี้มีชื่อว่าอะไร** ตอบแบบจำเพาะเจาะจง?","answer":"A:White pulp","question1":"โครงสร้างปลายลูกศรชี้พบในอวัยวะอะไร?","answer1":"spleen"
},
{
"image": "image/lymph_node/Yellow_bone_marrow.jpg",
"question": "Question:โครงสร้างจากภาพพบในเนื้อเยื่ออะไร?","answer":"A:Bone"
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

