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
    # ตั้งค่าเริ่มต้นใน session state และ Shuffle ข้อสอบ
    # -------------------------------
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.show_answer = False
        # สุ่มลำดับคำถามครั้งเดียวตอนเริ่มต้น
        st.session_state.shuffled_quiz = random.sample(quiz_data, len(quiz_data))

    # -------------------------------
    # ดึงคำถามปัจจุบันจาก shuffled list
    # -------------------------------
    quiz = st.session_state.shuffled_quiz[st.session_state.quiz_index]

    st.subheader(f"Question {st.session_state.quiz_index + 1} / {len(st.session_state.shuffled_quiz)}")
    st.write(quiz["question"])

    # ถ้ามี question1 → แสดงต่อทันที
    if "question1" in quiz:
        st.write(quiz["question1"])

    # แสดงภาพคำถาม (เพิ่ม error handling)
    if "image" in quiz:
        try:
            # ตรวจสอบว่าไฟล์มีอยู่จริง
            if os.path.exists(quiz["image"]):
                img = Image.open(quiz["image"])
                st.image(img, caption="ภาพคำถาม", use_container_width=True)
            else:
                st.error(f"❌ ไม่พบไฟล์ภาพ: {quiz['image']}")
                st.info("กรุณาตรวจสอบ path ของไฟล์ภาพ")
        except Exception as e:
            st.error(f"❌ เกิดข้อผิดพลาดในการโหลดภาพ: {str(e)}")

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

            # ถ้าทำครบหมดแล้ว ให้รีเซ็ตและสุ่มใหม่
            if st.session_state.quiz_index >= len(st.session_state.shuffled_quiz):
                st.session_state.quiz_index = 0
                st.session_state.shuffled_quiz = random.sample(quiz_data, len(quiz_data))
                st.success("🎉 ทำครบหมดแล้ว! สุ่มคำถามใหม่แล้ว")

            st.rerun()


