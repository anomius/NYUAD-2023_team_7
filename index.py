import numpy as np
import streamlit as st
import pandas as pd
from contextlib import contextmanager, redirect_stdout
from io import StringIO
from streamlit_toggle import st_toggle_switch

@contextmanager
def st_capture(output_func):
    with StringIO() as stdout, redirect_stdout(stdout):
        old_write = stdout.write

        def new_write(string):
            ret = old_write(string)
            output_func(stdout.getvalue())
            return ret
        
        stdout.write = new_write
        yield
        
st.title('AqriCult')
mode = st_toggle_switch(
    label="Simulation Mode",
    key="Simulation",
    default_value=False,
    label_after=False,
)

no_of_plants=st.number_input('Number of Plants', 1, 7, 3)

itrg=st.tabs([str(i) for i in range(no_of_plants)])
for i in itrg:
    with i:
        type=st.selectbox('Type of Plant', ['Wheat', 'Chickpea', 'Beetroot', 'Eggplant'],key="type"+str(i))
        if type=='Wheat':
            #st.image('https://energyeducation.ca/wiki/images/thumb/d/d6/Coal_power_plant_Datteln_2_Crop1.png/553px-Coal_power_plant_Datteln_2_Crop1.png')
            st.write("🌾")
        elif type=='Cheakpea':
            st.write("🌱")
        elif type=='Beetroot':
            #st.image('https://energyeducation.ca/wiki/images/thumb/4/4d/Fermi_NPP.jpg/627px-Fermi_NPP.jpg')
            st.write("🌿")
        elif type=='Eggplant':
            #st.image('https://energyeducation.ca/wiki/images/thumb/0/04/Solar_farm.jpg/680px-Solar_farm.jpg')
            st.write("🍆")
        
        a=st.number_input('Fertilizer', 0.1, key='a'+str(i))
        b=st.number_input('Expected Yield', 0.1, key='b'+str(i))
        c=st.number_input(
            'Environmental Impact of Plant', 0.1, key='c'+str(i))
        min_power=st.number_input(
            'Minimum Price of Plant', 0.1, key='min'+str(i))
        max_power=st.number_input(
            'Minimum Price of Plant', 0.1, key='max'+str(i))