# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:32:02 2022

@author: etien
"""
from pathlib import Path
import streamlit as st 
from PIL import Image
import base64
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention



st.set_page_config(
    page_title="Etienne's Portfolio",
    page_icon="fallen_leaf",
    layout="centered",
    )


def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    
    st.markdown(pdf_display, unsafe_allow_html=True)



# --- ENGAGEMENT MENU ---

EXAMPLE_NO = 2


def mainENG(example=2):
    
    if example == 2:
        selected = option_menu(
            menu_title=None,  # required
            options=[ "Associatif", "Centres d'intérêt", "Animation"],  # required
            icons=["megaphone", 'brightness-alt-high', "gear"],  # optional
            orientation="horizontal",
            )
        return selected



# --- PATH SETTINGS ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
css_file2 = current_dir / "styles" / "style.css"
css_file3 = current_dir / "styles" / "page1.css"
resume_file = current_dir / "assets" / "ERALECcvfr.pdf"
profile_pic = current_dir / "assets" / "profile-pic2.png"
pic1 = current_dir / "assets" / "hackathon.jpg"
rapportdestage1 = current_dir / "assets" / "Prépa_2024_Stage_1ere_annee_RALEC_Etienne.pdf"
rapportdestage2 = current_dir / "assets" / "IR_2024_Stage_ING_3_RALEC_Etienne.pdf"
colo_pic = current_dir / "assets" / "COLO.jpg"
buddypic = current_dir / "assets" / "Buddy.png"
ridein_pic = current_dir / "assets" / "RideIN.jpg"
bdgpic = current_dir / "assets" / "logoBDG.png"
moipic = current_dir / "assets" / "DALLEE.png"
moiinsta = current_dir / "assets" / "moiinsta.png"
fleur = current_dir / "assets" / "fleur.png"
peche = current_dir / "assets" / "pechepeche.png"
ho = current_dir / "assets" / "hohochateau.png"
camp = current_dir / "assets" / "campcamp.png"
anim = current_dir / "assets" / "anim.png"
velo = current_dir / "assets" / "velo.png"
pote = current_dir / "assets" / "copains.png"
HU = current_dir / "assets" / "HU.png"
bpmwatch = current_dir / "assets" / "BPMaverageYear.png"
bins = current_dir / "assets" / "districtbins.png"
crypto = current_dir / "assets" / "crypto.png"
streamlit = current_dir / "assets" / "streamlitdash.png"
vtt = current_dir / "assets" / "vtt.jpg"
cap = current_dir / "assets" / "rennesmarathon.jpg"

def main():
    

    st.sidebar.title("Mon portfolio")
    page = st.sidebar.radio("Selectionnez une page",
       ("A propos de moi 👀", "CV 📃", "Mon projet professionnel 🧑‍💻", "Projets 💻",
        "Expériences 👨‍🏭","Mes engagements 🚴‍♂️","Mes compétences 🏋️‍♂️" , "Me contacter 👈")
       )
    
    
    if page == "A propos de moi 👀":
        moi(moipic, moiinsta, fleur, peche, ho, camp, anim, velo, pote, HU)
        
    elif page =="CV 📃":
        home(profile_pic)
        
    
    elif page == "Mon projet professionnel 🧑‍💻":
        monprojet()
    
    elif page == "Projets 💻":
        portfolio(pic1,  bpmwatch, bins, crypto, streamlit)
    
    elif page == "Mes compétences 🏋️‍♂️":
        competences()

    elif page == "Mes engagements 🚴‍♂️":
        hobbies(bdgpic, ridein_pic, buddypic, vtt, cap)
        
    
    elif page == "Me contacter 👈":
        contact()
        
    elif page == "Expériences 👨‍🏭":
        experience(colo_pic)


def moi(moipic, moiinsta, fleur, peche, ho, camp, anim, velo, pote, HU):
    
    NAME = "Etienne Ralec"
    
    with open(css_file3) as f:
                st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
  
    moipic = Image.open(moipic)
    moiinsta = Image.open(moiinsta)
    fleur = Image.open(fleur)
    peche = Image.open(peche)
    ho = Image.open(ho)
    camp = Image.open(camp)
    anim = Image.open(anim)
    velo = Image.open(velo)
    pote = Image.open(pote)
    HU = Image.open(HU)
            
    col1, col2 = st.columns(2, gap="small")
    with col1:
            st.image(moiinsta, width=230)

    with col2:
            st.header(NAME)
            st.write('**3** publications **443** followers **581** suivi(e)s')
            st.write("""
                
             Passionné de Course à Pied et de VTT. J'aime me perdre dans les grands espaces.
        
             """) 
            
    st.write(" ")
    
    col1, col2, col3, col4, col5, col6 = st.columns(6, gap="small")
    with col1:
            st.image(anim, caption='📣')

    with col2:
            st.image(velo, caption='🚲')
    
    with col3:
            st.image(camp, caption="🇫🇮/🏕️/🇳🇴")
         
    with col4:
            st.image(ho, caption="🇳🇱")
      
    with col5:
           st.image(fleur, caption='🌺')
           
    with col6:
          st.image(peche, caption='🎣')
        
             
    st.write("---")
    
    
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
            st.image(moipic, caption='DALL-E drip')

    with col2:
            st.image(pote, caption='Direction Bruxelles avec Julio et Pontus')
    
    with col3:
            st.image(HU, caption='Big Data à Hogeschool Utrecht')
            
                     


def home(profile_pic):
        
        


        # --- GENERAL SETTINGS ---

        NAME = "Etienne Ralec"

        EMAIL = "etienneralec@email.com"
        SOCIAL_MEDIA = {
            "YouTube": "https://youtube.com",
            "LinkedIn": "https://www.linkedin.com/in/etienne-ralec-esaip/",
            "GitHub": "https://github.com/tienou29",
            "Twitter": "https://twitter.com",
            }

        PROJECTS = {
            "Notebook - Design of a data driven app 📱 ": "https://github.com/tienou29/vivepakitest/blob/master/CarteRESULT.ipynb",
            "Notebook - Machine Learning Apple Watch ⌚": "https://github.com/tienou29/vivepakitest/blob/master/FinalAssignmentEtienneRALEC.ipynb",
              
            }
    
        # --- LOAD CSS, PDF & PROFIL PIC ---
        with open(css_file) as f:
                    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
        with open(resume_file, "rb") as pdf_file:
                PDFbyte = pdf_file.read()
                profile_pic = Image.open(profile_pic)
                


        # --- HERO SECTION ---
        col1, col2 = st.columns(2, gap="small")
        with col1:
                st.image(profile_pic, width=230)

        with col2:
                st.title(NAME)
                st.write('''<div style="text-align: justify;">Etudiant ingénieur en intelligence artificielle, je suis à la recherche d'un stage de 3 mois à partir du 01/06/2022</div>''', unsafe_allow_html=True)
                st.write('')     
                st.download_button(
                    label=" 📄 Download CV",
                    data=PDFbyte,
                    file_name=resume_file.name,
                    mime="application/octet-stream",
                    )
                st.write("📫", EMAIL)
                
        # --- SOCIAL LINKS ---
        st.write('\n')
        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f"[{platform}]({link})")


        # --- EXPERIENCE & QUALIFICATIONS ---
        st.write('\n')
        st.subheader("Formations")
     
        st.write(" ⏳ ESAIP 2021-2024 Cycle ingénieur numérique")
        
        st.write("""
                    - ▶️ Intelligence Artificielle, Réseaux, Programmation
                
                    - ▶️ Hackathon Design For Green
                
                    - ▶️ Developpement Jeu de Plateau / Java
                
                    - ▶️ Initiation à la recherche
                """)
        
                
        st.write('✔️ University of Applied Sciences Utrecht 2022 Big Data for Smart Media and Bussiness')
        
        st.write('''
                    - ▶️ Collection de données ; Algorithmes ; visualisation ; streamlit dashboard ; 
                    - ▶️ Smart media and data driven business
                 ''')
                 
        st.write('✔️ Riga Technical University 2021 Cross-cultural Communication Summer Camp')
        
        st.write('''
                    - ▶️ Objectifs SMART
                     
                    - ▶️ Communication orale
                 
                 ''')
       
        st.write('✔️ ESAIP 2019-2021 Cycle préparatoire anglophonne')
            
        st.write('''
                    - ▶️ Analyse, Algbèbre, Géométrie, Physique, Chimie
                    - ▶️ Python, C, Linux, 
                    - ▶️ Latex
            
                ''')
            
        # --- SKILLS ---
        st.write('\n')
        st.subheader("Compétences")
        
        st.write('**Savoirs**')
        
        st.write(
            """
            - 👩‍💻 Langage de programmation : Python ; JAVA ; HTML / CSS ; C 
            - 📊 Big Data : Python (Scikit-learn, Pandas, Streamlit, MatplotLib, Seaborn), UX and UI design, Interfaces intelligente
            - 📚 IA : Reconnaissance et Vision ; Visualisation ; Machine Learning
            - 🗄️ Logiciels : XAMPP ; MatLab ; Tableau ; Excel ; Figma
            - 🗺️ Langues et certifications : Anglais (First Certification of Cambridge B2 ; TOEIC 925 B2) ; Espagnol (B1) ; Japonais (Notions) ; Néerlandais (Notions)
            """
            )
        
        st.write('**Savoir-être**')
        st.write('confiant, organisé, esprit de collaboration, consciencieux')
        
        # --- WORK HISTORY ---
        st.write(' ')
        st.subheader("Expériences")
        st.write("---")
        
        # --- JOB 1
        st.write(' ')
        st.write("🚧", "**Runner | Mc Donald's | Pays-Bas**")
        st.write("2022")
        st.write(
            """
            - ► Prendre l'initiative de trouver des tâches supplémentaires lorsque lestâches prévues sont terminées.
            - ► Observations des enjeux numériques
            """)
            
        # --- JOB 2
        st.write(' ')
        st.write("🚧", "**Developpement Web | Welko | France**")
        st.write("Juillet 2020")
        st.write(
            """
            - ► HTML / CSS ; APACHE
            - ► Réalité Augmentée
            - ► UX / UI design
        
            """)
            
            
        # --- JOB 3
        st.write(' ')
        st.write("🚧", "**Animateur 10 - 14 ans | AVEA / IGESA / Les PEP | France**")
        st.write("2018 - 2022")
        st.write(
            """
            - ► Garantir la sécurité physique, morale et affective des enfants
            - ► RCréer et organiser des activités originales (management prévisionnel et organisationnel)
            - ► Mettre en place et surveiller la baignade
        
            """)
        
        
        
    
        # --- Projects  ---
        st.write(' ')
        st.subheader("Projets")
        st.write("---")
        for project, link in PROJECTS.items():
            st.write(f"[{project}]({link})")
        

   

def monprojet():
    st.title('Mon projet professionnel')
    
    st.subheader('Quel est mon projet professionel ?')
    st.markdown('''<div style="text-align: justify;">
        Ma formation actuelle m’apporte un bagage de connaissances en sciences de 
        l’informatique notamment en Big Data et en Intelligence Artificielle.
        </div>''', unsafe_allow_html=True)
    st.text('')  
        
    st.markdown('''<div style="text-align: justify;">
        Pendant mon semestre à HU l’université de sciences appliquées d’Utrecht, j’ai réalisé de nombreux projets individuels et en équipe sur la visualisation des données. 
        J’ai accompli un beau travail en créant un modèle prédictif de pertes caloriques 
        en récupérant et exploitant les données de ma montre connectée. 
        Suite à ce projet, le Machine Learning m’ayant beaucoup passionné j’ai décidé de 
        continuer vers l’intelligence Artificielle une fois de retour en France.         
        </div>''', unsafe_allow_html=True)
    st.text('')   
        
    st.markdown('''<div style="text-align: justify;">      
        J'attache de l'importance à la recherche, à la
        conception et au développement de produits répondant aux enjeux
        sociétaux. J'ambitionne de poursuivre ma formation en alternance car
        c'est un moyen efficace d’acquérir des connaissances pratiques et
        théoriques sur le terrain auprès de professionnels expérimentés. Si possible 
        dans la conception de système embarqué ou d'objets connectés guidés par l'IA.</div>''', unsafe_allow_html=True)
    
    st.text('')
    st.subheader('Comment est-ce que je me vois dans 5 ans ?')
    
    st.markdown('''<div style="text-align: justify;">      
        Je me vois en entreprise. Mon but sera encore de continuer d'acquérir de nombreuses compétences. 
        C'est à dire perfectionner mes compétences actuelles en data et intelligence artificielle par la
        réalisation de projets en lien avec : le traitement des signaux/ données, l'apprentissage et vision, le machine learning, la visualisation... 
        Et d'autre part devenir ingénieur full stack.</div>''', unsafe_allow_html=True)
    st.text('')
    
    st.markdown('''<div style="text-align: justify;">      
        Je me vois en effet en entreprise à travailler dans une équipe joyeuse et soudé.
        Je considère qu'il est important d'avoir un bon équilibre de vie entreprise/ sports & aventures / familles...</div>''', unsafe_allow_html=True)



def competences():
  
    
    st.title("Mes compétences")
    
    def main_page():
        st.subheader("Intelligence Artificielle")
        st.markdown('''
                 
                 Computer Vision : 
                     
                     - Find the number of people wearing chirurgical mask 
                       in one picture
                     
                Certification : 
                    
                    - Microsoft Azure AI Fundamentals
                
                 
                 ''')
        

            
    def pagescience():
        st.subheader("Sciences")
        
        st.markdown("""
                    - Traitements des Images / Signaux 
                    - Réseau de Pétrie 
                    - Analyse 
                    - Algbèbre 
                    - Géométrie 
                    - Physique 
                    - Chimie
                    """)
        
    def langue():
        st.subheader("Langues et certifications")
        st.markdown("""
                   
                   **Anglais B2** 
                       
                       First Certification of Cambridge
                       TOIEC 925
                       
                   **Espagnol B1**
                   
                   **Japonais Notions**
                   
                   **Néerlandais Notions**
                   
                   """)
    
    def etre():
        st.subheader("Savoir-être")
        st.markdown("""
                    - confiant 
                    - organisé  
                    - esprit d'équipe 
                    - sens de la communication 
                    - consciencieux
                    """)
    
    def faire():
        st.subheader("Savoir-faire")
        selector2 = {
            "Programmation, Data": prog,
            "Intelligence Artificielle": main_page,
            }
        
        selected_page2 = st.selectbox("Selectionnez un savoir-faire", selector2.keys())
        selector2[selected_page2]()
        
    def savoirs():
        st.subheader("Savoirs")
        selector3 = {
            "Sciences": pagescience,
            "Langues et Certificaitons": langue,
            "Droit": droit,
            }
        
        selected_page3 = st.selectbox("Selectionnez un savoir-faire", selector3.keys())
        selector3[selected_page3]()
    
    def droit():
        st.subheader("Droit")
        
        st.markdown("""
                    
                    - Introduction à l'histoire du droit français 
                    
                    - Les acteurs du droit 
                    
                    - Les différentes manières de déposer un projet de loi
                    
                    - Droit des contrats
                    
                    - Droit informatique
                    
                    """)
        
        
    def prog():
        st.subheader("Langages de programmation")
        
        st.markdown("""
                    
                    **Python :** 
                        
                        - Pandas
                        - Matplotlib
                        - Pyscript
                        - Seanborn
                        
                    Expériences / Projets : 
                        
                        - Machine Learning "Predict total calories for a ride 
                                            beatween Utrecht and Brussels"
                                            
                        - Machine Learning : Hidden Morkov Model "Predict the 
                                             state of a molecul at a moment t"
                                             
                        - Visualization / Scrapping / Cleaning : 
                            "Find the best Ligue 1 season of the XX's century"
                    
                    """)
                    
        st.markdown("""
                    
                    **HTML / CSS :** 
                    
                    Expériences / Projets : 
                        
                        - Design 4 Grean 2022
                        - Stage à Welko 2020
                    
                    
                    """)
                    
        st.markdown("""
                    
                    **JAVA :** 
                    
                    Projets : 
                        
                        - Conception d'un jeu de plateau : Citadelle 
                    
                    """)
    
    selector1 = {
        "Savoir-être": etre,
        "Savoir-faire": faire,
        "Savoirs": savoirs,
        }

    selected_page = st.selectbox("Selectionnez un domaine de compétence", selector1.keys())
    selector1[selected_page]()
    
    
    
    
    
    

def portfolio(pic1, bpmwatch, bins, crypto, streamlit):
    
    
    pic1 = Image.open(pic1)
    bpmwatch = Image.open(bpmwatch)
    bins = Image.open(bins)
    crypto = Image.open(crypto)
    streamlit = Image.open(streamlit)
            
    st.title("Mes projets")
    
    st.markdown("Vous trouverez sur cette page des projets réalisés seule ou en équipe")
    
    st.caption("key word : hackathon ; big data ; machine learning")
    
    st.subheader("Machine Learning Apple Watch ⌚")
    
    with st.expander("Voir le projet"):
        st.caption("key word : cleaning data ; machine learning ; visualization")
        st.write("""
                 
                 J’ai utilisé 
