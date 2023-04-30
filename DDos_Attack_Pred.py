# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# loading the saved models

unsw_model = pickle.load(open('unsw_model.sav', 'rb'))
kdd_model = pickle.load(open('kdd_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('DDos Attack Prediction System',
                           ['Home',
                            'Data visualisation for UNSW Dataset',
                            'Data visualisation for KDD Dataset',
                          'UNSW dataset prediction',
                          'KDD dataset prediction'],
                          default_index=0)
def main():
    if (selected == 'Home'):
        # giving a title
        st.title("Machine Learning-Based Detection of Botnet DDoS Attacks: An Evaluation of Performance")
        image=Image.open("dataset-cover.jpg")
        st.image(image, caption='',output_format="auto")
        '''Botnet DDoS (Distributed denial of service) attacks pose a significant risk to network security. They 
can make websites and servers inaccessible to legitimate users by overwhelming them with traffic 
generated by a large number of compromised devices. The complexity of detecting and mitigating 
these attacks is due to their dynamic and evolving nature. Machine learning techniques, such as 
Support Vector Machine (SVM), Artificial Neural Network (ANN), Naïve Bayes (NB), Decision Tree (DT), 
and Unsupervised Learning (USML) (K-means, X-means etc.) have been proven effective in detecting 
botnet DDoS attacks. These techniques train models on large scale datasets of network traffic to 
identify patterns and anomalies that indicate malicious activity. Using machine learning for botnet 
DDoS attack detection offers a significant advantage in that it can adapt to new and evolving attack 
patterns. Traditional rule-based methods rely on predefined rules that may not be effective against 
sophisticated attacks. In contrast, machine learning models can continuously learn from new data and 
update their classification accordingly. The algorithms can be trained on feature extracted from 
network traffic, such as packet size, direction, and inter- arrival time. This paper presents an
experimental analysis of the performance of machine learning methods in detecting botnet DDoS 
attacks using two well-known datasets: UNBS-NB 15 and KDD cup99. The study demonstrates that 
machine learning techniques are effective in detecting botnet DDoS attacks, achieving high detection 
rates and low false positives. Overall, machine learning techniques provide a promising approach for 
detecting botnet DDoS attacks. They offer the ability to adapt to new attack patterns and achieve high 
detection rate with low false positives. As botnet DDoS attacks continue to evolve, it is crucial to 
develop effective direction methods to ensure network security. Machine learning techniques offer a 
valuable tool for achieving this goal.'''

    # UNSW dataset Prediction Page
    if (selected == 'UNSW dataset prediction'):
    
        # page title
        st.title('DDos Attack Prediction using UNSW Dataset')
        
        # getting the input data from the user
        synack = st.text_input('TCP connection setup time, the time between the SYN and the SYN_ACK packets - synack')
        sttl = st.text_input('Source to destination time to live value - sttl')
        stcpb = st.text_input('Source TCP base sequence number - stcpb')
        state_INT = st.text_input('Indicator to the state and its dependent protocol, e.g. ACC, CLO, CON, ECO, ECR, FIN, INT, MAS, PAR, REQ, RST, TST, TXD, URH, URN, and (-) (if not used state) - state_INT')
        smean = st.text_input('Mean of the ?ow packet size transmitted by the src  - smean')
        sload = st.text_input('Source bits per second - sload')
        sjit = st.text_input('Source jitter (mSec) - sjit')
        sbytes = st.text_input('Source to destination transaction bytes - sbytes')
        rate = st.text_input('rate')
        dur = st.text_input('Record total duration - dur')
        dttl = st.text_input('Destination to source time to live value - dttl')
        dtcpb = st.text_input('Destination TCP base sequence number - dtcpb')
        dmean = st.text_input('Mean of the ?ow packet size transmitted by the dst - dmean')
        dload = st.text_input('Destination bits per second - dload')
        djit = st.text_input('Destination jitter (mSec) - djit')
        dinpkt = st.text_input('Destination interpacket arrival time (mSec) - dinpkt')
        dbytes = st.text_input('Destination to source transaction bytes - dbytes')
        ct_state_ttl = st.text_input('No. for each state (6) according to specific range of values for source/destination time to live (10) (11) - ct_state_ttl')
        ct_dst_sport_ltm = st.text_input('No of connections of the same destination address (3) and the source port (2) in 100 connections according to the last time (26) - ct_dst_sport_ltm')
        ackdat = st.text_input('TCP connection setup time, the time between the SYN_ACK and the ACK packets - ackdat')
        
        # code for Prediction
        unsw_prediction = ''
        
        # creating a button for Prediction  
        if st.button('UNSW dataset prediction Result'):
            unsw_prediction = unswmodel_prediction([[synack,sttl,stcpb,state_INT,smean,sload,sjit,sbytes,rate,dur,dttl,dtcpb,dmean,dload,djit,dinpkt,dbytes,ct_state_ttl,ct_dst_sport_ltm,ackdat]])
            
        st.success(unsw_prediction)
    # KDD dataset Prediction Page
    if (selected == 'KDD dataset prediction'):
    
        # page title
        st.title('DDos Attack Prediction using KDD Dataset')
    
        # getting the input data from the user
        srv_diff_host_rate = st.text_input('Percentage of connections to different hosts - srv_diff_host_rate')
        srv_count = st.text_input('Number of connections to same service as currentconnection in past two seconds - srv_count')
        src_bytes = st.text_input('Number of data bytes from src to dst - src_bytes')
        serror_rate = st.text_input('Percentage of connections that have ‘SYN’ errors - serror_rate')
        same_srv_rate = st.text_input('Percentage of connections to the same service - same_srv_rate')
        protocol_type_udp = st.text_input('Protocol type UDP')
        protocol_type_tcp = st.text_input('Protocol type TCP')
        protocol_type_icmp = st.text_input('Protocol type ICMP')
        logged_in = st.text_input('1 if successfully logged in; else 0 - logged_in')
        flag_SF = st.text_input('Normal or error status flag of connection - flag_SF')
        flag_S0 = st.text_input('Normal or error status flag of connection - flag_S0')
        duration = st.text_input('Duration of connection in seconds - duration')
        dst_host_srv_diff_host_rate = st.text_input('Percentage of connections to same service coming from diff - hostdst_host_srv_diff_host_rate')
        dst_host_srv_count = st.text_input('Count of connections having same dst host andusing same service - dst_host_srv_count')
        dst_host_same_src_port_rate = st.text_input('Percentage of connections to current host having same src port - dst_host_same_src_port_rate')
        dst_host_diff_srv_rate = st.text_input('Percentage of different services on current host - dst_host_diff_srv_rate')
        dst_host_count = st.text_input('Count of connections having same dst host - dst_host_count')
        dst_bytes = st.text_input('Bytes from dst to src - dst_bytes')
        diff_srv_rate = st.text_input('Percentage of connections to different services - diff_srv_rate')
        count = st.text_input('Number of connections to same host as currentconnection in past two seconds - count')
        
        kdd_prediction = ''
        
        # creating a button for Prediction
        if st.button('KDD dataset prediction Result'):
            kdd_prediction = kddmodel_prediction([[srv_diff_host_rate,srv_count,src_bytes,serror_rate,same_srv_rate,protocol_type_udp,protocol_type_tcp,protocol_type_icmp,logged_in,flag_SF,flag_S0,duration,dst_host_srv_diff_host_rate,dst_host_srv_count,dst_host_same_src_port_rate,dst_host_diff_srv_rate,dst_host_count,dst_bytes,diff_srv_rate,count]])
        
        st.success(kdd_prediction)
    
# creating a function for Prediction
def unswmodel_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    input_data_reshaped = input_data_reshaped.astype(int)

    unsw_prediction = unsw_model.predict(input_data_reshaped)
    print(unsw_prediction)
    
    if (unsw_prediction[0] == 1):
        return 'It is not normal traffic'
    else:
        return 'It is normal traffic'

# creating a function for Prediction
def kddmodel_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    input_data_reshaped = input_data_reshaped.astype(int)
    
    kdd_prediction = kdd_model.predict(input_data_reshaped)
    print(kdd_prediction)
    
    if (kdd_prediction[0] == 1):
        return 'It is not normal traffic'
    else:
        return 'It is normal traffic'
    
if (selected == 'Data visualisation for UNSW Dataset'):
    st.title('Data visualisation for UNSW Dataset')
    data=pd.read_csv('UNSW_NB15_training-set.csv.zip')
    
    if st.checkbox("display dataset"):
        st.dataframe(data.head(10))
        
    if st.checkbox("display correlation"):  
        cor=data.corr()
        top_corr_feature=cor.index
        fig = plt.figure(figsize=(10,10))
        sns.heatmap(data[top_corr_feature].corr(),annot=True,cmap="RdYlGn")
        st.title("HEATMAP")
        st.pyplot(fig)
        
    if st.checkbox("bargraph visualisation of data"):
        fig1 = plt.figure(figsize=(20,20))
        plt.title("count of protocol")
        sns.countplot(x="proto", data=data)
        
        fig2 = plt.figure(figsize=(20, 20))
        plt.title("count of service")
        sns.countplot(x="service", data=data)
        
        fig3 = plt.figure(figsize=(20, 20))
        sns.countplot(x="state", data=data)
        plt.title("count of state")
        
        col1, col2 ,col3 = st.columns(3)
        
        with col1:
            st.pyplot(fig1)
        with col2:
            st.pyplot(fig2)
        with col3:
            st.pyplot(fig3)
   
if (selected == 'Data visualisation for KDD Dataset'):
    st.title('Data visualisation for KDD Dataset')
    data=pd.read_csv('kddcup.csv.zip',names=['duration', 'protocol_type', 'service', 'flag', 'src_bytes',
       'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
       'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',
       'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
       'num_access_files', 'num_outbound_cmds', 'is_host_login',
       'is_guest_login', 'count', 'srv_count', 'serror_rate',
       'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
       'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
       'dst_host_srv_count', 'dst_host_same_srv_rate',
       'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
       'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
       'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
       'dst_host_srv_rerror_rate', 'target'])
    
    if st.checkbox("display dataset"):
        st.dataframe(data.head(10))
        
    if st.checkbox("display correlation"):  
        cor=data.corr()
        top_corr_feature=cor.index
        fig = plt.figure(figsize=(10,10))
        sns.heatmap(data[top_corr_feature].corr(),annot=True,cmap="RdYlGn")
        st.title("HEATMAP")
        st.pyplot(fig)
        
    if st.checkbox("bargraph visualisation of data"):
       fig1 = plt.figure(figsize=(20,20))
       plt.title("count of protocol_type")
       sns.countplot(x="protocol_type", data=data)
       
       fig2 = plt.figure(figsize=(20, 20))
       plt.title("count of flag")
       sns.countplot(x="flag", data=data)
       
       fig3 = plt.figure(figsize=(20, 20))
       sns.countplot(x="service", data=data)
       plt.title("count of service")
       
       col1, col2 ,col3 = st.columns(3)
       
       with col1:
           st.pyplot(fig1)
       with col2:
           st.pyplot(fig2)
       with col3:
           st.pyplot(fig3)
    
        
if __name__ == '__main__':
    main()



    
