from covid import Covid

covid = Covid()
covid.get_data()
country = input("please enter your countery : ")
data = covid.get_status_by_country_name(F"{country}")
active = covid.get_total_active_cases()
print("status of the country is : ",data)
