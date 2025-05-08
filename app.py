import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def stats(dataframe):
    st.header('Data Statistics')
    st.write(dataframe.describe())

def header(dataframe):
    st.header('Data Header')
    st.write(dataframe.head())

def plot(dataframe):
    fig ,ax= plt.subplots(1,1)
    ax.scatter(x = dataframe['Depth'],y=dataframe['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    st.pyplot(fig)
def home():
    st.title('Hello world!')
    st.markdown(' mark down ##Baby ')
    st.sidebar.title('Navigation')

def interactive_plot(dataframe):
    x_axis_val = st.selectbox('Select X-Axis Values',options=df.columns)
    y_axis_val = st.selectbox('Select Y-Axis Values',options=df.columns)
    col = st.color_picker('Select a plot color')
    plot = px.scatter(dataframe,x=x_axis_val,y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

uploaded_file = st.sidebar.file_uploader('upload your file here please!')

options = st.sidebar.radio('Pages',options=
                           ['Home',
                            'Data Statistics',
                            'Data Header',
                            'Plot',
                            'Interactive Plot'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if options == 'home':
        home()
    if options == 'Data Statistics':
        stats(df)
    elif options == 'Data Header':
        header(df)
    elif options == 'Plot':
        plot(df)
    elif options == 'Interactive Plot':
        interactive_plot(df)
