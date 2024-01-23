import pandas as pd
import yfinance as yf
import time as t
import streamlit as st
import plotly.express as px
#By DataMiiner
#define st
if "ticker" not in st.session_state:
  st.session_state["ticker"]=""
if "start_date" not in st.session_state:
  st.session_state["start_date"]=""
if "end_date" not in st.session_state:
  st.session_state["end_date"]=""    

st.set_page_config(
  page_title="Stock Analysis",
  page_icon="chart_with_upwards_trend",
  layout="wide"
)

st.title("STOCKS ANALYSIS")
#sidebar
st.sidebar.info("stocks analysis 📈")
a=st.sidebar.text_input("Ticker name(for eg: 'AAPL')")
b=st.sidebar.date_input("start Date")
c=st.sidebar.date_input("End Date")
st.session_state["fetch"]=st.sidebar.button("Submit")


#fetch data
if st.session_state["fetch"]:
     st.session_state["fetch"]=False  
     st.session_state["ticker"]=a
     st.session_state["start_date"]=b
     st.session_state["end_date"]=c
     with st.spinner("We are Gathering Data"):
          t.sleep(3)

try:          
      s_data=yf.download(st.session_state["ticker"],st.session_state["start_date"],st.session_state["end_date"])
      max=s_data[["Open","Close","Volume","High","Low"]][s_data["Close"]==s_data["Close"].max()]
      mins=s_data[["Open","Close","Volume","High","Low"]][s_data["Close"]==s_data["Close"].min()]
      max_vol=s_data[["Open","Close","Volume","High","Low"]][s_data["Volume"]==s_data["Volume"].max()]
      min_vol=s_data[["Open","Close","Volume","High","Low"]][s_data["Volume"]==s_data["Volume"].min()]          
      
      st.success(f"Ticker: {st.session_state['ticker']} &nbsp;&nbsp;&nbsp; Start Date: {st.session_state['start_date']}&nbsp;&nbsp;&nbsp;&nbsp;End Date: {st.session_state['end_date']}")
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
      st.subheader(f"Graphical Analysis : {st.session_state['ticker']}") 
        
      
      #Tabs
      lin,bar=st.tabs(['Line Graph','Bar Graph'])
      with lin:
            
            fig = px.line(s_data, x=s_data.index, y=['Close','Open','High','Low'], title=f"Line Graph")
            st.plotly_chart(fig)
      with bar:
            fig = px.bar(s_data, x=s_data.index, y=s_data['Close'],title="Bar Graph")
            st.plotly_chart(fig) 
       # Download CSV button
      csv_data = s_data.reset_index().to_csv(index=False)
      st.download_button(
          label="Download CSV",
          data=csv_data,
          file_name=f"{st.session_state['ticker']}.csv",
          mime="application/octet-stream"
      )
    
except:
     st.warning("Enter correct values from side bar")      


          

 
