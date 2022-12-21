import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinich & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#let's put a pick list so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table
streamlit.dataframe(fruits_to_show)

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
       fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
       fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       return fruityvice_normalized
   
#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
   if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
   else:
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()


streamlit.header("The fruit load list contain:")
#snowflake related function
def get_fruit_load_list(): 
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * From fruit_load_list")
         return my_cur.fetchall()
      
# Add a button to load the fruit
If streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   my_cnx.close()    
   streamlit.dataframe(my_data_rows)
   streamlit.stop()
   
#Allow end user to add a fruit to list. 
def insert_row_snowflake(new_fruit):
   with my_cnx.corsor() as my_cur:
       my_cur.execute("insert into fruit_load_list values('" + ???? +"')')
                      return "Thanks for adding "+new_fruit
      
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streanlit.button('Add a Fruit to the List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   steamlit.text(back_from_function)
   
   
streamlit.write('Thanks for adding', add_my_fruit)

#this wi not work but lets just go with it. 
my_cur.execute("insert into fruit_load_list values ('from streamlist')")
   
   
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * From fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contain:")
streamlit.dataframe(my_data_rows)

#Allow the end user to add a fruit to list 



#copy it into your streamlit file and change the word "test" to "from streamlit" so you know where the row comes from. This wil not be correct. 
my_cur.execute("insert into fruit_load_list values ('from streamlist')")
