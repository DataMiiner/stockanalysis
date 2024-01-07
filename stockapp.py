import pandas as pd
import yfinance as yf
import time as t
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as pt

st.set_page_config(
  page_title="Stock Analysis",
  page_icon="chart_with_upwards_trend",
  layout="wide"
)
st.title("STOCKS ANALYSIS")
#sidebar
st.sidebar.info("stocks analysis 📈")
ticker=st.sidebar.text_input("Ticker")
start_date=st.sidebar.date_input("start Date")
end_date=st.sidebar.date_input("End Date")
fetch=st.sidebar.button("Submit")


#fetch data
if fetch==True:
      
      s_data=yf.download(ticker,start_date,end_date)
      
      max=s_data[["Open","Close","Volume","High","Low"]][s_data["Close"]==s_data["Close"].max()]
      mins=s_data[["Open","Close","Volume","High","Low"]][s_data["Close"]==s_data["Close"].min()]
      max_vol=s_data[["Open","Close","Volume","High","Low"]][s_data["Volume"]==s_data["Volume"].max()]
      min_vol=s_data[["Open","Close","Volume","High","Low"]][s_data["Volume"]==s_data["Volume"].min()]
      with st.spinner("We are Gathering Data"):
          t.sleep(3)
          
      if s_data is not None:
          st.success(f"Ticker: {ticker} &nbsp;&nbsp;&nbsp; Start Date: {start_date}&nbsp;&nbsp;&nbsp;&nbsp;End Date: {end_date}")
          st.write(s_data)
          
        
          col1,col2=st.columns([1,1])
          col3,col4=st.columns([1,1])  
          with col1:           
            st.info("Max Close price")
            st.write(max)
          with col2:
            st.info("Min Close price ")
            st.write(mins)
          with col3:
            st.info("Max Volume ")
            st.write(max_vol)
          with col4:
            st.info("Min Volume") 
            st.write(min_vol) 
          st.title("  ") 
          st.subheader(f"Graphical Analysis : {ticker}") 
            
          
          #Tabs
          lin,bar=st.tabs(['Line Graph','Bar Graph'])
          with lin:
                
                fig = px.line(s_data, x=s_data.index, y=['Close','Open','High','Low'], title=f"Line Graph")
                st.plotly_chart(fig)
          with bar:
                fig = px.bar(s_data, x=s_data.index, y=s_data['Close'],title="Bar Graph")
                st.plotly_chart(fig) 
      else:
          st.error("Sorry!, There is some error")

          

 