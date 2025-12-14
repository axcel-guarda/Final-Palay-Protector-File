# utils/disease_info.py
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
    # Note: Add other 10 diseases here following the same structure
    # Due to character limit, I'm showing 2 examples
]