les données de ma montre connectée pour créer un modèle prédictif. J'ai décidé assez rapidement de 
récupérer les données de ma montre. L’occasion de se questionner sur ce qu’on peut faire avec 1 an 
de données. Avec les données nettoyées, j’ai décidé de faire une régression linéaire pour prédire la 
durée de mon trajet Utrecht-Bruxelles, puis de créer une régression linéaire multiple pour prédire les 
calories brûlées. J’ai ensuite nettoyé ces fichiers. Pour ainsi mettre en place un modèle d’apprentissage 
avec comme donnée dépendante les calories dépensées. Les valeurs indépendantes étaient par 
exemple le dénivelé, l’altitude, le type de vélo, la météo... Ce notebook me permet de prédire les 
calories que je vais dépenser avant une sortie vélo et ainsi organiser mon alimentation.

 """)
        st.image(bpmwatch)
        
        mention(
           label="Machine Learning Apple Watch ⌚",
           icon="github",  # GitHub is also featured!
           url=" https://github.com/tienou29/vivepakitest/blob/master/FinalAssignmentEtienneRALEC.ipynb",
            )        
      
        
         
    
    st.subheader("Design of a data driven app 📱")
    
    with st.expander("Voir le projet"):
        st.caption("key word : figma ux/ui ; algorithme ; data visualization ; cluster ")
    
        st.write("""
                 Aux Pays-Bas j’ai été initié à la pratique de la méthode de gestion de projet Agile : scrum. Nous 
