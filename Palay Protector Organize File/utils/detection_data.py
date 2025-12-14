DISEASE_INFO = {
    "Bacterial Leaf Blight": {
        "description": "A bacterial disease causing water-soaked lesions that turn yellow to white. This serious infection can spread rapidly in warm, humid conditions and may cause significant yield loss if left untreated.",
        "severity": "High", 
        "severity_color": "#f44336",
        "tagalog": {
            "description": "Isang bakteryal na sakit na nagdudulot ng basang-basa na sugat na nagiging dilaw hanggang puti. Ang seryosong impeksyon na ito ay maaaring kumalat nang mabilis sa mainit at mahalumigmig na kondisyon at maaaring magdulot ng malaking pagkalugi sa ani kung hindi gagamutin.",
            "severity": "Mataas"
        }
    },
    "Brown Spot": {
        "description": "Circular brown lesions that reduce photosynthesis and grain quality. This fungal disease is often associated with nutrient deficiency and can affect both leaves and grains.",
        "severity": "Moderate", 
        "severity_color": "#ff9800",
        "tagalog": {
            "description": "Bilog na kayumangging sugat na bumababa ang photosynthesis at kalidad ng butil. Ang fungal na sakit na ito ay kadalasang nauugnay sa kakulangan ng sustansya at maaaring makaapekto sa mga dahon at butil.",
            "severity": "Katamtaman"
        }
    },
    "Healthy Rice": {
        "description": "Your rice plant appears healthy with no disease symptoms detected. Continue with proper care and regular monitoring to maintain plant health.",
        "severity": "None", 
        "severity_color": "#4CAF50",
        "tagalog": {
            "description": "Ang iyong palay ay malusog at walang sintomas ng sakit na nakita. Magpatuloy sa tamang pag-aalaga at regular na pagsubaybay upang mapanatili ang kalusugan ng halaman.",
            "severity": "Wala"
        }
    },
    "Leaf Blast": {
        "description": "Diamond-shaped lesions with gray centers that can cause up to 50% yield loss. This is one of the most destructive rice diseases worldwide.",
        "severity": "High", 
        "severity_color": "#f44336",
        "tagalog": {
            "description": "Hugis-diyamante na sugat na may kulay-abong gitna na maaaring magdulot ng hanggang 50% na pagkalugi sa ani. Isa ito sa pinaka-mapaminsalang sakit ng palay sa buong mundo.",
            "severity": "Mataas"
        }
    },
    "Leaf Scald": {
        "description": "Large white-centered lesions with brown borders that reduce leaf function and yield. This bacterial disease thrives in high humidity.",
        "severity": "High", 
        "severity_color": "#f44336",
        "tagalog": {
            "description": "Malalaking sugat na may puting gitna at kayumangging hangganan na bumababa ang gawain ng dahon at ani. Ang bakteryal na sakit na ito ay umuunlad sa mataas na halumigmig.",
            "severity": "Mataas"
        }
    },
    "Neck Blast": {
        "description": "Infects the panicle neck, leading to poor grain filling and significant yield loss. Infected panicles may turn white or gray and produce empty grains.",
        "severity": "High", 
        "severity_color": "#f44336",
        "tagalog": {
            "description": "Nahawahan ang leeg ng panicle, nangunguna sa mahinang pagpuno ng butil at malaking pagkalugi sa ani. Ang mga nahawahang panicle ay maaaring maging puti o kulay-abo at gumawa ng walang laman na butil.",
            "severity": "Mataas"
        }
    },
    "Rice Hispa": {
        "description": "Insect pest scraping chlorophyll and leaving white streaks on leaves. Adult beetles and larvae feed on leaf tissue, reducing photosynthetic capacity.",
        "severity": "Moderate", 
        "severity_color": "#ff9800",
        "tagalog": {
            "description": "Peste ng insekto na nag-aalis ng chlorophyll at nag-iiwan ng puting guhit sa mga dahon. Ang mga adult na beetles at larvae ay kumakain ng tissue ng dahon, na binabawasan ang kakayahang photosynthetic.",
            "severity": "Katamtaman"
        }
    },
    "Rice Tungro": {
        "description": "A viral disease causing orange-yellow discoloration and stunted growth. Transmitted by green leafhoppers, it can severely reduce yields and plant vigor.",
        "severity": "High", 
        "severity_color": "#f44336",
        "tagalog": {
            "description": "Viral na sakit na nagdudulot ng orange-dilaw na pagbabago ng kulay at pagkaantala ng paglaki. Ipinasa ng mga berdeng leafhopper, lubhang maaaring bawasan ang ani at sigla ng halaman.",
            "severity": "Mataas"
        }
    },
    "Sheath Blight": {
        "description": "Irregular greenish-gray lesions on leaf sheaths causing lodging and yield loss. This fungal disease spreads rapidly in dense plantings with high nitrogen.",
        "severity": "Moderate", 
        "severity_color": "#ff9800",
        "tagalog": {
            "description": "Hindi regular na berde-kulay-abong sugat sa mga balat ng dahon na nagdudulot ng pagbagsak at pagkalugi sa ani. Ang fungal na sakit na ito ay kumakalat nang mabilis sa siksikang pagtatanim na may mataas na nitrogen.",
            "severity": "Katamtaman"
        }
    },
    "Non Plant Object": {
        "description": "This is not a rice plant image. Please upload a valid rice leaf photo for accurate disease detection.",
        "severity": "N/A", 
        "severity_color": "#9e9e9e",
        "is_non_plant": True,
        "tagalog": {
            "description": "Hindi ito larawan ng palay. Mangyaring mag-upload ng wastong larawan ng dahon ng palay para sa tumpak na pagtuklas ng sakit.",
            "severity": "N/A"
        }
    }
}

def normalize_disease_name(name):
    name = name.strip().replace("_", " ").replace("-", " ").title()

    # Fix: Handle "Shealth Bligh" from your folder name
    if "Shealth" in name or "Sheath" in name or "Bligh" in name:
        return "Sheath Blight"
    if "Healthy" in name: 
        return "Healthy Rice"
    if "Hispa" in name: 
        return "Rice Hispa"
    if "Neck" in name: 
        return "Neck Blast"
    if "Leaf Blast" in name or "Blast" in name: 
        return "Leaf Blast"
    if "Non" in name: 
        return "Non Plant Object"

    # Direct matches for your folder names
    if name == "Bacterial Leaf Blight":
        return "Bacterial Leaf Blight"
    if name == "Brown Spot":
        return "Brown Spot"
    if name == "Leaf Scald":
        return "Leaf Scald"
    if name == "Rice Tungro":
        return "Rice Tungro"

    return name