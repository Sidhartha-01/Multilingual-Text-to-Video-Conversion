import spacy
import pytextrank

def tokens_generated(finaltext):
    text = finaltext

    # print("*****************")
    nlp = spacy.load("en_core_web_sm")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    # examine the top-ranked phrases in the document
    list =[]
    for phrase in doc._.phrases[:10]:
        list.append(phrase.text)
    return list

# listuu=tokens_generated("""The Women Entrepreneurship Platform (WEP), under NITI Aayog's State Support Mission, is organizing a state-level workshop in collaboration with the Government of Goa. The workshop aims to raise awareness about WEP and its initiatives, including Udyam Uplift and support cohorts for green women entrepreneurs. The event will feature discussions on mentoring, skill development, finance access, and compliance. It will have speakers from notable organizations and government representatives like the Honorable Chief Minister of Goa. This workshop offers women entrepreneurs an opportunity to gain knowledge, share experiences, and access resources and support. It also highlights the commitment of the government and private sector to promote a more inclusive entrepreneurial ecosystem.""")
# print(listuu)

# tokens_generated("gvhjhk")
# text='''
# Union Minister of Fisheries, Animal Husbandry and Dairying, Shri Parshottam Rupala will chair a one day “National Conference on KCC for Fisheries” on 4th September 2023 at Yashwantrao Chavan Centre in Mumbai, Maharashtra. The Conference is being jointly organized by Department of Fisheries (DoF) and Department of Animal Husbandry Dairying (DAHD) to resolve pressing on-ground issues. The other dignitaries present during the event will be Minister of State, MoFAH&D - Dr. L. Murugan, Minister of State, Ministry of Finance, -Dr. Bhagwat Kishanrao Karad, Minister for Fisheries, Govt. of Maharashtra - Shri Sudhir Mungantiwar, Minister for Revenue, Animal Husbandry and Dairy Development, Govt. of Maharashtra –Shri Radhakrishna Eknathrao Vikhepatil, Secretary,DAHD- Ms Alka Upadhyaya, Secretary, DoF - Dr Abhilaksh Likhi, Joint Secretary (Inland Fisheries), Additional Secretary, DAHD - Ms Varsha Joshi, Joint Secretary (Inland Fisheries), DoF- Shri Sagar Mehra and Chief Executive, NFDB - Dr. L. Narasimha Murthy, ARS along with key representatives from financial and banking institutions namely Reserve Bank of India (RBI), Dept of Financial Services (DFS) and NABARD.
#
# Representatives from Fisheries Department of States/UTs, NFDB and other relevant Departments/Ministries, KCC beneficiaries, fishermen, fish farmers, entrepreneurs and other stakeholders from across the nation are expected to participate. The program is being organised in hybrid mode and is expected to have around 500 participants.
#
# During the event, Minister of FAH&D will distribute KCC cards to eligible fishers and fishermen. He will interact with them and address the gathering in accordance with the discussion during the conference and the way forward from welfare and policy perspectives. Special address will be shared by representatives from RBI, DFS and NABARD. During the program, guidelines/SOPs on KCC in vernacular language will be distributed. The interaction between all the stakeholders is expected to pave way for addressing issues and give long term and practical solutions for seamless flow of available credit with simplified process, checks and balances.
#
# Fisheries and aquaculture activities are an important source of food, nutrition and employment generation and is an important source of livelihood for 2.8 crore fishers and fishermen. In the last decade the sector has exhibited growth in a constituent manner and one of the key aspects that have been gained attention is availability of institutional finance to small scale fisheries’ stakeholders.
#
# Kisan Credit Card scheme was extended by the Government of India in the 2018-19 to fisheries and animal husbandry farmers to help them meet their working capital requirements. Reserve Bank of India issued the guidelines on KCC to fishers and fish farmers on 4th February 2019. Subsequently, to streamline the process of credit delivery through KCC to the Animal Husbandry and Fisheries farmers, a Standard Operating Procedure (SOP)/Guidelines was issued in consultation with the stakeholders including Ministry of AHDF, RBI, National Bank for Agriculture and Rural development (NABARD) and Indian Bank’s Association (IBA).
#
# In order to mobilise beneficiaries and boost uptake of KCC, Department of Fisheries has been pursuing all States/UTs and State Level Bankers Committee (SLBC) to sensitize and disseminate information amongst the fishers and fish farmers. In spite of various challenges, all the States/UTs and SLBC are being pursued to enhance awareness and visibility about the usefulness of KCC facility amongst the potential beneficiaries through different mode of campaigns and outreach and promotional activities. Through these continued efforts, 1.49 lakh KCC have been issued till date to fishers and fish farmers across the country.
#
# A special drive for mobilization of KCC applications was organized from 1st June to 31st December 2020 by DoF. Followed by a Nationwide campaign launched on 15th November 2021 to 31st July 2022 under the leadership of Minister of FAH&D. "Nationwide AHDF KCC Campaign" was resumed 15th September 2022 till 15th March 2023 and is now continuing from 1st May 2023 till 31st March 2024. Special KCC campaigns were also organized during Sagar Parikrama program in coastal districts. Through these campaigns, DoF endeavours to understand the bottlenecks and challenges in extending KCC facility by the financial and banking institutions while also attempting to understand the beneficiary perspective regarding their problems and constraints faced.
#
# The Kisan Credit Card is a powerful tool for financial inclusion and collaboration where activity like agriculture, fisheries, animal husbandry and dairying are treated as vital components for livelihood and income generation for large numbers of poor and marginal farmers and fishers. It represents the determination of the centre and the state entities to support its farmers and promote equitable growth.
# '''
#
#
# nlp = spacy.load("en_core_web_sm")
# # add PyTextRank to the spaCy pipeline
# nlp.add_pipe("textrank")
# doc = nlp(text)
# Name=[]
# # examine the top-ranked phrases in the document
# for phrase in doc._.phrases[:10]:
#     print(phrase.text)
#     Name.append(phrase.text)
# print(Name)
# l = []
# l = tokens_generated("""The 12th Joint Working Group (JWG) meeting between the Defence Ministries of India and Mongolia took place in Ulaanbaatar on May 16-17, 2024. The meeting was co-chaired by Joint Secretary, MoD, India Shri Amitabh Prasad and State Secretary of MoD, Mongolia Brigadier General Gankhuyag Davagdorj. India’s Ambassador to Mongolia Shri Atul Malhari Gotsurve also attended the meeting.During the JWG, both sides expressed satisfaction at the ongoing defence cooperation between the two countries. They reviewed the progress on various bilateral defence cooperation initiatives and identified means to further enhance cooperation in these areas, articulating steps in this direction. Both sides also exchanged views on the current geopolitical situation.The Joint Secretary highlighted the potential of the capacity & capability of the Indian defence industry, and looked forward to a fruitful partnership with the Armed Forces of Mongolia. The Mongolian side exuded confidence in the capacity & capability of the Indian industry. Both sides also acknowledged the growing ties between the two countries.The Joint Secretary & the Indian Ambassador also called on Deputy Defence Minister of Mongolia Mr B Bayarmagnai, and discussed bilateral cooperation issues. The delegation visited a training establishment in Ulaanbaatar and reviewed the ongoing engagements.India enjoys age-old historical, cultural and civilisational ties with Mongolia. Both countries regard each other as ‘Spiritual Neighbours’. In the modern times, values like democracy, freedom and market economy hold the two nations closer.
# MinistryofDefence12thIndiaMongoliaJointWorkingGroupmeetingtobolsterbilateraldefencetiesheldinUlaanbaatar
# 678
# India and Mongolia held their 12th Joint Working Group meeting on defense cooperation in Ulaanbaatar, co-chaired by representatives from both countries. They expressed satisfaction with current initiatives, identified areas for enhanced cooperation, and exchanged views on the geopolitical situation.  India highlighted its defense industry's potential and eagerness to partner with Mongolia, who expressed confidence in India's capabilities.  The Indian delegation also met with Mongolia's Deputy Defence Minister and visited a training establishment. The meeting underscored the strong and growing ties between the two nations, rooted in shared history, culture, and values.""")

# print(l)

