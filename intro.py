import streamlit as st

st.title("You are my love....")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.title("Dashboard", icon=":material/dashboard:")

agree = st.checkbox("I agree with me only")

if agree:
    st.write("Go to hell")
genre=st.radio(
    "What's your favourite movie genre",
    ["Comedy","Drama","Documentary"]
)

if genre=="Comedy":
    st.write("You selected comedy")
else:
    st.write("You didn't select comedy.")


num1=st.number_input("Enter a number:")
num2=st.number_input("Enter another number:")

if st.button("Add"):
    st.write("The sum of 2 numbers is :", num1 + num2)
