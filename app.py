#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import joblib
import numpy as np


# In[2]:


model = joblib.load('model.pkl')
model


# In[3]:


scaler = joblib.load('scaler.bin')
scaler


# In[4]:


app = Flask(__name__)


# In[5]:


nations = ['Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile',
        'China', 'Czech Republic', 'Denmark', 'Egypt', 'Finland', 'France',
        'Germany', 'Greece', 'Hong Kong', 'Hungary', 'India', 'Iran',
        'Israel', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'New Zealand',
        'Norway', 'Poland', 'Portugal', 'Republic of Ireland',
        'Russian Federation', 'Saudi Arabia', 'Serbia', 'Singapore',
        'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sweden',
        'Switzerland', 'Taiwan', 'Turkey', 'United Kingdom',
        'United States of America']
cntry_encoded = np.arange(0,42,1)
countries = dict(zip(nations,cntry_encoded))
schools = ['Aalborg University', 'Aalto University', 'Aarhus University',
        'Aix Marseille University', 'Aix-Marseille University',
        'Aristotle University of Thessaloniki', 'Arizona State University',
        'Arizona State University - Tempe', 'Auburn University',
        'Autonomous University of Barcelona',
        'Autonomous University of Madrid', 'Bangor University',
        'Bar-Ilan University', 'Baylor College of Medicine',
        'Beihang University', 'Beijing Normal University',
        'Beijing University of Aeronautics and Astronautics',
        'Ben-Gurion University of the Negev', 'Bielefeld University',
        'Birkbeck, University of London', 'Boston College',
        'Boston University', 'Brandeis University',
        'Brigham Young University', 'Brown University',
        'Brunel University', 'Cairo University',
        'California Institute of Technology', 'Capital Medical University',
        'Capital University of Medical Sciences', 'Cardiff University',
        'Carleton University', 'Carnegie Mellon University',
        'Case Western Reserve University', 'Catholic University of Chile',
        'Catholic University of Korea', 'Catholic University of Leuven',
        'Catholic University of Louvain',
        'Catholic University of the Sacred Heart',
        'Central South University', 'Chalmers University of Technology',
        'Chang Gung University', 'Charles University in Prague',
        'Chiba University', 'China Agricultural University',
        'China Medical University', 'Chungnam National University',
        'City University of Hong Kong',
        'City University of New York City College',
        'Claude Bernard University Lyon 1', 'Clemson University',
        'College of France', 'Colorado State University',
        'Columbia University', 'Complutense University of Madrid',
        'Concordia University', 'Cornell University',
        'Cranfield University', 'Curtin University',
        'Curtin University of Technology', 'Dalhousie University',
        'Dalian University of Technology', 'Dartmouth College',
        'Deakin University', 'Delft University of Technology',
        'Dresden University of Technology', 'Drexel University',
        'Duke University', 'Durham University', 'ESPCI ParisTech',
        'East China University of Science and Technology',
        'Ecole National Superieure Mines - Paris',
        'Ecole Normale Superieure - Lyon',
        'Ecole Normale Superieure - Paris', 'Ecole Polytechnique',
        'Ehime University', 'Eindhoven University of Technology',
        'Emory University', 'Eotvos Lorand University',
        'Erasmus University', 'Ewha Womans University',
        'Federal University of Minas Gerais',
        'Federal University of Rio Grande do Sul',
        'Federal University of Rio de Janeiro',
        'Federal University of Sao Paulo', 'Flinders University',
        'Florida International University', 'Florida State University',
        'Fudan University', 'George Mason University',
        'Georgetown University', 'Georgia Institute of Technology',
        'Ghent University', 'Gifu University', 'Griffith University',
        'Gunma University', 'Hacettepe University',
        'Hannover Medical School', 'Hanyang University',
        'Harbin Institute of Technology', 'Harvard University',
        'Heidelberg University', 'Henri Poincare University (Nancy 1)',
        'Hiroshima University', 'Hokkaido University', 'Howard University',
        'Huazhong University of Science and Technology',
        'Icahn School of Medicine at Mount Sinai',
        'Indian Institute of Science',
        'Indian Institute of Technology Kharagpur',
        'Indiana University Bloomington',
        'Indiana University-Purdue University at Indianapolis',
        'Industrial Physics and Chemistry Higher Educational Institution - Paris',
        'International School for Advanced Studies',
        'Iowa State University', 'Istanbul University',
        'Jagiellonian University', 'James Cook University',
        'Jilin University', 'Johns Hopkins University',
        'Joseph Fourier University (Grenoble 1)', 'Juntendo University',
        'KTH Royal Institute of Technology', 'KU Leuven',
        'Kagoshima University', 'Kanazawa University',
        'Kansas State University',
        'Karlsruhe Institute of Technology (KIT)', 'Karolinska Institute',
        'Keio University', 'Kent State University',
        'King Abdulaziz University',
        'King Abdullah University of Science and Technology',
        'King Fahd University of Petroleum & Minerals',
        'King Saud University', "King's College London", 'Kobe University',
        'Korea Advanced Institute of Science and Technology',
        'Korea University', 'Kumamoto University', 'Kyoto University',
        'Kyung Hee University', 'Kyungpook National University',
        'Kyushu University', 'La Trobe University', 'Lancaster University',
        'Lanzhou University', 'Laval University', 'Lehigh University',
        'Leiden University', 'Linkoping University',
        'London School of Economics and Political Science',
        'London School of Hygiene & Tropical Medicine',
        'London School of Hygiene and Tropical Medicine',
        'Loughborough University',
        'Louisiana State University - Baton Rouge',
        'Louisiana State University Health Sciences Center',
        'Loyola University Chicago', 'Lund University', 'MINES ParisTech',
        'Maastricht University', 'Macquarie University',
        'Massachusetts Institute of Technology (MIT)', 'Massey University',
        'Mayo Medical School', 'McGill University', 'McMaster University',
        'Medical College of Georgia', 'Medical College of Wisconsin',
        'Medical University of Graz', 'Medical University of Innsbruck',
        'Medical University of South Carolina',
        'Medical University of Vienna',
        'Memorial University of Newfoundland', 'Michigan State University',
        'Michigan Technological University',
        'Mississippi State University', 'Monash University',
        'Montana State University - Bozeman', 'Moscow State University',
        'Mount Sinai School of Medicine', 'Murdoch University',
        'Nagasaki University', 'Nagoya University',
        'Nanjing Medical University', 'Nanjing University',
        'Nankai University', 'Nanyang Technological University',
        'Nara Institute of Science and Technology',
        'National Autonomous University of Mexico',
        'National Central University', 'National Cheng Kung University',
        'National Chiao Tung University',
        'National Sun Yat-Sen University', 'National Taiwan University',
        'National Tsing Hua University',
        'National University of Singapore',
        'National Yang Ming University',
        'National and Kapodistrian University of Athens',
        'New Jersey Institute of Technology',
        'New Mexico State University', 'New York University',
        'Newcastle University', 'Nihon University', 'Niigata University',
        'North Carolina State University - Raleigh',
        'Northeastern University', 'Northern Arizona University',
        'Northwestern University',
        'Norwegian University of Science and Technology',
        'Norwegian University of Science and Technology - NTNU',
        'Ohio University', 'Okayama University',
        'Oklahoma State University', 'Old Dominion University',
        'Oregon Health and Science University', 'Oregon State University',
        'Osaka City University', 'Osaka Prefecture University',
        'Osaka University', 'Paris Dauphine University (Paris 9)',
        'Paul Sabatier University (Toulouse 3)',
        'Peking Union Medical College', 'Peking University',
        'Pennsylvania State University - University Park',
        'Pierre and Marie  Curie University - Paris 6',
        'Pohang University of Science and Technology',
        'Polytechnic Institute of Milan',
        'Polytechnic University of Catalonia',
        'Polytechnic University of Turin',
        'Polytechnic University of Valencia', 'Pompeu Fabra University',
        'Portland State University', 'Princeton University',
        'Purdue University - West Lafayette', 'Pusan National University',
        'Queen Mary University of London', 'Queen Mary, U. of London',
        'Queen Mary, University of London', "Queen's University",
        "Queen's University Belfast",
        'Queensland University of Technology', 'RWTH Aachen University',
        'Radboud University Nijmegen', 'Rensselaer Polytechnic Institute',
        'Rice University', 'Rockefeller University',
        'Royal Holloway, U. of London', 'Royal Institute of Technology',
        'Rush University', 'Rutgers, The State University of New Jersey',
        'Rutgers, The State University of New Jersey - New Brunswick',
        'SUNY at Albany', 'Saarland University', 'Saint Louis University',
        'Saint Petersburg State University', 'San Diego State University',
        'Sao Paulo State University', 'Sapienza University of Rome',
        'Scuola Normale Superiore - Pisa', 'Seoul National University',
        'Shandong University', 'Shanghai Jiao Tong University',
        'Sharif University of Technology', 'Sichuan University',
        'Simon Fraser University', 'Soochow University',
        'South China University of Technology', 'Southeast University',
        'Southern Methodist University', 'Stanford University',
        'State University of Campinas',
        'State University of New York Health Science Center at Brooklyn',
        'State University of New York at Albany',
        'State University of New York at Buffalo',
        'State University of New York at Stony Brook',
        'Stellenbosch University', 'Stockholm School of Economics',
        'Stockholm University', 'Stony Brook University',
        'Sun Yat-sen University', 'Sungkyunkwan University',
        'Swansea Univ', 'Swedish University of Agricultural Sciences',
        'Swinburne University of Technology',
        'Swiss Federal Institute of Technology Lausanne',
        'Swiss Federal Institute of Technology Zurich',
        'Swiss Federal Institute of Technology of Lausanne',
        'Syracuse University', 'TU Dresden',
        'Technical University Darmstadt', 'Technical University Munich',
        'Technical University of Berlin',
        'Technical University of Braunschweig',
        'Technical University of Denmark',
        'Technion-Israel Institute of Technology', 'Tel Aviv University',
        'Temple University', 'Texas A & M University',
        'Texas A&M University', 'Texas A&M University - College Station',
        'Texas Tech University', 'The Australian National University',
        'The Chinese University of Hong Kong',
        'The College of  William and Mary',
        'The George Washington University',
        'The Graduate University for Advanced Studies',
        'The Hebrew University of Jerusalem',
        'The Hong Kong Polytechnic University',
        'The Hong Kong University of Science and Technology',
        'The Imperial College of Science, Technology and Medicine',
        'The Johns Hopkins University',
        'The Ohio State University - Columbus', 'The Open University',
        'The Royal Veterinary and Agricultural University',
        'The University of Adelaide', 'The University of Akron',
        'The University of Alabama at Birmingham',
        'The University of Auckland', 'The University of Calgary',
        'The University of Connecticut - Storrs',
        'The University of Connecticut Health Center',
        'The University of Dundee', 'The University of Edinburgh',
        'The University of Georgia', 'The University of Glasgow',
        'The University of Hong Kong', 'The University of Manchester',
        'The University of Melbourne', 'The University of Memphis',
        'The University of Montana - Missoula',
        'The University of New Mexico - Albuquerque',
        'The University of New South Wales',
        'The University of Newcastle, Australia',
        'The University of Queensland', 'The University of Reading',
        'The University of Sheffield',
        'The University of Texas Health Science Center at Houston',
        'The University of Texas Health Science Center at San Antonio',
        'The University of Texas M. D. Anderson Cancer Center',
        'The University of Texas Medical Branch at Galveston',
        'The University of Texas Southwestern Medical Center at Dallas',
        'The University of Texas at Austin',
        'The University of Texas at Dallas',
        'The University of Texas at San Antonio',
        'The University of Tokushima', 'The University of Tokyo',
        'The University of Western Australia',
        'Thomas Jefferson University', 'Tianjin University',
        'Tilburg University', 'Tohoku University',
        'Tokyo Institute of Technology',
        'Tokyo Medical and Dental University',
        'Tokyo Metropolitan University',
        'Tokyo University of Agriculture and Technology',
        'Tokyo University of Science', 'Tongji University',
        'Toulouse School of Economics', 'Trinity College Dublin',
        'Tsinghua University', 'Tufts University', 'Tulane University',
        'UNESP', 'Umea University', 'University College Cork',
        'University College Dublin', 'University College London',
        'University Libre Bruxelles', 'University Paris Diderot - Paris 7',
        'University at Albany (State University of New York)',
        'University at Buffalo, the State University of New York',
        'University of Aberdeen', 'University of Alabama at Birmingham',
        'University of Alaska - Fairbanks', 'University of Alberta',
        'University of Amsterdam', 'University of Antwerp',
        'University of Arizona', 'University of Arkansas at Fayetteville',
        'University of Arkansas at Little Rock', 'University of Auvergne',
        'University of Barcelona', 'University of Bari',
        'University of Basel', 'University of Bath',
        'University of Bayreuth', 'University of Belgrade',
        'University of Bergen', 'University of Bern',
        'University of Bielefeld', 'University of Birmingham',
        'University of Bochum', 'University of Bologna',
        'University of Bonn', 'University of Bordeaux',
        'University of Bordeaux 1', 'University of Bradford',
        'University of Bremen', 'University of Bristol',
        'University of British Columbia', 'University of Buenos Aires',
        'University of Cagliari', 'University of Calcutta',
        'University of California, Berkeley',
        'University of California, Davis',
        'University of California, Irvine',
        'University of California, Los Angeles',
        'University of California, Riverside',
        'University of California, San Diego',
        'University of California, San Francisco',
        'University of California, Santa Barbara',
        'University of California, Santa Cruz',
        'University of California-Berkeley', 'University of Cambridge',
        'University of Campinas', 'University of Canterbury',
        'University of Cape Town', 'University of Central Florida',
        'University of Chicago', 'University of Chile',
        'University of Cincinnati', 'University of Coimbra',
        'University of Colorado Health Science Center',
        'University of Colorado at Boulder',
        'University of Colorado at Denver', 'University of Connecticut',
        'University of Copenhagen', 'University of Delaware',
        'University of Dortmund', 'University of Duesseldorf',
        'University of Duisburg-Essen', 'University of Durham',
        'University of East Anglia', 'University of Eastern Finland',
        'University of Erlangen-Nuremberg', 'University of Essex',
        'University of Exeter', 'University of Ferrara',
        'University of Florence', 'University of Florida',
        'University of Frankfurt', 'University of Freiburg',
        'University of Fribourg', 'University of Geneva',
        'University of Genoa', 'University of Genova',
        'University of Giessen', 'University of Goettingen',
        'University of Gothenburg', 'University of Granada',
        'University of Graz', 'University of Greifswald',
        'University of Groningen', 'University of Guelph',
        'University of Haifa', 'University of Halle-Wittenberg',
        'University of Hamburg', 'University of Hannover',
        'University of Hawaii at Manoa', 'University of Heidelberg',
        'University of Helsinki', 'University of Hertfordshire',
        'University of Houston', 'University of Idaho',
        'University of Illinois at Chicago',
        'University of Illinois at Urbana-Champaign',
        'University of Innsbruck', 'University of Iowa',
        'University of Jena', 'University of Jyvaskyla',
        'University of Kansas', 'University of Kansas - Lawrence',
        'University of Kansas Medical Center', 'University of Karlsruhe',
        'University of Kentucky', 'University of Kiel',
        'University of Koeln', 'University of Konstanz',
        'University of KwaZulu-Natal', 'University of Lausanne',
        'University of Leeds', 'University of Leicester',
        'University of Leipzig', 'University of Liege',
        'University of Lille 1', 'University of Lisbon',
        'University of Liverpool', 'University of Ljubljana',
        'University of Lorraine', 'University of Louisville',
        'University of Maastricht', 'University of Maine',
        'University of Mainz', 'University of Malaya',
        'University of Manitoba', 'University of Marburg',
        'University of Maryland, Baltimore',
        'University of Maryland, Baltimore County',
        'University of Maryland, College Park',
        'University of Massachusetts Amherst',
        'University of Massachusetts Medical School - Worcester',
        'University of Medicine and Dentistry New Jersey',
        'University of Melbourne', 'University of Miami',
        'University of Michigan - Ann Arbor',
        'University of Michigan-Ann Arbor', 'University of Milan',
        'University of Milan - Bicocca',
        'University of Minnesota, Twin Cities',
        'University of Mississippi', 'University of Missouri - Columbia',
        'University of Montana - Missoula', 'University of Montpellier',
        'University of Montpellier 2', 'University of Montreal',
        'University of Muenster', 'University of Munich',
        'University of Naples Federico II',
        'University of Nebraska - Lincoln',
        'University of Nebraska Medical Center',
        'University of Nevada - Reno', 'University of New England',
        'University of New Hampshire - Durham',
        'University of New South Wales', 'University of Newcastle',
        'University of Nice Sophia Antipolis',
        'University of North Carolina at Chapel Hill',
        'University of Notre Dame', 'University of Nottingham',
        'University of Oklahoma - Norman', 'University of Oregon',
        'University of Oslo', 'University of Otago',
        'University of Ottawa', 'University of Oulu',
        'University of Oxford', 'University of Padua',
        'University of Palermo', 'University of Paris Dauphine (Paris 9)',
        'University of Paris Descartes (Paris 5)',
        'University of Paris Diderot (Paris 7)',
        'University of Paris Sud (Paris 11)',
        'University of Paris-Sud (Paris 11)', 'University of Parma',
        'University of Pavia', 'University of Pennsylvania',
        'University of Perugia', 'University of Pisa',
        'University of Pittsburgh',
        'University of Pittsburgh, Pittsburgh Campus',
        'University of Pittsburgh-Pittsburgh Campus',
        'University of Pompeu Fabra', 'University of Porto',
        'University of Pretoria',
        'University of Provence (Aix-Marseille 1)', 'University of Quebec',
        'University of Regensburg', 'University of Rennes 1',
        'University of Rhode Island', 'University of Rochester',
        'University of Roma - La Sapienza',
        'University of Roma - Tor Vergata', 'University of Rostock',
        'University of Santiago Compostela', 'University of Sao Paulo',
        'University of Saskatchewan',
        'University of Science and Technology of China',
        'University of Science, Malaysia', 'University of Sevilla',
        'University of Seville', 'University of Sherbrooke',
        'University of Siena', 'University of South Carolina - Columbia',
        'University of South Florida', 'University of Southampton',
        'University of Southern California',
        'University of Southern Denmark', 'University of St Andrews',
        'University of Strasbourg', 'University of Strathclyde',
        'University of Stuttgart', 'University of Surrey',
        'University of Sussex', 'University of Sydney',
        'University of Szeged', 'University of Tasmania',
        'University of Technology, Sydney', 'University of Tehran',
        'University of Tennessee - Knoxville',
        'University of Tennessee Health Science Center',
        'University of Toronto', 'University of Trieste',
        'University of Tromso', 'University of Tsukuba',
        'University of Tuebingen', 'University of Turin',
        'University of Turku', 'University of Twente', 'University of Ulm',
        'University of Utah', 'University of Valencia',
        'University of Vermont', 'University of Versailles',
        'University of Victoria', 'University of Vienna',
        'University of Vigo', 'University of Virginia',
        'University of Wageningen', 'University of Warsaw',
        'University of Warwick', 'University of Washington',
        'University of Waterloo', 'University of Wisconsin - Madison',
        'University of Wisconsin - Milwaukee', 'University of Wollongong',
        'University of Wroclaw', 'University of Wuerzburg',
        'University of Wyoming', 'University of York',
        'University of Zagreb', 'University of Zaragoza',
        'University of Zurich', 'University of the Basque Country',
        'University of the Mediterranean (Aix-Marseille 2)',
        'University of the Witwatersrand',
        'Université libre de Bruxelles (ULB)', 'Uppsala University',
        'Utah State University', 'Utrecht University',
        'VU University Amsterdam', 'Vanderbilt University',
        'Victor Segalen Bordeaux 2 University',
        'Victoria University of Wellington',
        'Vienna University of Technology',
        'Virginia Commonwealth University',
        'Virginia Polytechnic Institute and State University',
        'Vrije Universiteit Brussel (VUB)', 'Vrije University Brussel',
        'Wake Forest University', 'Waseda University',
        'Washington State University',
        'Washington State University - Pullman',
        'Washington University in St. Louis', 'Wayne State University',
        'Weizmann Institute of Science', 'West Virginia University',
        'Western University',
        'Western University (The University of Western Ontario)',
        'Wuhan University', 'Xiamen University',
        'Xian Jiao Tong University', 'Yale University',
        'Yamaguchi University', 'Yeshiva University', 'Yonsei University',
        'York University', 'Zhejiang University']
