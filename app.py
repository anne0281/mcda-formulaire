import streamlit as st

st.set_page_config(page_title="Evaluation MCDA", layout="wide")

st.title("Evaluation médicament - Formulaire thérapeutique")

password = st.text_input("Mot de passe", type="password")

if password != "mcda123":
    st.stop()

st.header("Informations médicament")

drug = st.text_input("Nom du médicament")
indication = st.text_input("Indication")

st.header("Evaluation clinique")

c1 = st.slider("Bénéfice clinique",0,5)
c2 = st.slider("Qualité des études",0,5)

score_clinique = c1 + c2

st.header("Evaluation économique")

e1 = st.slider("Impact budgétaire",0,5)
e2 = st.slider("Coût comparateur",0,5)

score_eco = e1 + e2

st.header("Logistique")

l1 = st.slider("Stockage",0,5)
l2 = st.slider("Distribution",0,5)

score_log = l1 + l2

score_total = score_clinique + score_eco + score_log
score_percent = (score_total/30)*100

st.header("Résultat")

st.write("Score clinique :",score_clinique)
st.write("Score économique :",score_eco)
st.write("Score logistique :",score_log)

st.subheader(f"Score total : {round(score_percent,1)} %")

if score_clinique < 5:
    st.error("REFUS : score clinique insuffisant")

elif score_eco < 5:
    st.error("REFUS : score économique insuffisant")

elif score_percent > 50:
    st.success("ACCEPTÉ au formulaire thérapeutique")

else:
    st.warning("REFUS : score total insuffisant")