avons fait 3 sprints. Le but était de créer une application axée sur les données pour optimiser la gestion
des déchets. Les clients étaient la municipalité d’Utrecht, donc après chaque sprint les retours étaient 
riches. Le travail en équipe et les recherches dont nous avons fait preuve nous ont permis d'optimiser 
nos résultats, nous rapprochant ainsi de nos objectifs sprints après sprints. Ce projet sera utile dans le 
monde professionnel, car il permet de mieux comprendre cette méthode de travail
            
         """)
         
        st.image(bins)
        
        mention(
           label="IPYNB to find the nearest bin, visualization, print out meta data of a picture...",
           icon="github",  # GitHub is also featured!
           url="https://github.com/tienou29/bijplaatsingen/blob/main/CarteRESULT.ipynb",
            ) 
        mention(
           label="Deisgned App on Figma",
           icon="🪢",  # GitHub is also featured!
           url="https://www.figma.com/file/DHgWfQ5Kh0JaYKkejFeHsV/trashtruck?node-id=0%3A1",
            )  
         
    st.subheader("Hackathon pour visualiser les enjeux du vote législatif 📊")
    
    with st.expander("Voir le projet"):
        st.image(pic1)
        st.write("""
                 
       
        
         """)
         
    st.subheader("Design 4 Green 🌱 2021")
    
    with st.expander("Voir le projet"):
        
        st.markdown("<h4 style='color: green;'>Préparation avant le hackathon du 16/11/2022</h4>", unsafe_allow_html=True)
        st.caption("dashboard interractif; data visualization ; travail d'équipe")
        mention(
            label = "Esquisse rapide du projet",
            icon="👨‍🎨",
            url="https://d4gmadeleine-azea.onrender.com/",
            )
        mention(
            label = "Rendu final",
            icon="github",
            url="https://github.com/tienou29/gitprojectD4G",
            )
        st.write("""
                 
                 Préparation à l'hackathon Design 4 Green 2022
                 
                 Mon rôle : 
                     
                     - Création du prototype 
                     
                     - HTML / CSS
                     
                     - Management de l'équipe
        
         """)
         
    st.subheader("Hackathon Design 4 Green 🌱 2022")
         
    with st.expander("Voir le projet"):
             
             st.markdown("<h4 style='color: green;'>Hackathon du 16/11/2022</h4>", unsafe_allow_html=True)
             st.markdown("""
                         **Créer une page web accessible (RGAA) permettant
                         de visualiser les formations sur le numérique responsable
                         proposées sur le territoire et permettant de les visualiser
                         sous deux formats : une cartographie et une liste.**
                         """)
             st.caption("hackathon ; écoconception ; HTML ; CSS ; data visualization ; travail d'équipe")
            
             mention(
                 label = "Rendu final",
                 icon="github",
                 url="https://github.com/Joglodo/D4G_Group7",
                 )
             st.write("""
                      
                      Mon rôle : 
                          
                          - Definition de l'experience de l'utilisateur dans le projet UX design
                          
                          - Accessibilité du site (RGAA)
                          
                          - HTML / CSS
                          
                          - Management de l'équipe
             
              """)
    
    
    st.subheader("DashBoards")
    
    with st.expander("Voir le projet"):
        
        st.markdown("<h4 style='color: blue;'>Dashboards avec Tableau et Streamlit</h4>", unsafe_allow_html=True)
        st.caption("dashboard ; data visualization ; streamlit; Tableau")
        st.write("""
                 
       
        
         """)
         
        st.image(crypto)
        
        mention(
             label = "Who influences crypto ? (Tableau)",
             icon="🗺️",
             url="https://public.tableau.com/app/profile/etienne6558/viz/cryptotweetperday/Dashboard?publish=yes"
             )
        
        st.markdown ("""___""")
        
        st.image(streamlit)
        
        mention(
             label = "Find the most intresting ligue 1 season (Streamlit)",
             icon="	⚽",
             url=""
             )
        
    
       
         
def experience(colo_pic):
    
    # --- LOAD CSS, PDF & PROFIL PIC ---
    with open(rapportdestage1, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            colo_pic = Image.open(colo_pic)
          
    
    with open(rapportdestage2, "rb") as pdf_file:
            PDFbyte2 = pdf_file.read()
            
    
            
            
    st.title("Mes expériences")
    
    st.subheader("Mc Donald's 🍔")
    
    with st.expander("Voir l'expérience"):
        
        st.write("""
                     Mon stage au sein de la franchise Mc Donald's de Huis Ter Heide a été, à ma grande surprise, une
