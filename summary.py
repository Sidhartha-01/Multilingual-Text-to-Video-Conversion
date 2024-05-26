import google.generativeai as genai

def summary_func(finaltext):
  genai.configure(api_key="AIzaSyALs5U3G39wEo-SyCuLFv-fEEWQmNkf6Pg")

  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 1000,
  }

  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  ]

  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

  convo = model.start_chat(history=[
  ])

  convo.send_message(finaltext + "Summarize the above paragraph in a paragraph inorder to deliver a 30 seconds news")
  l = convo.last.text
  # print(len(l))
  # print(convo.last.text)

  return convo.last.text


# summary_func("Under the aegis of NITI Aayog’s State Support Mission, the Women Entrepreneurship Platform (WEP) is set to host a state-level workshop in collaboration with the Government of Goa. This workshop is taking place at the CSIR-National Institute of Oceanography (NIO) Auditorium, Goa on October 3, 2023 from 9:30 am onwards. It will welcome a diverse audience of women entrepreneurs including SHGs, collectives, women clusters, government officials and private sector representatives.The Women Entrepreneurship Platform (WEP) incubated in NITI Aayog, and now transitioned into a public-private partnership is a one-stop shop for information relevant to women entrepreneurs, including SmartMatch feature for government schemes, incubators, accelerators and private sector initiatives, a community page, and mentorship module.The State Sport Mission, an umbrella initiative by NITI Aayog, is strategically designed to support states and union territories in achieving their socioeconomic goals by 2047. Under the State Support Mission, a series of workshops are being conducted to provide a platform for Centre-State exchanges and forging partnerships.This workshop marks the commencement of the WEP State Workshop series. The primary goal is to augment awareness regarding the Women Entrepreneurship Platform (WEP) and unveil a range of pioneering initiatives that WEP has embarked upon. These initiatives include Udyam Uplift a collaborative effort with AIC-GIM-WEP, as well as the introduction of support cohorts tailored for green women entrepreneurs, among other exciting Partnership.Throughout the workshop, there will be engaging fireside chats and deep dive discussions exploring topics such as mentoring, skill development, access to finance, and compliance.The workshop will boast an impressive lineup of speakers, including notable figures such as the Honorable Chief Minister of Goa, Dr. Pramod Sawant, Dr. VK Saraswat, Member NITI Aayog, B.V.R Subrahmanyam, CEO NITI Aayog. Representatives from esteemed organizations like the Bill & Melinda Gates Foundation, Reliance Foundation, Piramal Foundation, ICAI (Institute of Chartered Accountants of India), SIDBI, Ola Foundation and others will also participate. Sulakshana P Sawant, President, Goa State Women’s Self Help Group Association would grace the Valedictory session.This event will present a unique occasion for women entrepreneurs to gain knowledge, share experiences, and access valuable resources and support. Moreover, it will provide an excellent platform for the government and the private sector to showcase their dedication to supporting women entrepreneurs and creating a more inclusive and equitable entrepreneurial ecosystem.")
# print(summary_func(""" The 12th Joint Working Group (JWG) meeting between the Defence Ministries of India and Mongolia took place in Ulaanbaatar on May 16-17, 2024. The meeting was co-chaired by Joint Secretary, MoD, India Shri Amitabh Prasad and State Secretary of MoD, Mongolia Brigadier General Gankhuyag Davagdorj. India’s Ambassador to Mongolia Shri Atul Malhari Gotsurve also attended the meeting.During the JWG, both sides expressed satisfaction at the ongoing defence cooperation between the two countries. They reviewed the progress on various bilateral defence cooperation initiatives and identified means to further enhance cooperation in these areas, articulating steps in this direction. Both sides also exchanged views on the current geopolitical situation.The Joint Secretary highlighted the potential of the capacity & capability of the Indian defence industry, and looked forward to a fruitful partnership with the Armed Forces of Mongolia. The Mongolian side exuded confidence in the capacity & capability of the Indian industry. Both sides also acknowledged the growing ties between the two countries.The Joint Secretary & the Indian Ambassador also called on Deputy Defence Minister of Mongolia Mr B Bayarmagnai, and discussed bilateral cooperation issues. The delegation visited a training establishment in Ulaanbaatar and reviewed the ongoing engagements.India enjoys age-old historical, cultural and civilisational ties with Mongolia. Both countries regard each other as ‘Spiritual Neighbours’. In the modern times, values like democracy, freedom and market economy hold the two nations closer.
# MinistryofDefence12thIndiaMongoliaJointWorkingGroupmeetingtobolsterbilateraldefencetiesheldinUlaanbaatar
# 678
# India and Mongolia held their 12th Joint Working Group meeting on defense cooperation in Ulaanbaatar, co-chaired by representatives from both countries. They expressed satisfaction with current initiatives, identified areas for enhanced cooperation, and exchanged views on the geopolitical situation.  India highlighted its defense industry's potential and eagerness to partner with Mongolia, who expressed confidence in India's capabilities.  The Indian delegation also met with Mongolia's Deputy Defence Minister and visited a training establishment. The meeting underscored the strong and growing ties between the two nations, rooted in shared history, culture, and values. """))