uni_encoded = np.arange(0,658,1)
universities = dict(zip(schools,uni_encoded))


# In[6]:


@app.route("/")
def home():
    return render_template('home.html',country_names=countries,university_names=universities)


# In[7]:


@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        uni_name = request.form['university']
        university = int(universities[uni_name])
        nation = request.form['country']
        country = int(countries[nation])
        national_rank = float(request.form['country_rank'])
        score = float(request.form['total_score'])  # 23.5 to 100.0
        # alumni to ns: 0.0 to 100.0
        alumni = float(request.form['alumni_score'])
        award = float(request.form['award_score'])
        hici = float(request.form['hici_score'])
        ns = float(request.form['ns_score'])
        pub = float(request.form['pub_score'])  # 7.3 to 100.0
        pcp = float(request.form['pcp_score'])  # 8.3 to 100.0
        year = int(request.form['year'])  # 2005 to 2015  
        scaled_input = scaler.transform([[university,
            country,
            national_rank,
            score,
            alumni,
            award,
            hici,
            ns,
            pub,
            pcp,
            year]])
        predictions = model.predict(scaled_input)
        output = round(abs(predictions[0])*143.488)
        return render_template('home.html',prediction_text="The world rank of the given university is {}.".format(output),country_names=countries,university_names=universities)


# In[ ]:


if __name__ == '__main__':
    app.run(port=8080)