bonne expérience.

Dans ce restaurant, j'ai découvert l'impressionnante logistique de la restauration rapide. J'ai pu
observer différentes techniques de gestion. J'ai pu voir comment les technologies de l'information
étaient utilisées. J'ai pu découvrir le travail d'un "ouvrier" dans un pays étranger, dans un pays
d'accueil. J'ai découvert le marché du travail aux Pays-Bas ; le pays du plein emploi. Je n'ai pas
développé beaucoup de compétences utiles mais mon état d'esprit a changé.

Enfin, cette expérience me motive dans mon ambition de continuer à travailler à l'étranger à l'avenir.
       
        
         """)
         
        st.download_button(
              label=" 📄 Rapport de Stage",
              data=PDFbyte2,
              file_name=resume_file.name,
              mime="application/octet-stream",
              )
    
    st.subheader("Intégration Web à Welko 🖥️")
    
    with st.expander("Voir l'expérience"):
      
        st.write("""
                 
                 Pendant le mois de juillet j'ai réalisé un stage dans une agence de communication nommé
Welko®. C'est une entreprise où on trouve des graphistes et des développeurs. J'ai observé
chaque métier et j'ai eu plusieurs missions d'intégration web. J'ai notamment donné une
nouvelle vie au site d'Angers SCO en modifiant la structure avec l'HTML et en modifiant le
style avec le CSS. J'ai appris avec Agrauxine à utiliser WordPress pour rajouter des anciens
articles. J'ai aussi appris à utiliser Adobe illustrator pour maitriser la taille, la couleur et le
format de l'image. J'ai appris avec Yakavan à intégrer une signature d'adresse mail. Je me
suis initié à la réalité augmentée avec SnapPress. Ensuite je me suis intéressé à la manière
de travailler des graphistes et j'ai découvert comment ils collaboraient avec les chargés
clientèles. Enfin j'ai observé attentivement la création du site de Yakavan. Grâce à ces
missions j'ai découvert la manière de travailler des différents acteurs qui façonnent les sites
webs sur lesquels nous naviguons.
       
        
         """)
         
        st.download_button(
             label=" 📄 Rapport de Stage",
             data=PDFbyte,
             file_name=resume_file.name,
             mime="application/octet-stream",
             )
    
    st.subheader("Animation populaire 🕺")
    
    with st.expander("Voir l'expérience"):
        
        st.write("""
        
                 Etre animateur c'est assurer la sécurité et l'épanouissement des enfants. 
                 
                 Comme vous pouvez le voir sur la photo c'est beaucoup de travail. 
                 
                 Assurer la vie quotidienne, éviter les catastrophes... Un enfant qui s'ennuie est un 
                 enfant dangereux pour lui et son entourage. Il faut constament les occuper. 
                 
                 Pour cela il faut faire preuve de travail d'équipe et de créativité.
                 
                 
        
    """)
        st.image(colo_pic)
    
 
def hobbies(bdgpic, ridein_pic, buddypic, vtt, cap):
    

    bdgpic = Image.open(bdgpic)
    ridein_pic = Image.open(ridein_pic)
    buddypic = Image.open(buddypic)
    vtt = Image.open(vtt)
    cap = Image.open(cap)
                
    st.title("Mes engagements")
    
    selected = mainENG(example=EXAMPLE_NO)
    
    if selected == "Animation":
        st.header("L'animation populaire")
        st.subheader("Les PEP") #write a title
        with st.expander("Voir l'engagement"):
             
            st.write("""
            PEP signifie "Pupille de l'Enseignement Public". 
            
            Pour ma dernière colonie de vacance en tant qu'animateur j'ai décidé de rejoindre les PEP. C'était en aout 2022.
            
            Faire l'effort d'aider les enfants qui sont nées sous une mauvaise étoile est toujours très gratifiant. 
                   
            
             """)
        
        st.subheader("AVEA")
        with st.expander("Voir l'engagement"):
             
            st.write("""
            
                     Avec l'AVEA j'ai réalisé de nombreuses colonies de vacance en tant qu'animateur. 
                     
                     Etre animateur c'est assurer la sécurité et l'épanouissement des enfants. Avec l'AVEA
                     je me suis moi même épanoui en devenant à chaque aventure un meilleur animateur. 
           
            
             """)
        
    if selected == "Associatif":
        st.subheader("Bureau Des Gourmets") 
        with st.expander("Voir l'engagement"):
            
            col1, col2 = st.columns(2)
            with col1:
                    st.image(bdgpic, width=275)

            with col2:
                  st.write("""
                           
                          J'ai rejoint cette associations étudiante en 2021. Je suis secrétaire et membre actif.
                          
                          Mon rôle est de prendre en note l'essentiel de ce qui est dit durant les réunion. Afin
                          d'aider le président à mettre en place les projets. 
                          
                          Nous avons organisé plusieurs événements. Comme des repas à thème. La tenu de la cafeteria de l'ecole. 
                          Ou encore l'animation d'un stand au marché de noël.
                  
                   """)
                
           
            
           
        st.subheader("RideIN") 
        with st.expander("Voir l'engagement"):
             col1, col2 = st.columns(2)
             with col1:
                     st.image(ridein_pic, width=250)

             with col2:
                   st.write("""
                            
                            RideIN, c’est le club de vélo que j’ai crée en 2020. L’objectif de ce club est