# import openai
# import io
# def summary_func(finaltext):
#     if(len(finaltext)>=1000):
#         openai.api_key = 'sk-proj-KdZPOeJMEdKcBSpQGI9lT3BlbkFJ1iUbYMYMUzjuk2DsTrRr'
#         # sk - HviJ526uNUj9w1Cs5p9MT3BlbkFJMworQkDMxWAMGH4CBw9Y

#         messages = [
#             {"role": "system", "content": "You are a smart summarization system. Summarize the given text into 1000 characters and retun the output to user "} ,
#         ]

#         item= finaltext
#         replies = []


#         # sleep(20)
#         #print(item)
#         message = "Annotate this text: "+str(item)
#         if message:
#           messages.append(
#             {"role": "user", "content": message},
#             )
#           chat = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo", messages=messages
#             )

#         reply = chat.choices[0].message.content
#         replies.append(reply)
#         # print(f"ChatGPT: {reply}")
#         return reply
#     else:
#         return finaltext

# t=summary_func("Under the aegis of NITI Aayog’s State Support Mission, the Women Entrepreneurship Platform (WEP) is set to host a state-level workshop in collaboration with the Government of Goa. This workshop is taking place at the CSIR-National Institute of Oceanography (NIO) Auditorium, Goa on October 3, 2023 from 9:30 am onwards. It will welcome a diverse audience of women entrepreneurs including SHGs, collectives, women clusters, government officials and private sector representatives.The Women Entrepreneurship Platform (WEP) incubated in NITI Aayog, and now transitioned into a public-private partnership is a one-stop shop for information relevant to women entrepreneurs, including SmartMatch feature for government schemes, incubators, accelerators and private sector initiatives, a community page, and mentorship module.The State Sport Mission, an umbrella initiative by NITI Aayog, is strategically designed to support states and union territories in achieving their socioeconomic goals by 2047. Under the State Support Mission, a series of workshops are being conducted to provide a platform for Centre-State exchanges and forging partnerships.This workshop marks the commencement of the WEP State Workshop series. The primary goal is to augment awareness regarding the Women Entrepreneurship Platform (WEP) and unveil a range of pioneering initiatives that WEP has embarked upon. These initiatives include Udyam Uplift a collaborative effort with AIC-GIM-WEP, as well as the introduction of support cohorts tailored for green women entrepreneurs, among other exciting Partnership.Throughout the workshop, there will be engaging fireside chats and deep dive discussions exploring topics such as mentoring, skill development, access to finance, and compliance.The workshop will boast an impressive lineup of speakers, including notable figures such as the Honorable Chief Minister of Goa, Dr. Pramod Sawant, Dr. VK Saraswat, Member NITI Aayog, B.V.R Subrahmanyam, CEO NITI Aayog. Representatives from esteemed organizations like the Bill & Melinda Gates Foundation, Reliance Foundation, Piramal Foundation, ICAI (Institute of Chartered Accountants of India), SIDBI, Ola Foundation and others will also participate. Sulakshana P Sawant, President, Goa State Women’s Self Help Group Association would grace the Valedictory session.This event will present a unique occasion for women entrepreneurs to gain knowledge, share experiences, and access valuable resources and support. Moreover, it will provide an excellent platform for the government and the private sector to showcase their dedication to supporting women entrepreneurs and creating a more inclusive and equitable entrepreneurial ecosystem.")
# print(t)