#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('myocardialinfractionn.pkl', 'rb')
classifier = pickle.load(pickle_in)


def welcome():
    return 'welcome all'


# defining the function which will make the prediction using
# the data which the user inputs
def prediction(AGE, SEX, INF_ANAM, STENOK_AN, FK_STENOK, IBS_POST, GB, ZSN_A,
               nr_01, nr_04, np_01, np_08, np_10, endocr_01, endocr_02,
               zab_leg_02, zab_leg_03, S_AD_ORIT, D_AD_ORIT, O_L_POST,
               K_SH_POST, MP_TP_POST, SVT_POST, FIB_G_POST, ant_im, lat_im,
               inf_im, IM_PG_P, ritm_ecg_p_01, ritm_ecg_p_02, ritm_ecg_p_04,
               ritm_ecg_p_07, n_r_ecg_p_01, n_r_ecg_p_02, n_r_ecg_p_04,
               n_r_ecg_p_05, n_r_ecg_p_06, n_r_ecg_p_08, n_p_ecg_p_03,
               n_p_ecg_p_06, n_p_ecg_p_08, n_p_ecg_p_12, K_BLOOD, NA_BLOOD,
               ALT_BLOOD, AST_BLOOD, L_BLOOD, ROE, TIME_B_S, R_AB_1_n,
               R_AB_3_n, NITR_S, NA_R_1_n, NA_R_3_n, NOT_NA_1_n, NOT_NA_3_n,
               B_BLOK_S_n, ANT_CA_S_n, GEPAR_S_n, ASP_S_n, FIBR_JELUD,
               A_V_BLOK, OTEK_LANC, RAZRIV, ZSN, REC_IM, P_IM_STEN):

    prediction = classifier.predict([[
        AGE, SEX, INF_ANAM, STENOK_AN, FK_STENOK, IBS_POST, GB, ZSN_A, nr_01,
        nr_04, np_01, np_08, np_10, endocr_01, endocr_02, zab_leg_02,
        zab_leg_03, S_AD_ORIT, D_AD_ORIT, O_L_POST, K_SH_POST, MP_TP_POST,
        SVT_POST, FIB_G_POST, ant_im, lat_im, inf_im, IM_PG_P, ritm_ecg_p_01,
        ritm_ecg_p_02, ritm_ecg_p_04, ritm_ecg_p_07, n_r_ecg_p_01,
        n_r_ecg_p_02, n_r_ecg_p_04, n_r_ecg_p_05, n_r_ecg_p_06, n_r_ecg_p_08,
        n_p_ecg_p_03, n_p_ecg_p_06, n_p_ecg_p_08, n_p_ecg_p_12, K_BLOOD,
        NA_BLOOD, ALT_BLOOD, AST_BLOOD, L_BLOOD, ROE, TIME_B_S, R_AB_1_n,
        R_AB_3_n, NITR_S, NA_R_1_n, NA_R_3_n, NOT_NA_1_n, NOT_NA_3_n,
        B_BLOK_S_n, ANT_CA_S_n, GEPAR_S_n, ASP_S_n, FIBR_JELUD, A_V_BLOK,
        OTEK_LANC, RAZRIV, ZSN, REC_IM, P_IM_STEN
    ]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("MYOCARDIAL INFRACTION")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">MYOCADIAL INFRACTION Classifier ML App </h1>
    </div>
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)
    if st.button("About Project"):
        st.text("Classifying the types of heartattack")

    if st.checkbox("TEAM-3"):
        st.text("RANGEETHA")
        st.text("SRINA")
        st.text("RAKSHI")
        st.text("RANJEET")
        st.text("AKASH")

        st.text("PREM")

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction

    AGE = st.number_input("AGE", key="1")
    SEX = st.selectbox("SEX", (0, 1), key="2")
    INF_ANAM = st.selectbox("INF_ANAM", (0, 1, 2, 3), key="3")
    STENOK_AN = st.selectbox("STENOK_AN", (0, 1, 2, 3, 4), key="4")
    FK_STENOK = st.selectbox("FK_STENOK", (0, 1, 2, 3, 4), key="5")
    IBS_POST = st.selectbox("IBS_POST", (0, 1, 2), key="6")
    GB = st.selectbox("GB", (0, 1, 2, 3), key="7")
    ZSN_A = st.selectbox("ZSN_A", (0, 1, 2, 3, 4), key="8")
    nr_01 = st.selectbox("nr_01", (0, 1), key="9")
    nr_04 = st.selectbox("nr_04", (0, 1), key="10")
    np_01 = st.selectbox("np_01", (0, 1), key="11")
    np_08 = st.selectbox("np_08", (0, 1), key="12")
    np_08 = st.selectbox("np_08", (0, 1), key="13")
    np_10 = st.selectbox("np_10", (0, 1), key="14")
    endocr_01 = st.selectbox("endocr_01", (0, 1), key="15")
    endocr_02 = st.selectbox("endocr_02", (0, 1), key="16")
    zab_leg_02 = st.selectbox("zab_leg_02", (0, 1), key="17")
    zab_leg_03 = st.selectbox("zab_leg_03", (0, 1), key="18")
    S_AD_ORIT = st.number_input("S_AD_ORIT", key="19")
    D_AD_ORIT = st.number_input("D_AD_ORIT", key="20")
    O_L_POST = st.selectbox("O_L_POST", (0, 1), key="21")
    K_SH_POST = st.selectbox("K_SH_POST", (0, 1), key="22")
    MP_TP_POST = st.selectbox("MP_TP_POST", (0, 1), key="23")
    SVT_POST = st.selectbox("SVT_POST", (0, 1), key="24")
    FIB_G_POST = st.selectbox("FIB_G_POST", (0, 1), key="25")
    ant_im = st.selectbox("ant_im", (0, 1, 2, 3), key="26")
    lat_im = st.selectbox("lat_im", (0, 1, 2, 3, 4), key="27")
    inf_im = st.selectbox("inf_im", (0, 1, 2, 3, 4), key="28")
    IM_PG_P = st.selectbox("IM_PG_P", (0, 1), key="29")
    ritm_ecg_p_01 = st.selectbox("ritm_ecg_p_01", (0, 1), key="30")
    ritm_ecg_p_02 = st.selectbox("ritm_ecg_p_02", (0, 1), key="31")
    ritm_ecg_p_04 = st.selectbox("ritm_ecg_p_04", (0, 1), key="32")
    ritm_ecg_p_07 = st.selectbox("ritm_ecg_p_07", (0, 1), key="33")
    n_r_ecg_p_01 = st.selectbox("n_r_ecg_p_01", (0, 1), key="34")
    n_r_ecg_p_02 = st.selectbox("n_r_ecg_p_02", (0, 1), key="35")
    n_r_ecg_p_04 = st.selectbox("n_r_ecg_p_04", (0, 1), key="36")
    n_r_ecg_p_05 = st.selectbox("n_r_ecg_p_05", (0, 1), key="37")
    n_r_ecg_p_06 = st.selectbox("n_r_ecg_p_06", (0, 1), key="38")
    n_r_ecg_p_08 = st.selectbox("n_r_ecg_p_08", (0, 1), key="39")
    n_p_ecg_p_03 = st.selectbox("n_p_ecg_p_03", (0, 1), key="40")
    n_p_ecg_p_06 = st.selectbox("n_p_ecg_p_06", (0, 1), key="41")
    n_p_ecg_p_08 = st.selectbox("n_p_ecg_p_08", (0, 1), key="42")
    n_p_ecg_p_12 = st.selectbox("n_p_ecg_p_12", (0, 1), key="43")
    K_BLOOD = st.number_input("K_BLOOD", key="44")
    NA_BLOOD = st.number_input("NA_BLOOD", key="45")
    ALT_BLOOD = st.number_input("ALT_BLOOD", key="46")
    AST_BLOOD = st.number_input("AST_BLOOD", key="47")
    L_BLOOD = st.number_input("L_BLOOD", key="48")
    ROE = st.number_input("ROE", key="49")
    TIME_B_S = st.selectbox("TIME_B_S", (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
                            key="50")
    R_AB_1_n = st.selectbox("R_AB_1_n", (0, 1, 2, 3), key="51")
    R_AB_3_n = st.selectbox("R_AB_3_n", (0, 1, 2, 3), key="52")
    NITR_S = st.selectbox("NITR_S", (0, 1, 2, 3), key="53")
    NA_R_1_n = st.selectbox("NA_R_1_n", (0, 1, 2, 3, 4), key="54")
    NA_R_3_n = st.selectbox("NA_R_3_n", (0, 1, 2), key="55")
    NOT_NA_1_n = st.selectbox("NOT_NA_1_n", (0, 1, 2, 3, 4), key="56")
    NOT_NA_3_n = st.selectbox("NOT_NA_3_n", (0, 1, 2), key="57")
    B_BLOK_S_n = st.selectbox("B_BLOK_S_n", (0, 1), key="58")
    ANT_CA_S_n = st.selectbox("ANT_CA_S_n", (0, 1), key="59")
    GEPAR_S_n = st.selectbox("GEPAR_S_n", (0, 1), key="60")
    ASP_S_n = st.selectbox("ASP_S_n", (0, 1), key="61")
    FIBR_JELUD = st.selectbox("FIBR_JELUD", (0, 1), key="62")
    A_V_BLOK = st.selectbox("A_V_BLOK", (0, 1), key="63")
    OTEK_LANC = st.selectbox("OTEK_LANC", (0, 1), key="64")
    RAZRIV = st.selectbox("RAZRIV", (0, 1), key="65")
    ZSN = st.selectbox("ZSN", (0, 1), key="66")
    REC_IM = st.selectbox("REC_IM", (0, 1), key="67")
    P_IM_STEN = st.selectbox("P_IM_STEN", (0, 1), key="68")
    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(
            AGE, SEX, INF_ANAM, STENOK_AN, FK_STENOK, IBS_POST, GB, ZSN_A,
            nr_01, nr_04, np_01, np_08, np_10, endocr_01, endocr_02,
            zab_leg_02, zab_leg_03, S_AD_ORIT, D_AD_ORIT, O_L_POST, K_SH_POST,
            MP_TP_POST, SVT_POST, FIB_G_POST, ant_im, lat_im, inf_im, IM_PG_P,
            ritm_ecg_p_01, ritm_ecg_p_02, ritm_ecg_p_04, ritm_ecg_p_07,
            n_r_ecg_p_01, n_r_ecg_p_02, n_r_ecg_p_04, n_r_ecg_p_05,
            n_r_ecg_p_06, n_r_ecg_p_08, n_p_ecg_p_03, n_p_ecg_p_06,
            n_p_ecg_p_08, n_p_ecg_p_12, K_BLOOD, NA_BLOOD, ALT_BLOOD,
            AST_BLOOD, L_BLOOD, ROE, TIME_B_S, R_AB_1_n, R_AB_3_n, NITR_S,
            NA_R_1_n, NA_R_3_n, NOT_NA_1_n, NOT_NA_3_n, B_BLOK_S_n, ANT_CA_S_n,
            GEPAR_S_n, ASP_S_n, FIBR_JELUD, A_V_BLOK, OTEK_LANC, RAZRIV, ZSN,
            REC_IM, P_IM_STEN)

        st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()