de promouvoir la pratique du vélo au quotidien. C’est à dire promouvoir le vélotaf, 
le cyclotourisme ou encore la pratique plus sportive. 


Pour cela j'organise les sorties hebdomadaires/ mensuel nous avons pu mettre en place une vingtaine de sorties.
                   
                    """)
                    
             st.write("""
                             
  Ainsi que deux 
sorties longue distance Angers-Nantes et Angers-Saumur. Le plus technique c’est de créer à la main  un 
itinéraire grâce à l'application Komoot. Les itinéraires doivent répondre aux 
compétences de chacun et aux envies. Une sortie qui doit être riche en paysage et 
en patrimoine mais qui ne soit pas trop dur physiquement. Une bonne manière 
d’apprendre à écouter les attentes des membres du club.


Un autre challenge rencontré est de travailler avec l'equipe
de communication pour promouvoir la sortie avec des itinéraires attractifs ! Je suis toujours émerveillé de faire découvrir les alentours 
d’Angers aux autres. Je pourrai rouler tout seul, plus vite et plus loin et découvrir plus mais il faut aussi 
savoir partager. Voir des Marocains, des sudistes, des réunionnais, des Bretons et même des Angevins sortir 
de la ville et prendre des photos pour leur famille c’est vraiment très beau à voir.
                             
                             """)
            
            
            
        st.subheader("Buddy Go Dutch") 
        with st.expander("Voir l'engagement"):
            col1, col2 = st.columns(2)
            with col1:
                    st.image(buddypic, width=300)

            with col2:
                  st.write("""
                           
                           Buddy Go Dutch est une association de l’Université d’Utrecht. Elle a 
