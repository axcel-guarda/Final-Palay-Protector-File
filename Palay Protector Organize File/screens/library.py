# screens/library.py
import streamlit as st
from components.navigation import show_bottom_nav

def show_library():
    # Initialize translation state if not exists
    if 'translations' not in st.session_state:
        st.session_state.translations = {}
    
    st.markdown("""
    <style>
    /* ===== FORCE WHITE BACKGROUND ===== */
    body, .main, .stApp {
        background-color: #ffffff !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
    }

    .block-container {
        background-color: #ffffff !important;
        padding-top: 2rem;
    }

    /* HEADER */
    .library-header {
        text-align: center;
        color: #2e7d32;
        margin-bottom: 20px;
    }

    .search-container {
        margin: 20px 0;
    }

    /* CARD STYLE */
    .disease-card {
        background: #ffffff;
        border-left: 5px solid #4CAF50;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }

    .disease-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    .disease-title {
        font-size: 20px;
        font-weight: bold;
        color: #1b5e20;
        margin-bottom: 5px;
        text-align: left;
    }

    .disease-scientific {
        font-style: italic;
        color: #6c757d;
        font-size: 14px;
        margin-bottom: 10px;
        text-align: left;
    }

    .severity-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 12px;
        font-weight: bold;
        margin-bottom: 15px;
    }

    .severity-high {
        background-color: #ffebee;
        color: #c62828;
    }

    .severity-medium {
        background-color: #fff3e0;
        color: #ef6c00;
    }

    .severity-low {
        background-color: #e8f5e9;
        color: #2e7d32;
    }

    .info-section {
        margin: 15px 0;
        text-align: left;
    }

    .info-title {
        font-weight: bold;
        color: #2e7d32;
        font-size: 15px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        text-align: left;
    }

    .info-content {
        color: #424242;
        line-height: 1.6;
        font-size: 14px;
        padding-left: 10px;
        text-align: left;
    }

    .tip-box {
        background: #f5f5f5;
        border-left: 4px solid #4CAF50;
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0;
        text-align: left;
    }
    
    /* BUTTON STYLING */
    div.stButton > button {
        width: 100% !important;
        background: linear-gradient(135deg, #2e7d32 0%, #1b5e20 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 0 !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        text-align: center !important;
        box-shadow: 0 4px 12px rgba(46, 125, 50, 0.3) !important;
        margin: 5px 0 !important;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(46, 125, 50, 0.4) !important;
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%) !important;
    }

    /* SEARCH BOX STYLING */
    .stTextInput > div > div > input {
        border: 2px solid #4CAF50 !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 16px !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #2e7d32 !important;
        box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1) !important;
    }

    p {
        text-align: left !important;
    }

    ul, li {
        text-align: left !important;
    }

    /* EXPANDER STYLING */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f1f8e9 0%, #e8f5e8 100%) !important;
        border-radius: 10px !important;
        border: 1px solid #c8e6c9 !important;
        font-weight: 600 !important;
    }

    .streamlit-expanderContent {
        background: #ffffff !important;
        border-radius: 0 0 10px 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="library-header">
        <h2 style='font-size: 32px; font-weight: 800; margin-bottom: 8px;'>Rice Disease Library</h2>
        <p style="color: #6c757d; font-size: 16px;">Complete guide to rice plant diseases</p>
    </div>
    """, unsafe_allow_html=True)

    # Search functionality
    search = st.text_input("🔍 Search diseases...", key="disease_search", placeholder="Type disease name...")
    
    # Enhanced disease database with detailed information - ALL 12 DISEASES WITH TAGALOG
    diseases = [
        {
            "name": "Brown Spot",
            "scientific": "Bipolaris oryzae",
            "severity": "Medium",
            "description": "A fungal disease common in nutrient-deficient fields, particularly those lacking potassium.",
            "symptoms": [
                "Small circular brown spots on leaves",
                "Spots have yellow halos",
                "Affects both leaves and grains",
                "Reduces grain quality and weight"
            ],
            "treatment": [
                "Apply mancozeb or copper fungicides",
                "Improve soil nutrition (especially potassium)",
                "Remove infected plant parts",
                "Ensure proper drainage"
            ],
            "prevention": [
                "Maintain balanced soil nutrition",
                "Use healthy certified seeds",
                "Practice proper water management",
                "Avoid stress conditions"
            ],
            "image": "https://apps.lucidcentral.org/ppp_v9/images/entities/rice_brown_leaf_spot_427/5390490lgpt.jpg",
            "tagalog": {
                "description": "Isang sakit na dulot ng fungus na karaniwan sa mga bukid na kulang sa sustansya, lalo na ang potassium.",
                "symptoms": [
                    "Maliliit na bilog na kayumangging batik sa mga dahon",
                    "May dilaw na bilog sa paligid ng batik",
                    "Nakakaapekto sa dahon at butil",
                    "Bumababa ang kalidad at timbang ng butil"
                ],
                "treatment": [
                    "Maglagay ng mancozeb o copper fungicide",
                    "Pagbutihin ang nutrisyon ng lupa (lalo na potassium)",
                    "Alisin ang mga nahawaang bahagi ng halaman",
                    "Siguraduhing maayos ang drainage"
                ],
                "prevention": [
                    "Panatilihing balanse ang nutrisyon ng lupa",
                    "Gumamit ng malusog at sertipikadong binhi",
                    "Magsagawa ng tamang pamamahala ng tubig",
                    "Iwasan ang mga kondisyon na nakaka-stress"
                ]
            }
        },
        {
            "name": "Sheath Blight",
            "scientific": "Rhizoctonia solani",
            "severity": "High",
            "description": "A major fungal disease that thrives in warm, humid conditions with dense plant populations.",
            "symptoms": [
                "Oval or irregular lesions on leaf sheaths",
                "Greenish-gray lesions with brown borders",
                "Lesions merge and spread upward",
                "Plant lodging in severe cases"
            ],
            "treatment": [
                "Apply validamycin or hexaconazole fungicides",
                "Remove infected plant debris after harvest",
                "Improve air circulation in the field",
                "Reduce plant density"
            ],
            "prevention": [
                "Use proper plant spacing",
                "Avoid excessive nitrogen fertilization",
                "Drain fields periodically",
                "Practice crop rotation with non-host crops"
            ],
            "image": "https://th.bing.com/th/id/R.74ee4c2cbd251001c04c8b984b754cf0?rik=x%2bM1DIRpKy7dQw&riu=http%3a%2f%2f2.bp.blogspot.com%2f_-rGxVjqS77w%2fSsQ7mTG2bnI%2fAAAAAAAAAaY%2fGEv3UJtn7eE%2fw1200-h630-p-k-no-nu%2fSHEATH%2bBLIGHT.jpg&ehk=syWAczjiAoUbiwqvNeQOi48XNm3JzXEqpGJ4wCIym8U%3d&risl=&pid=ImgRaw&r=0",
            "tagalog": {
                "description": "Isang malaking sakit na dulot ng fungus na lumalaki sa mainit at mahalumigmig na kondisyon na may siksik na tanim.",
                "symptoms": [
                    "Oval o hindi regular na sugat sa balat ng dahon",
                    "Berde-abong sugat na may kayumangging gilid",
                    "Nagsasama ang mga sugat at kumakalat pataas",
                    "Pagbagsak ng halaman sa malubhang kaso"
                ],
                "treatment": [
                    "Maglagay ng validamycin o hexaconazole fungicide",
                    "Alisin ang nahawaang mga basura ng halaman pagkatapos ng ani",
                    "Pagbutihin ang sirkulasyon ng hangin sa bukid",
                    "Bawasan ang density ng halaman"
                ],
                "prevention": [
                    "Gumamit ng tamang pagitan ng halaman",
                    "Iwasan ang labis na nitrogen fertilization",
                    "Pana-panahong patuyuin ang bukid",
                    "Magsagawa ng crop rotation na hindi host"
                ]
            }
        },
        {
            "name": "Bacterial Leaf Blight",
            "scientific": "Xanthomonas oryzae pv. oryzae",
            "severity": "High",
            "description": "A serious bacterial disease that affects rice plants at all growth stages, especially during rainy seasons.",
            "symptoms": [
                "Water-soaked lesions on leaf tips and edges",
                "Yellowing of infected leaves",
                "Wilting of seedlings (kresek symptom)",
                "White bacterial ooze on leaves"
            ],
            "treatment": [
                "Apply copper-based bactericides",
                "Remove and destroy infected plants",
                "Improve field drainage",
                "Use certified disease-free seeds"
            ],
            "prevention": [
                "Plant resistant varieties",
                "Avoid injury to plants",
                "Balance nitrogen fertilization",
                "Maintain proper spacing for air circulation"
            ],
            "image": "https://toagriculture.com/wp-content/uploads/2022/12/Bacterial-blight-disease-of-rice-Soci.jpg",
            "tagalog": {
                "description": "Isang seryosong bakteryal na sakit na nakakaapekto sa palay sa lahat ng yugto ng paglaki, lalo na sa tag-ulan.",
                "symptoms": [
                    "Basang-basa na sugat sa dulo at gilid ng dahon",
                    "Paninilaw ng nahawaang dahon",
                    "Paglanta ng punla (kresek symptom)",
                    "Puting bakteryal na dumadaloy sa dahon"
                ],
                "treatment": [
                    "Maglagay ng copper-based bactericide",
                    "Alisin at sirain ang nahawaang halaman",
                    "Pagbutihin ang drainage ng bukid",
                    "Gumamit ng sertipikadong binhing walang sakit"
                ],
                "prevention": [
                    "Magtanim ng resistant na uri",
                    "Iwasan ang pagkapinsala ng halaman",
                    "Balansehin ang nitrogen fertilization",
                    "Panatilihing tamang pagitan para sa daloy ng hangin"
                ]
            }
        },
        {
            "name": "Healthy Rice",
            "scientific": "Oryza sativa (Healthy)",
            "severity": "Low",
            "description": "Healthy rice plants showing normal growth and development without any disease symptoms.",
            "symptoms": [
                "Vibrant green leaves",
                "Uniform growth pattern",
                "No lesions or discoloration",
                "Strong and upright stems"
            ],
            "treatment": [
                "No treatment needed",
                "Continue good agricultural practices",
                "Monitor regularly for early disease detection",
                "Maintain preventive measures"
            ],
            "prevention": [
                "Use certified quality seeds",
                "Practice integrated pest management",
                "Maintain balanced nutrition",
                "Ensure proper water management"
            ],
            "image": "https://thumbs.dreamstime.com/b/close-up-rice-plant-leaves-dew-drops-190913252.jpg",
            "tagalog": {
                "description": "Malusog na palay na nagpapakita ng normal na paglaki at pag-unlad na walang anumang sintomas ng sakit.",
                "symptoms": [
                    "Maliwanag na berdeng dahon",
                    "Pantay na pattern ng paglaki",
                    "Walang sugat o pagbabago ng kulay",
                    "Malakas at tuwid na tangkay"
                ],
                "treatment": [
                    "Walang kinakailangang gamot",
                    "Ipagpatuloy ang mabuting kagawian sa pagsasaka",
                    "Regular na suriin para sa maagang pagtuklas ng sakit",
                    "Panatilihin ang mga pag-iingat"
                ],
                "prevention": [
                    "Gumamit ng sertipikadong de-kalidad na binhi",
                    "Magsagawa ng integrated pest management",
                    "Panatilihing balanse ang nutrisyon",
                    "Siguraduhing maayos ang pamamahala ng tubig"
                ]
            }
        },
        {
            "name": "Rice Hispa",
            "scientific": "Dicladispa armigera",
            "severity": "Medium",
            "description": "A pest infestation causing white streaks on leaves due to larvae feeding between leaf surfaces.",
            "symptoms": [
                "White longitudinal streaks on leaves",
                "Parallel feeding marks",
                "Dried and papery leaf appearance",
                "Reduced photosynthesis"
            ],
            "treatment": [
                "Apply appropriate insecticides",
                "Remove heavily infested leaves",
                "Flood the field to kill pupae",
                "Use light traps for adults"
            ],
            "prevention": [
                "Avoid close plant spacing",
                "Remove weeds around fields",
                "Use hispa-resistant varieties",
                "Practice proper field sanitation"
            ],
            "image": "https://wordpress-cdn-echoupaladvisory.echoupal.co.in/wp-content/uploads/2022/03/ricehipsa2-1.jpg",
            "tagalog": {
                "description": "Isang peste na nagdudulot ng puting guhit sa dahon dahil sa uod na kumakain sa pagitan ng ibabaw ng dahon.",
                "symptoms": [
                    "Puting pahabang guhit sa dahon",
                    "Magkakaparalelong marka ng pagkain",
                    "Tuyong at papel na anyo ng dahon",
                    "Bumabang photosynthesis"
                ],
                "treatment": [
                    "Maglagay ng angkop na insecticide",
                    "Alisin ang labis na nahawaang dahon",
                    "Bahaiin ang bukid para patayin ang pupae",
                    "Gumamit ng light trap para sa adult"
                ],
                "prevention": [
                    "Iwasan ang masyadong malapit na pagitan ng tanim",
                    "Alisin ang mga damo sa paligid ng bukid",
                    "Gumamit ng hispa-resistant na uri",
                    "Magsagawa ng tamang kalinisan ng bukid"
                ]
            }
        },
        {
            "name": "False Smut",
            "scientific": "Ustilaginoidea virens",
            "severity": "Medium",
            "description": "A fungal disease affecting rice grains, forming large greenish-black spore balls on panicles.",
            "symptoms": [
                "Greenish-black velvety balls on grains",
                "Individual grains enlarged",
                "Powder-covered spore balls",
                "Reduced grain quality"
            ],
            "treatment": [
                "Apply fungicides during flowering",
                "Remove and burn infected panicles",
                "Improve field drainage",
                "Reduce humidity in field"
            ],
            "prevention": [
                "Use resistant varieties",
                "Avoid excessive nitrogen fertilization",
                "Maintain proper plant spacing",
                "Practice crop rotation"
            ],
            "image": "https://tse2.mm.bing.net/th/id/OIP.TZd75GWVA5aL_qxqLemfMAHaFj?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3",
            "tagalog": {
                "description": "Isang sakit na dulot ng fungus na nakakaapekto sa butil ng palay, bumubuo ng malalaking berde-itim na bola ng spore sa panicle.",
                "symptoms": [
                    "Berde-itim na mabalahibo ng bola sa butil",
                    "Lumalaki ang bawat butil",
                    "Bola ng spore na may pulbos",
                    "Bumabang kalidad ng butil"
                ],
                "treatment": [
                    "Maglagay ng fungicide sa panahon ng pamumulaklak",
                    "Alisin at sunugin ang nahawaang panicle",
                    "Pagbutihin ang drainage ng bukid",
                    "Bawasan ang kahalumigmigan sa bukid"
                ],
                "prevention": [
                    "Gumamit ng resistant na uri",
                    "Iwasan ang labis na nitrogen fertilization",
                    "Panatilihing tamang pagitan ng halaman",
                    "Magsagawa ng crop rotation"
                ]
            }
        },
        {
            "name": "Leaf Smut",
            "scientific": "Entyloma oryzae",
            "severity": "Low",
            "description": "A minor fungal disease causing small black angular spots on leaves.",
            "symptoms": [
                "Small angular black spots on leaves",
                "Spots scattered on leaf surface",
                "Minimal yield impact",
                "More common in wet conditions"
            ],
            "treatment": [
                "Usually no treatment needed",
                "Improve field drainage if severe",
                "Reduce leaf wetness duration",
                "Apply fungicides if widespread"
            ],
            "prevention": [
                "Use quality seeds",
                "Maintain proper field drainage",
                "Avoid overhead irrigation",
                "Practice balanced fertilization"
            ],
            "image": "https://bugwoodcloud.org/images/768x512/5390514.jpg",
            "tagalog": {
                "description": "Isang minor na sakit na dulot ng fungus na nagdudulot ng maliliit na itim na angular na batik sa dahon.",
                "symptoms": [
                    "Maliliit na angular na itim na batik sa dahon",
                    "Kalat ang batik sa ibabaw ng dahon",
                    "Maliit na epekto sa ani",
                    "Mas karaniwan sa basang kondisyon"
                ],
                "treatment": [
                    "Kadalasan ay walang kinakailangang gamot",
                    "Pagbutihin ang drainage ng bukid kung malubha",
                    "Bawasan ang tagal ng pagkabasa ng dahon",
                    "Maglagay ng fungicide kung laganap"
                ],
                "prevention": [
                    "Gumamit ng de-kalidad na binhi",
                    "Panatilihing maayos ang drainage ng bukid",
                    "Iwasan ang overhead irrigation",
                    "Magsagawa ng balanseng fertilization"
                ]
            }
        },
        {
            "name": "Leaf Scald",
            "scientific": "Monographella albescens",
            "severity": "Medium",
            "description": "A fungal disease causing distinctive banded lesions on rice leaves.",
            "symptoms": [
                "Alternating light and dark bands on leaves",
                "Lesions start from leaf tips",
                "Yellowing of affected areas",
                "Premature leaf drying"
            ],
            "treatment": [
                "Apply appropriate fungicides",
                "Remove infected plant debris",
                "Improve air circulation",
                "Ensure proper drainage"
            ],
            "prevention": [
                "Use resistant varieties",
                "Avoid excessive nitrogen",
                "Practice proper spacing",
                "Maintain field sanitation"
            ],
            "image": "https://bugwoodcloud.org/images/768x512/5390511.jpg",
            "tagalog": {
                "description": "Isang sakit na dulot ng fungus na nagdudulot ng natatanging banda na sugat sa dahon ng palay.",
                "symptoms": [
                    "Magpapalit-palit na liwanag at madilim na banda sa dahon",
                    "Nagsisimula ang sugat mula sa dulo ng dahon",
                    "Paninilaw ng naapektuhang lugar",
                    "Maagaang pagkatuyo ng dahon"
                ],
                "treatment": [
                    "Maglagay ng angkop na fungicide",
                    "Alisin ang nahawaang basura ng halaman",
                    "Pagbutihin ang sirkulasyon ng hangin",
                    "Siguraduhing maayos ang drainage"
                ],
                "prevention": [
                    "Gumamit ng resistant na uri",
                    "Iwasan ang labis na nitrogen",
                    "Magsagawa ng tamang pagitan",
                    "Panatilihin ang kalinisan ng bukid"
                ]
            }
        },
        {
            "name": "Narrow Brown Leaf Spot",
            "scientific": "Cercospora janseana",
            "severity": "Low",
            "description": "A minor leaf spot disease causing narrow brown lesions on rice leaves.",
            "symptoms": [
                "Narrow brown linear lesions",
                "Lesions parallel to leaf veins",
                "Yellow halos around spots",
                "Minimal impact on yield"
            ],
            "treatment": [
                "Usually no treatment required",
                "Apply fungicides if severe",
                "Remove heavily infected leaves",
                "Improve field conditions"
            ],
            "prevention": [
                "Use healthy seeds",
                "Maintain balanced nutrition",
                "Ensure proper drainage",
                "Practice crop rotation"
            ],
            "image": "https://tse1.mm.bing.net/th/id/OIP.YeSPfVgbqHLbF54KLRtl9gHaE9?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3",
            "tagalog": {
                "description": "Isang minor na sakit ng batik sa dahon na nagdudulot ng makitid na kayumangging sugat sa dahon ng palay.",
                "symptoms": [
                    "Makitid na kayumangging tuwid na sugat",
                    "Sugat na kahanay ng ugat ng dahon",
                    "Dilaw na bilog sa paligid ng batik",
                    "Maliit na epekto sa ani"
                ],
                "treatment": [
                    "Kadalasan ay walang kinakailangang gamot",
                    "Maglagay ng fungicide kung malubha",
                    "Alisin ang labis na nahawaang dahon",
                    "Pagbutihin ang kondisyon ng bukid"
                ],
                "prevention": [
                    "Gumamit ng malusog na binhi",
                    "Panatilihing balanse ang nutrisyon",
                    "Siguraduhing maayos ang drainage",
                    "Magsagawa ng crop rotation"
                ]
            }
        },
        {
            "name": "Rice Blast",
            "scientific": "Pyricularia oryzae",
            "severity": "High",
            "description": "Rice blast is one of the most destructive diseases of rice, causing significant yield losses worldwide.",
            "symptoms": [
                "Diamond-shaped lesions on leaves",
                "White to gray centers with brown margins",
                "Lesions on leaf nodes and panicles",
                "Neck rot in severe cases"
            ],
            "treatment": [
                "Apply fungicides containing tricyclazole or azoxystrobin",
                "Remove infected plant debris",
                "Maintain proper field drainage",
                "Use resistant varieties"
            ],
            "prevention": [
                "Use resistant varieties",
                "Avoid excessive nitrogen fertilization",
                "Maintain proper water management",
                "Practice crop rotation"
            ],
            "image": "https://tse2.mm.bing.net/th/id/OIP.N5zA4MwJYeI20Q2YGCme2wHaE9?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3",
            "tagalog": {
                "description": "Ang Rice Blast ay isa sa pinakamarahas na sakit ng palay, nagdudulot ng malaking pagkalugi sa ani sa buong mundo.",
                "symptoms": [
                    "Hugis-diyamante na sugat sa dahon",
                    "Puti hanggang abong gitna na may kayumangging gilid",
                    "Sugat sa node ng dahon at panicle",
                    "Pagkabulok ng leeg sa malubhang kaso"
                ],
                "treatment": [
                    "Maglagay ng fungicide na may tricyclazole o azoxystrobin",
                    "Alisin ang nahawaang basura ng halaman",
                    "Panatilihing maayos ang drainage ng bukid",
                    "Gumamit ng resistant na uri"
                ],
                "prevention": [
                    "Gumamit ng resistant na uri",
                    "Iwasan ang labis na nitrogen fertilization",
                    "Panatilihing maayos ang pamamahala ng tubig",
                    "Magsagawa ng crop rotation"
                ]
            }
        },
        {
            "name": "Rice Stripes",
            "scientific": "Rice stripe virus (RSV)",
            "severity": "High",
            "description": "A viral disease transmitted by small brown planthoppers causing chlorotic stripes on leaves.",
            "symptoms": [
                "Yellow or chlorotic stripes on leaves",
                "Stunted plant growth",
                "Reduced tillering",
                "Incomplete panicle exertion"
            ],
            "treatment": [
                "Remove infected plants immediately",
                "Control planthopper vectors",
                "No direct cure for viral infection",
                "Use resistant varieties"
            ],
            "prevention": [
                "Plant virus-resistant varieties",
                "Control planthopper populations",
                "Adjust planting dates",
                "Remove volunteer rice plants"
            ],
            "image": "https://tse2.mm.bing.net/th/id/OIP.hPJMjM6glnzy2itgSj9H6QHaE8?cb=12&w=1500&h=1000&rs=1&pid=ImgDetMain&o=7&rm=3",
            "tagalog": {
                "description": "Isang viral na sakit na dinadala ng maliit na kayumangging planthopper na nagdudulot ng chlorotic na guhit sa dahon.",
                "symptoms": [
                    "Dilaw o chlorotic na guhit sa dahon",
                    "Sunog ang paglaki ng halaman",
                    "Bumabang tillering",
                    "Hindi kumpleto ang paglabas ng panicle"
                ],
                "treatment": [
                    "Alisin kaagad ang nahawaang halaman",
                    "Kontrolin ang planthopper vector",
                    "Walang direktang gamot sa viral infection",
                    "Gumamit ng resistant na uri"
                ],
                "prevention": [
                    "Magtanim ng virus-resistant na uri",
                    "Kontrolin ang populasyon ng planthopper",
                    "Ayusin ang petsa ng pagtatanim",
                    "Alisin ang kusang tumutubo na palay"
                ]
            }
        },
        {
            "name": "Rice Tungro",
            "scientific": "Rice tungro bacilliform virus (RTBV) & Rice tungro spherical virus (RTSV)",
            "severity": "High",
            "description": "A viral disease transmitted by green leafhopper, causing severe stunting and yield loss.",
            "symptoms": [
                "Yellow or orange-yellow leaf discoloration",
                "Stunted plant growth",
                "Reduced number of tillers",
                "Incomplete panicle formation"
            ],
            "treatment": [
                "Remove and destroy infected plants immediately",
                "Control leafhopper vectors with insecticides",
                "No direct cure available for viral infection",
                "Replant with resistant varieties if severe"
            ],
            "prevention": [
                "Plant tungro-resistant varieties",
                "Control green leafhopper populations",
                "Adjust planting dates to avoid peak vector activity",
                "Remove weeds that host leafhoppers"
            ],
            "image": "https://tse1.mm.bing.net/th/id/OIP.rtDAwQ8P15ghoq0nTNZu3gHaFj?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3",
            "tagalog": {
                "description": "Isang viral na sakit na dinadala ng berdeng leafhopper, nagdudulot ng malubhang pagkasunog at pagkawala ng ani.",
                "symptoms": [
                    "Dilaw o orange-dilaw na pagbabago ng kulay ng dahon",
                    "Sunog ang paglaki ng halaman",
                    "Bumabang bilang ng tillers",
                    "Hindi kumpleto ang pagbuo ng panicle"
                ],
                "treatment": [
                    "Alisin at sirain kaagad ang nahawaang halaman",
                    "Kontrolin ang leafhopper vector gamit ang insecticide",
                    "Walang direktang gamot para sa viral infection",
                    "Magtanim muli ng resistant na uri kung malubha"
                ],
                "prevention": [
                    "Magtanim ng tungro-resistant na uri",
                    "Kontrolin ang populasyon ng berdeng leafhopper",
                    "Ayusin ang petsa ng pagtatanim para maiwasan ang peak vector activity",
                    "Alisin ang damo na host ng leafhopper"
                ]
            }
        }
    ]
    
    # Filter diseases based on search
    filtered_diseases = diseases
    if search and search.strip():
        search_lower = search.lower().strip()
        filtered_diseases = [
            d for d in diseases 
            if search_lower in d['name'].lower() or search_lower in d['scientific'].lower()
        ]

    # Display filtered diseases
    if filtered_diseases:
        for disease in filtered_diseases:
            # Create unique key for this disease's translation state
            disease_key = disease['name'].replace(" ", "_").lower()
            
            with st.expander(f"**{disease['name']}** - *{disease['scientific']}*", expanded=False):
                # Translation buttons in columns
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if st.button("🇵🇭 Tagalog", key=f"tagalog_{disease_key}", use_container_width=True):
                        st.session_state.translations[disease_key] = "tagalog"
                        st.rerun()
                with col_btn2:
                    if st.button("🇺🇸 English", key=f"english_{disease_key}", use_container_width=True):
                        st.session_state.translations[disease_key] = "english"
                        st.rerun()
                
                # Check current language
                current_lang = st.session_state.translations.get(disease_key, "english")
                
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.image(disease['image'], width=150)
                
                with col2:
                    # Severity badge
                    severity_class = f"severity-{disease['severity'].lower()}"
                    severity_label = "Severity" if current_lang == "english" else "Kalubhaan"
                    st.markdown(f"""
                    <div class="{severity_class}" style="display: inline-block; padding: 6px 14px; border-radius: 15px; font-size: 12px; font-weight: bold; margin-bottom: 10px;">
                        {severity_label}: {disease['severity']}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Description - Display based on language
                if current_lang == "tagalog":
                    description = disease['tagalog']['description']
                else:
                    description = disease['description']
                
                st.markdown(f"<p style='margin: 15px 0; color: #424242; text-align: left; line-height: 1.6;'>{description}</p>", unsafe_allow_html=True)
                
                # Symptoms
                symptoms_title = "Symptoms" if current_lang == "english" else "Mga Sintomas"
                st.markdown(f"<div style='font-weight: bold; color: #2e7d32; margin: 20px 0 10px 0; font-size: 16px;'>{symptoms_title}</div>", unsafe_allow_html=True)
                
                symptoms_list = disease['symptoms'] if current_lang == "english" else disease['tagalog']['symptoms']
                for symptom in symptoms_list:
                    st.markdown(f"<div style='text-align: left; margin: 5px 0; padding-left: 10px;'>• {symptom}</div>", unsafe_allow_html=True)
                
                # Treatment
                treatment_title = "Treatment" if current_lang == "english" else "Gamot"
                st.markdown(f"<div style='font-weight: bold; color: #2e7d32; margin: 20px 0 10px 0; font-size: 16px;'>{treatment_title}</div>", unsafe_allow_html=True)
                
                treatment_list = disease['treatment'] if current_lang == "english" else disease['tagalog']['treatment']
                for treatment in treatment_list:
                    st.markdown(f"<div style='text-align: left; margin: 5px 0; padding-left: 10px;'>• {treatment}</div>", unsafe_allow_html=True)
                
                # Prevention
                prevention_title = "Prevention" if current_lang == "english" else "Pag-iwas"
                st.markdown(f"<div style='font-weight: bold; color: #2e7d32; margin: 20px 0 10px 0; font-size: 16px;'>{prevention_title}</div>", unsafe_allow_html=True)
                
                prevention_list = disease['prevention'] if current_lang == "english" else disease['tagalog']['prevention']
                for prevention in prevention_list:
                    st.markdown(f"<div style='text-align: left; margin: 5px 0; padding-left: 10px;'>• {prevention}</div>", unsafe_allow_html=True)
    else:
        st.info("🔍 No diseases found matching your search.")
    
    # Tips section at bottom
    st.markdown("""
    <div class="tip-box">
        <div style="font-weight: bold; color: #2e7d32; margin-bottom: 12px; text-align: left; font-size: 18px;">
            💡 Pro Tips for Disease Management
        </div>
        <div style="font-size: 14px; color: #424242; text-align: left; line-height: 1.8;">
            • <strong>Regular monitoring</strong> is key to early detection<br>
            • Always use <strong>certified disease-free seeds</strong><br>
            • Maintain proper <strong>field sanitation</strong><br>
            • <strong>Rotate crops</strong> to break disease cycles<br>
            • Consult <strong>agricultural extension services</strong> for severe cases
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Bottom Navigation - FIXED: should be 'library' not 'home'
    show_bottom_nav('library')