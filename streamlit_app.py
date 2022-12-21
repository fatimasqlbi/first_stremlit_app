import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinich & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#let's put a pick list so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
#Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call.
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#delete this later 'streamlit.text(fruityvice_response.json())'# just writes the data to the screen,

# take json version of the response and normalize it. 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output the secreen as a table.
streamlit.dataframe(fruityvice_normalized)

#Add a STOP Command to Focus Our Attention
streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#adding initial code for future reference. 
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * From fruit_load_list")

# version 1 - streamlit.text("Hello from Snowflake:")
# version 2 - below
#streamlit.text("The fruit load list contain:")
#streamlit.text(my_data_row)
#version 3 #Change the Streamlit Components to Make Things Look a Little Nicer and get all rows.
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contain:")
streamlit.dataframe(my_data_rows)

#Allow the end user to add a fruit to list 
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)

#copy it into your streamlit file and change the word "test" to "from streamlit" so you know where the row comes from. This wil not be correct. 
my_cur.execute("insert into fruit_load_list values ('from streamlist')")