pour but de mettre en contact les élèves étrangers avec les élèves 
néerlandais. Pour cela ils ont créé un système de parrainage et ils 
organisent des événements comme du patin sur glace, du bowling, 
découverte de lieux touristiques comme la Dom Tower ou 
Kinderdijk etc.

                  
                   """)
                 
            st.write("""
                     
                     Cette association a trois objectifs. Ils 
veulent perfectionneur leur site web. Créer une application. Ainsi 
que rendre l’algorithme de parrainage lisible pour le pour le prochain bureau


Je me suis porté volontaire pour rafraîchir le site web. C’était un moyen pour moi de perfectionner mes 
compétences d’intégration web. Mais aussi de découvrir d’autre techniques.


Je devais faire face à un autre défi. Faire comprendre mon travail aux membres du bureau d’organisation. 
Ma première action a été de mettre à jour le PHP du site web en une version plus récente. C’était assez 
dure car cela devait correspondre à notre version de WordPress. Ensuite j’ai redimensionné le logo du 
menu pour qu’il est une meilleure résolution. De plus j’ai rajouté des lieux sur la carte d’activité.


J’ai développé des compétences techniques. J’ai vu de nouvelle manière de planifier des réunions avec 
loulouapp. J’ai perfectionné mon anglais dans un langage informatique et professionnel. Beaucoup 
d’apprentissage en autodidacte, j’ai perfectionné mon autonomie. Je suis content de cette expérience.
                     """)
        
    if selected == "Centres d'intérêt":
        st.subheader("VTT, montagne, forêt") #write a title
        with st.expander("Voir le centre d'intérêt"):
            
            col1, col2 = st.columns(2)
            with col1:
                    st.image(vtt, width=275)

            with col2:
                  st.write("""
                           
                          Je porte beaucoup d'importance à la découverte des paysages qui nous entourent.
                          
                          Je suis licencié au Relecq VTT depuis mes 14 ans. Je participe aux compétitions, 
                          aux randonnées et à la vie du club. 
                          
                          Grâce à ce club je respecte énormément la vie associative. 
                          
                          Par exemple nous avons partciper à une course de 24h en relais. C'était 
                          beaucoup d'organisation !
                  
                   """)
    
        st.subheader("Course à pied et le dépassement de soi") 
        with st.expander("Voir le centre d'intérêt"):
            col1, col2 = st.columns(2)
            with col1:
                    st.image(cap, width=275)

            with col2:
                  st.write("""
                           
                           Se dépasser, progresser, partager. Le sport a toujours été present dans ma vie.
                           
                           J'ai pour ambition de faire des ultras trails dans le futur, comme l'UTMB Mont Blanc
                           ou la diagonal des fous à la Réunion. 
                           
                           
                  
                   """)
                   
                   
def contact():
    st.title("Me contacter")
    
    st.header("Temps de réponse : ~ 1 heure ⚡️")
    
    
    contact_form = """
    <form action="https://formsubmit.co/etienneralec@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
     </form>
     """

    st.markdown(contact_form, unsafe_allow_html=True)
    
    
    # Use Local CSS File
    with open(css_file2) as f:
                st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

 
    
main()