# -----------------------------
# Data Section
# -----------------------------
def Respiratory_lab():
    return [
        {"image": "image/Respiratory/epiglottis.jpg", "question": "พบในอวัยวะอะไร?", "answer": "Epiglottis"},
        {"image": "image/Respiratory/smooth_muscle.jpg", "question": "A:เซลล์จากภาพคือเซลล์อะไร", "answer": "smooth muscle cell"},
        {"image": "image/Respiratory/alveolar_knob.jpg", "question": "A:โครงสร้างจากภาพชื่อว่าอะไร?", "answer": "A:Alveolar knob","question1":"B:พบในไหน?","answer1":"B:terminal bronchiole"}
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

def Urinary_system():
    return [
        {
            "image": "image/Urinary_system/Ureter.jpg",
            "question": "A:จากภาพคือโครงสร้างจากอวัยวะอะไร?",
            "answer": "Ureter"
        },
        {
            "image": "image/Urinary_system/Collecting_duct.jpg",
            "question": "A:โครงสร้างจากภาพมีการเรียงตัวแบบใด?",
            "answer": "Simple Cuboidal/Simple low cuboidal"
        },
        {
            "image": "image/Urinary_system/Ureter.jpg",
            "question": "A:โครงสร้างจากภาพคืออวัยวะอะไร?",
            "answer": "Ureter"
        },
        {
            "image": "image/Urinary_system/Vascular_pore.jpg",
            "question": "A:ตำแหน่งดังกล่าวจากภาพจะพบเซลล์อะไรได้บ้าง?",
            "answer": "Macula densa, Juxtaglomerular cell, Lacis cell (Extramesangial cell)"
        },
        {
            "image": "image/Urinary_system/Collecting_duct1.jpg",
            "question": "A:โครงสร้างจากภาพที่วงกลมสีแดงวงกลมคืออะไร?",
            "answer": "Collecting duct",
            "question1": "B:แยกได้โดย?",
            "answer1": "มีลักษณะกลมๆ, Lumen สีใส, เห็น tight junction, เรียงตัวแบบ simple cuboidal"
        },
        {
            "image": "image/Urinary_system/Female_urethra.jpg",
            "question": "A:โครงสร้างจากภาพที่ปลายลูกศรชี้คืออะไร?",
            "answer": "Female urethra",
            "question1": "B:มีการเรียงตัวแบบใด",
            "answer1": "Transitional epithelium / Urothelium"
        },
        {
            "image": "image/Urinary_system/Macula_densa.jpg",
            "question": "A:โครงสร้างจากภาพที่ปลายลูกศรชี้คืออะไร?",
            "answer": "Macula densa cell",
            "question1": "B:โครงสร้างจากปลายลูกศรชี้ทำหน้าที่อะไร?",
            "answer1": "ช่วยตรวจจับระดับ NaCl ที่ผ่าน DCT"
        },
        {
            "image": "image/Urinary_system/thin_urethra.jpg",
            "question": "A:โครงสร้างจากภาพที่ปลายลูกศรชี้คืออะไร?(ตอบแบบจำเพาะเจาะจง)",
            "answer": "Thin ascending loop of Henle"
        },
        {
            "image": "image/Urinary_system/PCT.jpg",
            "question": "A:โครงสร้างจากภาพที่ปลายลูกศรชี้คืออะไร?(ตอบแบบจำเพาะเจาะจง)",
            "answer": "Proximal convoluted tubule"
        },
        {
            "image": "image/Urinary_system/Urinary_bladder.jpg",
            "question": "A:โครงสร้างจากภาพที่ปลายลูกศรชี้คืออวัยวะอะไร?",
            "answer": "Urinary bladder"
        },
        {
            "image": "image/Urinary_system/Penis.jpg",
            "question": "A:โครงสร้างจากภาพที่ปลายลูกศรชี้คืออวัยวะอะไร?(ตอบแบบจำเพาะเจาะจง)",
            "answer": "Spongy urethra of penis",
            "question1": "B:โครงสร้างดังภาพมีการจัดเรียงตัวแบบใด?",
            "answer1": "Pseudostratified columnar epithelium"
        },
        {
            "image": "image/Urinary_system/Ureter6.jpg",
            "question": "A:โครงสร้างจากภาพที่ปลายลูกศรชี้คือชั้นอะไร?",
            "answer": "Muscularis or Muscular propria"
        },
        {
            "image": "image/Urinary_system/Urinary_bladder.jpg",
            "question": "A:โครงสร้างจากภาพคืออวัยวะอะไร?",
            "answer": "Urinary bladder"
        }
    ]

def GI_Tract_Complete_Lab():
    return [
        # 1.1 Esophagus (หลอดอาหาร)
        {
            "image": "image/GI_Tract/Esophagus1.jpg",
            "question": "A:เยื่อบุผิวที่บุหลอดอาหาร (Esophagus) มีการเรียงตัวแบบใดตาม Checklist?",
            "answer": "A:Stratified squamous non-keratinized epithelium (เยื่อบุผิวชนิด Squamous แบบมีหลายชั้นและไม่มีเคราติน)",
            "question1": "B:พบในอวัยวะอะไร?",
            "answer1": "B:Esophagus"
        },
        # 1.2 Stomach - Parietal cell
        {
            "image": "image/GI_Tract/Parietal_cell1.jpg",
            "question": "A:เซลล์จากลูกศรชี้ชื่อเซลล์อะไร?",
            "answer": "A:Parietal cell (Oxyntic cell)",
            "question1": "B:ตาม Checklist เซลล์นี้สร้างสารสำคัญอะไรอีกบ้าง?",
            "answer1": "B:Intrinsic factor + HCl"
        },
        # 1.2 Stomach - Chief cell
        {
            "image": "image/GI_Tract/Chief_cell.jpg",
            "question": "A:เซลล์จากปลายลูกศรชี้มีหน้าที่อะไร?",
            "answer": "A:Pepsinogen + Gastric lipase"
        },
        # 1.3 Small Intestine - Surface absorptive
        {
            "image": "image/GI_Tract/Surface_absorbtive.jpg",
            "question": "A:เซลล์จากปลายลูกศรชี้คือเซลล์อะไร?",
            "answer": "A:Surface absorptive cell"
        },
        # 1.3 Small Intestine - Duodenum (Brunner's glands)
        {
            "image": "image/GI_Tract/Duodenum_Brunner_glands.jpg",
            "question": "A:โครงสร้างที่ลูกศรชี้คืออะไร?",
            "answer": "A:Brunner's glands",
            "question1": "B:โครงสร้างนี้ทำหน้าที่สร้างอะไร?",
            "answer1": "B:Alkaline mucin"
        },
        # 1.3 Small Intestine - Jejunum
        {
            "image": "image/GI_Tract/Jejunum.jpg",
            "question": "A:จากภาพดังกล่าวคืออวัยวะอะไร?",
            "answer": "A:Jejunum",
            "question1": "B:รู้ได้อย่างไร?",
            "answer1": "B:มี long villi ไม่มี Brunner's glands"
        },
        # 1.3 Small Intestine - Ileum
        {
            "image": "image/GI_Tract/Ileum.jpg",
            "question": "A:โครงสร้างที่ลูกศรชี้คือกลุ่มก้อนของอะไร?",
            "answer": "A:Peyer's patches"
        },
        # 1.4 Large intestine
        {
            "image": "image/GI_Tract/Colon.jpg",
            "question": "A:การเรียงตัวของโครงสร้างดังกล่าวเป็นแบบใด?",
            "answer": "A:Simple columnar epithelium with many goblet cells",
            "question1": "B:โครงสร้างที่ลูกศรชี้ทำหน้าที่อะไร?",
            "answer1": "B:สร้างเมือก"
        },
        # 1.5 Appendix
        {
            "image": "image/GI_Tract/Appendix.jpg",
            "question": "A:โครงสร้างดังภาพคืออวัยวะอะไร?",
            "answer": "A:Appendix",
            "question1": "B:รู้ได้อย่างไร?",
            "answer1": "B:มี lumen ขนาดเล็กครบวงและมี lymphatic nodules"
        },
        # 1.6 Anus
        {
            "image": "image/GI_Tract/Anus.jpg",
            "question": "A:จากภาพพบการเรียงตัวแบบใด?",
            "answer": "A:Stratified squamous keratinized epithelium",
            "question1": "B:โครงสร้างดังกล่าวพบในอวัยวะอะไร?",
            "answer1": "B:Anus"
        },
        # 2.1 Liver - Portal Triad
        {
            "image": "image/GI_Tract/Liver.jpg",
            "question": "A:โครงสร้างจากภาพคืออะไร? (ตอบแบบจำเพาะเจาะจง)",
            "answer": "A:Hepatic artery",
            "question1": "B:โครงสร้างดังกล่าวพบในบริเวณใด?",
            "answer1": "B:Portal triad or portal area"
        },
        # 2.1 Liver - Kupffer cells
        {
            "image": "image/GI_Tract/Kupffer_cell.jpg",
            "question": "A:เซลล์จากปลายลูกศรชี้คือเซลล์อะไร?",
            "answer": "A:Kupffer cells",
            "question1": "B:เซลล์จากปลายลูกศรชี้ทำหน้าที่อะไร?",
            "answer1": "B:ทำหน้าที่เป็น macrophage ทำลาย bacteria"
        },
        # 2.2 Small intestine - Paneth cell
        {
            "image": "image/GI_Tract/Paneth_cell.jpg",
            "question": "A:เซลล์จากลูกศรชี้คืออะไร?",
            "answer": "A:Paneth cell",
            "question1": "B:ทำหน้าที่สร้างอะไร?",
            "answer1": "B:Lysozyme"
        },
        # 2.3 Pancreas
        {
            "image": "image/GI_Tract/Centroacinar_cell.jpg",
            "question": "A:เซลล์จากภาพคืออะไร?
